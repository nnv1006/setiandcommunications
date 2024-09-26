hexcode="4e656b7261736f76204e696b69746120566c6164696d69726f766963682031302e30362e32303033"
res=''
for i in range(0,len(hexcode),2):
    elem=hexcode[i]+hexcode[i+1]
    n=int(elem,16)
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    res +="0"+bStr+" "
print(res," ")

