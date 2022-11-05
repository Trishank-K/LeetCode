num = int(input())
st=""
Th = int(num/1000)
if(Th<4):
    st+= "M"*Th
num = num%1000
if(num/100<9):
    Fh = int(num/500)
    st+="D"*Fh
    num=num%500
    H= int(num/100)
    if(H<4):
        st+="C"*H
    else:
        st+="CD"
else:
    st+="CM"
num=num%100

if(num/10<9):
    F= int(num/50)
    st+="L"*F
    num=num%50
    T= int(num/10)
    if(T<4):
        st+="X"*T
    else:
        st+="XL"
else:
    st+="XC"
num=num%10

if(num<9):
    F= int(num/5)
    st+="V"*F
    num=num%5
    if(num<4):
        st+="I"*num
    else:
        st+="IV"
else:
    st+="IX"
print(st)