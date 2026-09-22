import json,sys
c=sys.argv[1]
d=json.load(open(f'presets/{c}.build.json',encoding='utf-8')); d.pop('notes',None)
t=json.dumps(d,ensure_ascii=False,separators=(',',':'))
h=0
for ch in t: h=(h*31+ord(ch))%1000000007
sys.stdout.reconfigure(encoding='utf-8')
print(len(t),h)
print(t)
