import random
def reverse1( a):
    temp=list(a)
    temp.reverse()
    a=''.join(temp)
    return a    

def encrypt(a):
    temp=list(a)
    item=temp.pop(0)
    temp.append(item)
    custom_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(3):
     c = random.choice(custom_list)
     temp.append(c)
    for i in range(3):
     c = random.choice(custom_list)
     temp.insert(0,c) 
     
    a=''.join(temp)
    return a

def decrypt(a):
    temp=list(a)
    
    j=0
    temp=temp[3:]
    for i in range(3):
        temp.pop()
    item=temp.pop()
    temp.insert(0,item)        
    a=''.join(temp)
    return a   
   
        
print("Press 1 : Encrypt Your Message \nPress 2 : Decrypt Your Message\n")   
p=int(input("Enter Your Choice : "))
if(p==1):
    a=input("\nEnter Message : ")
    if len(a)<3:
        a=reverse1(a)   
 
    else:
      a=encrypt(a)
    print("Your Message in Encrypted Version : ",a)  
if(p==2):
    a=input("\nEnter Message : ")
    if(len(a)<3):
        a=reverse1(a)
    else:
        a=decrypt(a) 
    print("Your Message in Decrypted Version : ",a)
