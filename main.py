import json,os,sys,urllib.request as u
V=[0,100,320,330,500,900,20000]
T="BBBBGLL.G=8BBBBVGGL[LLV`ttttBBBB!!$$!.BG$GLQ$BQV$GQV$BLQ!.BB!!$$.8888GBB8LLL8BLL8GGL8BGL8BBB.888BBBG=BBB=BBB=BBB=BBB=BBBGLLLBBBB.88=8BGB8GGGBBGG=BGG8BGG8BBB.88=V`LBVVBB8....$$!$!!!$!!!$!!!$!!!"
KN=[33,31,-31,-33,18,14,-14,-18];BD=[17,15,-17,-15];RD=[16,1,-16,-1];KI=RD+BD
B=[0]*128;S=1;C=0;E=-1;K=4;k=116;N=0;G=30000;Q=[s for s in range(128)if not s&136]
def on(t):return 0<=t<128 and not t&136
def tu(u):
 f=(int(u[1])-1)*16+ord(u[0])-97;t=(int(u[3])-1)*16+ord(u[2])-97;pr=0
 if len(u)==5:pr='nbrq'.index(u[4])+2
 return f|t<<7|pr<<14
def mk(m):
 global S,C,E,K,k
 sv=(B[:],S,C,E,K,k);f=m&127;t=(m>>7)&127;pr=m>>14;p=B[f]
 if abs(p)==1 and t==E and not B[t]:B[t-16*S]=0
 B[f]=0;B[t]=pr*S if pr else p
 if abs(p)==6 and abs(t-f)==2:
  rf,rt=(f+3,f+1)if t>f else(f-4,f-1);r=B[rf];B[rf]=0;B[rt]=r
 if abs(p)==6:
  if S>0:K=t
  else:k=t
 nc=C
 if abs(p)==6:nc&=12 if S>0 else 3
 for q,bb in((0,2),(7,1),(112,8),(119,4)):
  if f==q or t==q:nc&=~bb
 C=nc;E=(f+t)//2 if abs(p)==1 and abs(t-f)==32 else -1;S=-S
 return sv
def uk(sv):
 global S,C,E,K,k
 B[:]=sv[0];S,C,E,K,k=sv[1:]
def st(mv):
 global B,S,C,E,K,k
 A=[4,2,3,5,6,3,2,4];B=[0]*128
 for i in range(8):B[i]=A[i];B[i+16]=1;B[i+96]=-1;B[i+112]=-A[i]
 S=1;C=15;E=-1;K=4;k=116
 for x in mv:mk(tu(x))
def ak(sq,by):
 for t in(sq-15*by,sq-17*by):
  if on(t)and B[t]==by:return 1
 for O,p in((KN,2),(KI,6)):
  for o in O:
   t=sq+o
   if on(t)and B[t]==by*p:return 1
 for O,p in((BD,3),(RD,4)):
  for o in O:
   t=sq+o
   while on(t)and not B[t]:t+=o
   if on(t)and(B[t]==by*p or B[t]==by*5):return 1
 return 0
def gn(cp):
 m=[];d=16*S
 for f in Q:
  p=B[f]
  if not p or p*S<0:continue
  a=abs(p)
  if a==1:
   t=f+d
   if on(t)and not B[t]:
    pr=(t>>4)==(7 if S>0 else 0);m.append((0,f|t<<7|(81920 if pr else 0)))
    if not cp and not pr and(f>>4)==(1 if S>0 else 6):
     x=f+2*d
     if on(x)and not B[x]:m.append((0,f|x<<7))
   for e in(d-1,d+1):
    t=f+e
    if not on(t):continue
    v=B[t]
    if v*S<0:m.append((10*V[abs(v)]-100,f|t<<7|(81920 if(t>>4)==(7 if S>0 else 0)else 0)))
    elif t==E:m.append((900,f|t<<7))
  else:
   O=KN if a==2 else KI if a==6 else BD if a==3 else RD if a==4 else BD+RD;sl=a>2 and a!=6
   for o in O:
    t=f+o
    while on(t):
     v=B[t]
     if not v:
      if not cp:m.append((0,f|t<<7))
     else:
      if v*S<0:m.append((10*V[abs(v)]-V[a],f|t<<7))
      break
     if not sl:break
     t+=o
 if not cp:
  for a_,b_,c_,e_,g_,h_ in((4,7,6,5,1,-1),(4,0,2,3,2,1),(116,119,118,117,4,-1),(116,112,114,115,8,113)):
   if C&g_ and B[b_]==4*S and not B[e_]and not B[c_]and(h_<0 or not B[h_])and not(ak(a_,-S)or ak(e_,-S)or ak(c_,-S)):m.append((0,a_|c_<<7))
 return m
def ev():
 s=0
 for sq in Q:
  p=B[sq]
  if p:
   a=abs(p);r=sq>>4;f=min(sq&7,7-(sq&7));i=(r if p>0 else 7-r)*4+f;s+=(V[a]+ord(T[(a-1)*32+i])-66)*(1 if p>0 else -1)
 return s*S
Ab=Exception
def sr(d,a,b,pl):
 global N
 N+=1
 if N>G:raise Ab
 if d<=0:
  if ak(K if S>0 else k,-S):mv=gn(0)
  else:
   s=ev()
   if s>=b:return b
   if s>a:a=s
   mv=gn(1)
 else:mv=gn(0)
 f=0
 for sc_,m in sorted(mv,reverse=True):
  sv=mk(m)
  if ak(K if S<0 else k,S):uk(sv);continue
  f=1;v=-sr(d-1,-b,-a,pl+1);uk(sv)
  if v>a:a=v
  if a>=b:break
 if not f:return(-20000+pl)if ak(K if S>0 else k,-S)else(0 if d>0 else a)
 return a
def rt(lg):
 global N
 mv=[tu(x)for x in lg];best=mv[0]
 for d in range(1,10):
  N=0;cur=best;bs=-999999
  try:
   for m in mv:
    sv=mk(m)
    if ak(K if S<0 else k,S):uk(sv);continue
    v=-sr(d-1,-999999,999999,1);uk(sv)
    if v>bs:bs=v;cur=m
   best=cur
  except Ab:break
 f=best&127;t=(best>>7)&127;pr=best>>14;s=chr(97+(f&7))+str((f>>4)+1)+chr(97+(t&7))+str((t>>4)+1)
 return s+('nbrq'[pr-2]if pr else '')
EN=os.environ["MAKEFUN_ENV_URL"]
def po(p,b):
 q=u.Request(EN+p,data=json.dumps(b).encode())
 try:
  with u.urlopen(q)as x:return json.load(x)
 except Exception:sys.exit(9)
while 1:
 g=po("/game",{})
 if"game"not in g:break
 while g["status"]=="your_move":
  st(g["moves"]);g=po("/move",{"game":g["game"],"move":rt(g["legal_moves"])})
