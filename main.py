import json,os,sys,urllib.request as u,urllib.error as e
V=[0,100,320,330,500,900,20000]
T=["BBBBGLL.G=8BBBBVGGL[LLV`ttttBBBB","!!$$!.BG$GLQ$BQV$GQV$BLQ!.BB!!$$",".8888GBB8LLL8BLL8GGL8BGL8BBB.888","BBBG=BBB=BBB=BBB=BBB=BBBGLLLBBBB",".88=8BGB8GGGBBGG=BGG8BGG8BBB.88=","V`LBVVBB8....$$!$!!!$!!!$!!!$!!!"]
KN=[33,31,-31,-33,18,14,-14,-18]
KI=[16,17,1,-15,-16,-17,-1,15]
BD=[17,15,-17,-15]
RD=[16,1,-16,-1]
Z=[];_x=88172645463325252
for _ in range(1689):
 _x=(_x*6364136223846793005+1442695040888963407)&((1<<64)-1);Z.append(_x)
B=[0]*128;S=1;C=0;E=-1;H=0;WK=4;BK=116;NODES=0;BUDGET=30000;TT={};KIL=[0]*64
SQS=[s for s in range(128) if not s&136]
def on(t):return 0<=t<128 and not t&136
def setup(f):
 p=f.split();b=[0]*128;r=7;fl=0
 for ch in p[0]:
  if ch=='/':r-=1;fl=0
  elif ch.isdigit():fl+=int(ch)
  else:
   v='PNBRQK'.index(ch.upper())+1;b[r*16+fl]=v if ch.isupper() else -v;fl+=1
 global B,S,C,E,H,WK,BK
 B=b;S=1 if p[1]=='w' else -1;C=0
 if 'K' in p[2]:C|=1
 if 'Q' in p[2]:C|=2
 if 'k' in p[2]:C|=4
 if 'q' in p[2]:C|=8
 E=-1
 if p[3]!='-':E=(int(p[3][1])-1)*16+'abcdefgh'.index(p[3][0])
 H=0
 for s in SQS:
  v=B[s]
  if v:H^=Z[(v+6)*128+s]
 if S<0:H^=Z[1664]
 H^=Z[1665+C]
 if E>=0:H^=Z[1681+(E&7)]
 WK=4;BK=116
 for s in SQS:
  if B[s]==6:WK=s
  if B[s]==-6:BK=s
def atk(sq,by):
 if by>0:
  for t in (sq-15,sq-17):
   if on(t) and B[t]==1:return 1
 else:
  for t in (sq+15,sq+17):
   if on(t) and B[t]==-1:return 1
 for o in KN:
  t=sq+o
  if on(t) and B[t]==by*2:return 1
 for o in KI:
  t=sq+o
  if on(t) and B[t]==by*6:return 1
 for o in BD:
  t=sq+o
  while on(t):
   v=B[t]
   if v:
    if v==by*3 or v==by*5:return 1
    break
   t+=o
 for o in RD:
  t=sq+o
  while on(t):
   v=B[t]
   if v:
    if v==by*4 or v==by*5:return 1
    break
   t+=o
 return 0
def gen(cap):
 ms=[]
 for f in SQS:
  p=B[f]
  if not p or (p>0)!=(S>0):continue
  a=abs(p);d=16*S
  if a==1:
   t=f+d
   if on(t) and not B[t]:
    if (t>>4)==(7 if S>0 else 0):
     for pr in (5,4,3,2):ms.append((0,f|t<<7|pr<<14))
    elif not cap:
     ms.append((0,f|t<<7))
     if (f>>4)==(1 if S>0 else 6):
      t2=f+2*d
      if on(t2) and not B[t2]:ms.append((0,f|t2<<7))
   for dd in (d-1,d+1):
    t=f+dd
    if not on(t):continue
    v=B[t]
    if v and (v>0)!=(S>0):
     if (t>>4)==(7 if S>0 else 0):
      for pr in (5,4,3,2):ms.append((10*V[abs(v)]-100,f|t<<7|pr<<14))
     else:ms.append((10*V[abs(v)]-100,f|t<<7))
    elif t==E and not v:
     ms.append((10*100-100,f|t<<7))
  elif a==2 or a==6:
   for o in (KN if a==2 else KI):
    t=f+o
    if not on(t):continue
    v=B[t]
    if not v:
     if not cap:ms.append((0,f|t<<7))
    elif (v>0)!=(S>0):ms.append((10*V[abs(v)]-V[a],f|t<<7))
  else:
   for o in ((BD if a==3 else RD if a==4 else BD+RD)):
    t=f+o
    while on(t):
     v=B[t]
     if not v:
      if not cap:ms.append((0,f|t<<7))
     else:
      if (v>0)!=(S>0):ms.append((10*V[abs(v)]-V[a],f|t<<7))
      break
     t+=o
 if not cap:
  if S>0:
   if C&1 and not B[5] and not B[6] and B[7]==4 and not atk(4,-1) and not atk(5,-1) and not atk(6,-1):ms.append((0,4|6<<7))
   if C&2 and not B[3] and not B[2] and not B[1] and B[0]==4 and not atk(4,-1) and not atk(3,-1) and not atk(2,-1):ms.append((0,4|2<<7))
  else:
   if C&4 and not B[117] and not B[118] and B[119]==-4 and not atk(116,1) and not atk(117,1) and not atk(118,1):ms.append((0,116|118<<7))
   if C&8 and not B[115] and not B[114] and not B[113] and B[112]==-4 and not atk(116,1) and not atk(115,1) and not atk(114,1):ms.append((0,116|114<<7))
 return ms
