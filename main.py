import json,os,urllib.request as u
V=[0,100,320,330,500,900,9999]
T="BBBBGLL.G=8BBBBVGGL[LLV`ttttBBBB!!$$!.BG$GLQ$BQV$GQV$BLQ!.BB!!$$.8888GBB8LLL8BLL8GGL8BGL8BBB.888BBBG=BBB=BBB=BBB=BBB=BBBGLLLBBBB"
P=[ord(c)-66 for c in T]
KN=[33,31,-31,-33,18,14,-14,-18];BD=[17,15,-17,-15];RD=[16,1,-16,-1];KI=RD+BD;OF=(0,0,KN,BD,RD,BD+RD,KI)
D={0:2,7:1,112:8,119:4}
B=[0]*128;S=1;C=0;E=-1;K=4;k=116;N=0;G=50000;H=0;TT={}
R=[];x=1
for i in range(1665):x=x*1103515245+12345&2147483647;R+=[x]
O=lambda t:not t&136
def tu(u):
 f=int(u[1])*16+ord(u[0])-113;t=int(u[3])*16+ord(u[2])-113
 return f|t<<7|(('nbrq'.find(u[4])+2)<<14 if len(u)==5 else 0)
def mk(m):
 global S,C,E,K,k,H
 sv=(B[:],S,C,E,K,k,H);f=m&127;t=(m>>7)&127;pr=m>>14;p=B[f];a=abs(p)
 H^=R[(p+6)*128+f]
 if B[t]:H^=R[(B[t]+6)*128+t]
 if a==1 and t==E and not B[t]:H^=R[((-S)+6)*128+t-16*S];B[t-16*S]=0
 B[f]=0;np=pr*S if pr else p;B[t]=np;H^=R[(np+6)*128+t]
 if a==6 and abs(t-f)==2:
  rf,rt=(f+3,f+1)if t>f else(f-4,f-1);r=B[rf];H^=R[(r+6)*128+rf];B[rf]=0;B[rt]=r;H^=R[(r+6)*128+rt]
 if a==6:K,k=(t,k)if S>0 else(K,t)
 nc=C
 if a==6:nc&=12 if S>0 else 3
 nc&=~(D.get(f,0)|D.get(t,0))
 C=nc;E=(f+t)//2 if a==1 and abs(t-f)==32 else -1;S=-S;H^=R[-1]
 return sv
def uk(sv):
 global S,C,E,K,k,H
 B[:]=sv[0];S,C,E,K,k,H=sv[1:]
def st(mv):
 global B,S,C,E,K,k,H
 B=[0]*128
 for i,c in enumerate('42356324'):B[i]=int(c);B[i+16]=1;B[i+96]=-1;B[i+112]=-int(c)
 S=1;C=15;E=-1;K=4;k=116;H=547197312
 for x in mv:mk(tu(x))
def ak(sq,by):
 for t in(sq-15*by,sq-17*by):
  if O(t)and B[t]==by:return 1
 for D_,p,sl in((KN,2,0),(KI,6,0),(BD,3,1),(RD,4,1)):
  for o in D_:
   t=sq+o
   while O(t):
    v=B[t]
    if v:
     if v==by*p or(sl and v==by*5):return 1
     break
    if not sl:break
    t+=o
 return 0
def gn(cp):
 m=[];d=16*S;r=7 if S>0 else 0;y=1 if S>0 else 6
 for f in range(128):
  p=B[f]
  if not p or p*S<0:continue
  a=abs(p)
  if a==1:
   for e in(d-1,d,d+1):
    t=f+e
    if not O(t):continue
    v=B[t];z=(t>>4)==r;q=z*81920
    if e==d:
     if v:continue
     m.append((0,f|t<<7|q))
     if not cp and not z and(f>>4)==y:
      x=f+2*d
      if O(x)and not B[x]:m.append((0,f|x<<7))
    elif v*S<0:m.append((10*V[abs(v)]-100,f|t<<7|q))
    elif t==E:m.append((900,f|t<<7))
  else:
   D_=OF[a];sl=a>2 and a!=6
   for o in D_:
    t=f+o
    while O(t):
     v=B[t]
     if v:
      if v*S<0:m.append((10*V[abs(v)]-V[a],f|t<<7))
      break
     if not cp:m.append((0,f|t<<7))
     if not sl:break
     t+=o
 if not cp:
  for a_,b_,c_,e_,g_,h_ in((4,7,6,5,1,-1),(4,0,2,3,2,1),(116,119,118,117,4,-1),(116,112,114,115,8,113)):
   if C&g_ and B[b_]==4*S and not B[e_]and not B[c_]and(h_<0 or not B[h_])and not(ak(a_,-S)or ak(e_,-S)or ak(c_,-S)):m.append((0,a_|c_<<7))
 return m
def ev():
 s=0
 for sq in range(128):
  p=B[sq]
  if p:
   a=abs(p);i=((sq>>4)if p>0 else 7-(sq>>4))*4+min(sq&7,7-(sq&7));s+=(V[a]+(P[(a-1)*32+i]if a<5 else 0))*(p//a)
 return s*S
Ab=Exception
def sr(d,a,b,pl):
 global N
 N+=1
 if N>G:raise Ab
 e=TT.get(H)
 if d<=0:
  if ak(K if S>0 else k,-S):mv=gn(0)
  else:
   s=ev()
   if s>=b:return b
   if s+900<a:return a
   if s>a:a=s
   mv=gn(1)
 else:
  mv=gn(0)
  if e:mv=[(99999 if m==e else s,m)for s,m in mv]
 f=0;bm=0;mv.sort(reverse=True)
 for sc_,m in mv:
  sv=mk(m)
  if ak(K if S<0 else k,S):uk(sv);continue
  f=1;v=-sr(d-1,-b,-a,pl+1);uk(sv)
  if v>a:a=v;bm=m
  if a>=b:break
 if not f:return(-9999+pl)if ak(K if S>0 else k,-S)else(0 if d>0 else a)
 if bm:TT[H]=bm
 return a
def rt(lg):
 global N
 mv=[tu(x)for x in lg];best=mv[0]
 for d in range(1,10):
  N=0;cur=best;bs=-9999
  try:
   for m in mv:
    sv=mk(m)
    v=-sr(d-1,-9999,9999,1);uk(sv)
    if v>bs:bs=v;cur=m
   best=cur
  except Ab:break
 f=best&127;t=(best>>7)&127;pr=best>>14
 return chr(97+f%8)+chr(49+f//16)+chr(97+t%8)+chr(49+t//16)+('nbrq'[pr-2]if pr else '')
EN=os.environ["MAKEFUN_ENV_URL"]
def po(p,b):return json.load(u.urlopen(u.Request(EN+p,data=json.dumps(b).encode())))
while 1:
 g=po("/game",{})
 if"game"not in g:break
 while g["status"]=="your_move":
  st(g["moves"]);g=po("/move",dict(game=g["game"],move=rt(g["legal_moves"])))
