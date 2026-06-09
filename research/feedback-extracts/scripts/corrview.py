import json, sys, re
fp=sys.argv[1]
def blocks(o):
    m=o.get("message") or {}; c=m.get("content")
    if isinstance(c,str): return [("text",c)]
    out=[]
    if isinstance(c,list):
        for b in c:
            if not isinstance(b,dict): continue
            t=b.get("type")
            if t=="text": out.append(("text",b.get("text","")))
            elif t=="tool_use": out.append(("tool",b.get("name","")))
            elif t=="tool_result": out.append(("tres",""))
    return out
turns=[]
for line in open(fp,errors="ignore"):
    line=line.strip()
    if not line: continue
    try:o=json.loads(line)
    except:continue
    typ=o.get("type"); m=o.get("message") or {}; role=m.get("role")
    if typ=="user" and role=="user":
        bs=blocks(o)
        if any(k=="tres" for k,_ in bs): continue
        txt=" ".join(v for k,v in bs if k=="text").strip()
        if txt: turns.append(("H",txt))
    elif typ=="assistant" and role=="assistant":
        bs=blocks(o)
        txt=" ".join(v for k,v in bs if k=="text").strip()
        tools=[v for k,v in bs if k=="tool"]
        seg=txt + (f" [tools: {', '.join(tools[:5])}]" if tools else "")
        if seg.strip(): turns.append(("A",seg.strip()))
merged=[]
for r,t in turns:
    if merged and merged[-1][0]==r: merged[-1]=(r,merged[-1][1]+" ⏎ "+t)
    else: merged.append((r,t))
# strip the giant skill-injection from first human turn
def clean(t): return re.sub(r"\s+"," ",t)
n=0
for i,(r,t) in enumerate(merged):
    if r=="H":
        if i==0: continue  # skip opening (skill injection)
        n+=1
        prev=clean(merged[i-1][1]) if i>0 and merged[i-1][0]=="A" else ""
        print(f"\n──── exchange {n} ────")
        if prev: print(f"[assistant proposed] …{prev[-380:]}")
        print(f"[REX] {clean(t)[:1200]}")
print(f"\n(total non-opening human turns: {n})")