def make(m):
 global S,C,E,H,WK,BK
 f=m&127;t=(m>>7)&127;pr=m>>14;p=B[f];oc,oe,oh=C,E,H
 cap=B[t];cs=-1
 if abs(p)==1 and t==E and not cap:
  cs=t-16*S;cap=B[cs];B[cs]=0;H^=Z[(cap+6)*128+cs]
 B[f]=0;np=pr*S if pr else p;B[t]=np
 H^=Z[(p+6)*128+f];H^=Z[(np+6)*128+t]
 if cap and cs<0:H^=Z[(cap+6)*128+t]
 rf=rt=-1
 if abs(p)==6 and abs(t-f)==2:
  rf,rt=(f+3,f+1) if t>f else (f-4,f-1)
  r=B[rf];B[rf]=0;B[rt]=r;H^=Z[(r+6)*128+rf];H^=Z[(r+6)*128+rt]
 if abs(p)==6:
  if S>0:WK=t
  else:BK=t
 nc=C
 if abs(p)==6:nc&=12 if S>0 else 3
 for q,bb in ((0,2),(7,1),(112,8),(119,4)):
  if f==q or t==q:nc&=~bb
 if nc!=C:H^=Z[1665+C];H^=Z[1665+nc];C=nc
 ne=(f+t)//2 if abs(p)==1 and abs(t-f)==32 else -1
 if E>=0:H^=Z[1681+(E&7)]
 if ne>=0:H^=Z[1681+(ne&7)]
 E=ne;H^=Z[1664];S=-S
 return (cap,cs,oc,oe,oh,rf,rt)
def unmake(m,u):
 global S,C,E,H,WK,BK
 cap,cs,oc,oe,oh,rf,rt=u
 f=m&127;t=(m>>7)&127;pr=m>>14
 S=-S
 p=S if pr else B[t]
 if rf>=0:
  r=B[rt];B[rt]=0;B[rf]=r
 B[t]=0;B[f]=p
 if cap:B[cs if cs>=0 else t]=cap
 if abs(p)==6:
  if S>0:WK=f
  else:BK=f
 C,E,H=oc,oe,oh
def ev():
 s=0
 for sq in SQS:
  p=B[sq]
  if p:
   a=abs(p);i=(sq>>4)*4+min(sq&7,7-(sq&7))
   if p>0:s+=V[a]+ord(T[a-1][i])-66
   else:
    j=(7-(sq>>4))*4+min(sq&7,7-(sq&7));s-=V[a]+ord(T[a-1][j])-66
 return s*S
class Abort(Exception):pass
def qs(a,b):
 global NODES
 NODES+=1
 if NODES>BUDGET:raise Abort
 if atk(WK if S>0 else BK,-S):
  mv=gen(False)
 else:
  s=ev()
  if s>=b:return b
  if s>a:a=s
  mv=gen(True)
 for sc,m in sorted(mv,reverse=True):
  u=make(m)
  if atk(WK if S<0 else BK,S):unmake(m,u);continue
  v=-qs(-b,-a)
  unmake(m,u)
  if v>a:a=v
  if a>=b:break
 return a
def srch(d,a,b,ply):
 global NODES
 NODES+=1
 if NODES>BUDGET:raise Abort
 if d<=0:return qs(a,b)
 e=TT.get(H)
 tm=0
 if e and e[0]>=d:
  if e[2]==0:return e[1]
  if e[2]==1 and e[1]>=b:return e[1]
  if e[2]==2 and e[1]<=a:return e[1]
  tm=e[3]
 ms=gen(False)
 if tm:
  for i,(sc,m) in enumerate(ms):
   if m==tm:ms[i]=(1<<20,m);break
 ms.sort(reverse=True)
 best=-999999;bm=0;fl=2
 for sc,m in ms:
  iscap=B[(m>>7)&127]!=0 or (abs(B[m&127])==1 and ((m>>7)&127)==E)
  u=make(m)
  if atk(WK if S<0 else BK,S):unmake(m,u);continue
  v=-srch(d-1,-b,-a,ply+1)
  unmake(m,u)
  if v>best:best=v;bm=m
  if v>a:a=v
  if a>=b:
   fl=1
   if not iscap:KIL[ply]=m
   break
 if best==-999999:return -20000+ply if atk(WK if S>0 else BK,-S) else 0
 TT[H]=(d,best,fl,bm)
 return best
def uci(m):
 f=m&127;t=(m>>7)&127;pr=m>>14
 s='abcdefgh'[f&7]+str((f>>4)+1)+'abcdefgh'[t&7]+str((t>>4)+1)
 if pr:s+='nbrq'[pr-2]
 return s
def tou(u):
 f=(int(u[1])-1)*16+'abcdefgh'.index(u[0]);t=(int(u[3])-1)*16+'abcdefgh'.index(u[2])
 pr=0
 if len(u)==5:pr='nbrq'.index(u[4])+2
 return f|t<<7|pr<<14
def root(legal):
 global NODES
 moves=[tou(x) for x in legal]
 best=moves[0]
 for d in range(1,10):
  NODES=0;cur=best;bs=-999999
  try:
   for m in moves:
    u=make(m)
    if atk(WK if S<0 else BK,S):unmake(m,u);continue
    v=-srch(d-1,-999999,999999,1)
    unmake(m,u)
    if v>bs:bs=v;cur=m
   best=cur
  except Abort:
   break
 return uci(best)
ENV=os.environ.get("MAKEFUN_ENV_URL")
def post(p,b):
 r=u.Request(ENV+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 try:
  with u.urlopen(r) as x:return json.load(x)
 except e.HTTPError as ex:
  sys.exit(f"{p}: HTTP {ex.code}")
if __name__=='__main__':
 if not ENV:sys.exit("MAKEFUN_ENV_URL is not set")
 while True:
  g=post("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   setup(g["fen"])
   g=post("/move",{"game":g["game"],"move":root(g["legal_moves"])})
