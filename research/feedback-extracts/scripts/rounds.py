import json, re, sys
def blocks(o):
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
def human(o):
    if o.get("type")!="user": return None
    m=o.get("message") or {}
    if m.get("role")!="user": return None
    c=m.get("content")
    if isinstance(c,str): return c
    if isinstance(c,list):
        if any(isinstance(b,dict) and b.get("type")=="tool_result" for b in c): return None
        return " ".join(b.get("text","") for b in c if isinstance(b,dict) and b.get("type")=="text")
    return None

fp=sys.argv[1]
events=[]
for line in open(fp,errors="ignore"):
    line=line.strip()
    if not line: continue
    try:o=json.loads(line)
    except:continue
    h=human(o)
    if h and h.strip():
        events.append(("H",re.sub(r'\s+',' ',h.strip())))
    for k,v,inp in blocks(o):
        if k=="tool" and v=="ExitPlanMode":
            plan=inp.get("plan","") if isinstance(inp,dict) else ""
            title=""
            mt=re.search(r'#\s*(.+)', plan)
            if mt: title=mt.group(1)[:70]
            events.append(("PLAN",f"({len(plan)} chars) {title}"))
# print the plan/feedback interleaving
rnd=0
for typ,txt in events:
    if typ=="PLAN":
        rnd+=1
        print(f"\n  ┌─ PLAN v{rnd}: {txt}")
    else:
        # only show human turns that look like plan feedback (skip 'go'/'confirm' one-worders unless near a plan)
        short = txt[:240]
        print(f"  └▶ [REX] {short}")
