import json, os, glob, re
BASE=os.path.expanduser("~/.claude/projects")
SKIP=("private-tmp","private-var","wg-probe","wg-int")

def content_blocks(o):
    m=o.get("message") or {}; c=m.get("content")
    if isinstance(c,str): return [("text",c,None)]
    out=[]
    if isinstance(c,list):
        for b in c:
            if isinstance(b,dict):
                t=b.get("type")
                if t=="text": out.append(("text",b.get("text",""),None))
                elif t=="tool_use": out.append(("tool",b.get("name",""),b.get("input")))
                elif t=="tool_result": out.append(("tres","",None))
    return out

# 1) How does a plan present? Inspect ONE known plan-mode session (seance)
seance="/Users/rexc/.claude/projects/-Users-rexc-Sites-seance/ae2ae299-7a09-4b9c-b273-32a88610b2a7.jsonl"
print("=== seance: ExitPlanMode tool calls (does the plan text get captured?) ===")
for line in open(seance,errors="ignore"):
    line=line.strip()
    if not line: continue
    try:o=json.loads(line)
    except:continue
    for k,v,inp in content_blocks(o):
        if k=="tool" and v in ("ExitPlanMode","EnterPlanMode"):
            plan=""
            if isinstance(inp,dict):
                plan=inp.get("plan") or inp.get("plan_text") or json.dumps(inp)[:300]
            print(f"  [{v}] input keys={list(inp.keys()) if isinstance(inp,dict) else type(inp).__name__}  plan~{len(plan)} chars")
            if plan: print("     plan head:", re.sub(r'\s+',' ',plan)[:200])

# 2) Across ALL candidates: count ExitPlanMode occurrences per session (= revision rounds)
print("\n=== plan-mode round structure across all real transcripts ===")
rows=[]
for proj in os.listdir(BASE):
    if any(s in proj for s in SKIP): continue
    pdir=os.path.join(BASE,proj)
    if not os.path.isdir(pdir): continue
    pretty=proj.lstrip('-').replace('-Users-rexc-Sites-','').replace('-Users-rexc-','')
    for fp in glob.glob(os.path.join(pdir,"*.jsonl")):
        exits=enters=interrupts=0
        for line in open(fp,errors="ignore"):
            line=line.strip()
            if not line: continue
            try:o=json.loads(line)
            except:continue
            # interrupts (user stopped to give plan feedback)
            m=o.get("message") or {}
            if o.get("type")=="user" and m.get("role")=="user":
                c=m.get("content")
                txt=c if isinstance(c,str) else " ".join(b.get("text","") for b in c if isinstance(b,dict) and b.get("type")=="text") if isinstance(c,list) else ""
                if "Request interrupted" in txt: interrupts+=1
            for k,v,inp in content_blocks(o):
                if k=="tool" and v=="ExitPlanMode": exits+=1
                if k=="tool" and v=="EnterPlanMode": enters+=1
        if exits>0 or interrupts>0:
            rows.append((exits,enters,interrupts,pretty,os.path.basename(fp)))
rows.sort(reverse=True)
print(f"sessions with >=1 ExitPlanMode or interrupt: {len(rows)}")
print(f"sessions with >=2 ExitPlanMode (multi-round plan revision): {len([r for r in rows if r[0]>=2])}")
print(f"\n{'exits':>5} {'enters':>6} {'intr':>4}  project / file")
for r in rows[:20]:
    print(f"{r[0]:5} {r[1]:6} {r[2]:4}  {r[3][:24]:24} {r[4][:20]}")
