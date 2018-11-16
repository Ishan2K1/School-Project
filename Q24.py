s=input("Enter string here ")
s=s.lower()
k=input("Encrypt/Decrypt?: ")
try:
    r=int(input("Enter rotation number here "))
except:
    r=13
l=[]
f=""
if k.lower()=="decrypt":
    r=r*-1
if k.lower()=="encrypt"or k.lower()=='decrypt':
    for i in s:
        if i.isalpha():            
            if (ord(i)+r)>ord("z"):
                i=chr(ord("a")+((ord(i)+r)%ord("z"))-1)
                f+=i
            else:
                i=chr(ord(i)+r)
                f+=i
    print(f)
