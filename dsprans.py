x=int(input('enter product a quantity'))
y=int(input('enter product b quantity'))
z=int(input('enter product c quantity'))
prod={'a':20,'b':40,'c':50}
quant={'a':x,'b':y,'c':z}


f=0
ap=20
pf1=0
if x > 20:
    p1 = x * ap
    pf1 = p1 - (p1 * .10)
    f=1
elif x>10 :
    p1=x*ap
    pf1=p1-(p1*.05)

bp=40
pf2=0
if y > 20:
    p2 = y * bp
    pf2 = p2 - (p2 * .10)
    f=1
elif y>10 :
    p2=y*bp
    pf2=p2-(p2*.05)

cp=50
pf3=0
if z > 20:
    p3 = z * cp
    pf3 = p3 - (p3 * .10)
    f=1
elif z>10 :
    p3=z*cp
    pf3=p3-(p3*.05)

pf33=0
tq=x+y+z
if tq>30:
    if x>15:
        p1 = x * ap
        pf33 = (p1 - (p1 * .5))+(quant['b']*40+quant['c']*50)
    elif y>15:
        p2 = y * bp
        pf33 = (p2 - (p2 * .5))+(quant['a']*20+quant['c']*50)
    elif z>15:
        p3 = z * cp
        pf33 = (p3 - (p3 * .5))+(quant['a']*20+quant['b']*40)


tot=(x*ap)+(y*bp)+(z*cp)

pr=0
if tot>200:
    pr=tot-10



def discount(pf1,pf2,pf3,pf33,pr,f,q):
    disc={}
    pft=pf1+pf2+pf3
    if pft==0 and pf33==0:
        ta=pr
        disc['flat_10_discount'] = ta
        return disc
    elif pft!=0 and pf33==0:
        if pf1!=0 :
            if f==1:
                tot=pf1+(q['b']*40+q['c']*50)
                disc['bulk_10_discount'] = tot
            else:
                tot = pf1 + (q['b'] * 40 + q['c'] * 50)
                disc['bulk_5_discount'] = tot
        elif pf2!=0 :
            if f==1:
                tot=pf1+(q['a']*20+q['c']*50)
                disc['bulk_10_discount'] = tot
            else:
                tot = pf1 + (q['a'] * 20 + q['c'] * 50)
                disc['bulk_5_discount'] = tot
        elif pf3!=0 :
            if f==1:
                tot=pf1+(q['a']*20+q['b']*40)
                disc['bulk_10_discount'] = tot
            else:
                tot = pf1 + (q['a'] * 20 + q['b'] * 40)
                disc['bulk_5_discount'] = tot
        return disc
    else:
        disc['tiered_50_discount'] = pf33
        return disc


dp=discount(pf1,pf2,pf3,pf33,pr,f,quant)

sub=0
print('\tproduct\t quantity\tprice')
for i in prod:
    print(f'\t\t{i} \t\t{quant[i]} \t\t{prod[i]*quant[i]}$')
    sub+=prod[i]*quant[i]
print(f'\t\t\t   subtotal:{sub}$ ')
amount=0
for i,j in dp.items():
    amount=j
    print(f'discount type:{i}\n \t discounted amount:{j}')

tqt=tq
shfe=0
while tqt>0:
    tqt-=10
    shfe+=1
print(f'\t\t  shipping fee:{shfe*5}$ \n\tgift wrap fee: {tq}$ \n\t\t\t\ttotal:{amount+(shfe*5)+tq}')
