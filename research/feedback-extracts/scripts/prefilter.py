import json, os, re, glob
from collections import defaultdict

BASE = os.path.expanduser("~/.claude/projects")
# real projects only — drop tmp/probe junk
SKIP = ("private-tmp", "private-var", "wg-probe", "wg-int")

corr = re.compile(r"\b(no,|nope|not quite|instead|actually|you missed|you forgot|"
    r"don'?t|do not|should have|shouldn'?t|that'?s wrong|that is wrong|incorrect|"
    r"revert|undo|too much|out of scope|why did you|why are you|stop|wait,|"
    r"rather than|no need|isn'?t what|not what i|that'?s not|let'?s not|"
    r"you can'?t|you shouldn'?t|don'?t do|remove that|take out|i didn'?t ask|"
    r"that wasn'?t|over-?engineer|simpler|too complex|back to|go back)\b", re.I)
planmark = re.compile(r"ExitPlanMode|exit_plan_mode|here'?s (my|the) plan|## plan|"
    r"## the plan|implementation plan|i'?ll plan|let me plan", re.I)

def human_text(o):
    """Return typed human text for a line, or '' if it's a tool_result / non-human."""
    if o.get("type") != "user": return ""
    m = o.get("message") or {}
    if m.get("role") != "user": return ""
    c = m.get("content")
    if isinstance(c, str): return c
    if isinstance(c, list):
        parts = []
        for b in c:
            if isinstance(b, dict):
                if b.get("type") == "tool_result": return ""   # tool output, not human
                if b.get("type") == "text": parts.append(b.get("text",""))
        return " ".join(parts)
    return ""

def all_text(o):
    m = o.get("message") or {}
    c = m.get("content")
    if isinstance(c, str): return c
    if isinstance(c, list):
        return " ".join(b.get("text","") if isinstance(b,dict) else "" for b in c)
    return ""

rows = []
for proj in sorted(os.listdir(BASE)):
    if any(s in proj for s in SKIP): continue
    pdir = os.path.join(BASE, proj)
    if not os.path.isdir(pdir): continue
    pretty = proj.lstrip("-").replace("-Users-rexc-Sites-","").replace("-Users-rexc-","")
    for fp in glob.glob(os.path.join(pdir, "*.jsonl")):
        humans=0; corrections=0; plan=False; title=""; first=""; ts0=ts1=""
        for line in open(fp, errors="ignore"):
            line=line.strip()
            if not line: continue
            try: o=json.loads(line)
            except: continue
            if o.get("type")=="custom-title" and o.get("title"): title=o["title"]
            t=o.get("timestamp","")
            if t:
                ts0=ts0 or t; ts1=t
            ht=human_text(o)
            if ht.strip():
                humans+=1
                if not first: first=ht.strip().replace("\n"," ")[:80]
                if corr.search(ht): corrections+=1
            if not plan and planmark.search(all_text(o)): plan=True
        if humans==0: continue
        rows.append(dict(proj=pretty, file=os.path.basename(fp), humans=humans,
                         corrections=corrections, plan=plan,
                         date=ts0[:10], title=title or first))

# candidate = has plan signal OR >=2 correction-signal human turns
def is_cand(r): return r["plan"] or r["corrections"]>=2
rows.sort(key=lambda r:(r["corrections"], r["humans"]), reverse=True)
cands=[r for r in rows if is_cand(r)]

print(f"Scanned {len(rows)} non-empty transcripts. Candidates: {len(cands)}\n")
byproj=defaultdict(lambda:[0,0])
for r in rows:
    byproj[r["proj"]][0]+=1
    if is_cand(r): byproj[r["proj"]][1]+=1
print(f"{'project':28} {'total':>6} {'cand':>6}")
for p,(tot,c) in sorted(byproj.items(), key=lambda x:-x[1][1]):
    print(f"{p:28} {tot:6} {c:6}")
print("\nTop 25 candidates by correction-signal:")
print(f"{'corr':>4} {'turns':>5} {'plan':>4}  {'date':10} {'project':22} title")
for r in cands[:25]:
    print(f"{r['corrections']:4} {r['humans']:5} {'Y' if r['plan'] else ' ':>4}  "
          f"{r['date']:10} {r['proj'][:22]:22} {r['title'][:46]}")

print("\n--- tiers (candidates only) ---")
for thr in (2,3,4,5):
    n=len([r for r in cands if r["corrections"]>=thr])
    print(f"corrections >= {thr}: {n} transcripts")
print(f"with plan-mode signal: {len([r for r in cands if r['plan']])}")
