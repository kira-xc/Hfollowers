import amino
from os import _exit
listall=[]
ll=[]
email=input("your email : ")
password=input("your password : ")
client=amino.Client()
client.login(email=email,password=password)
infoos=input("give me your profile link : ")
infoo=amino.Client().get_from_code(infoos)
userId=infoo.objectId
comId=infoo.path[1:infoo.path.index("/")]
print ("userId = ",userId)
print("comId = ",comId)
boolo=False
try:
    if comId!=0 and comId!="":
        boolo=True
except:
    boolo=False
    
    
if boolo:
    sub=amino.SubClient(comId=comId,profile=client.profile)
    start=0
    while start<2000:
        print("the start is : ",start)
        ll=[]
        listf=sub.get_user_followers(userId=userId,start=start,size=25)
        ll=[x for x,y in zip(listf.userId,listf.status) if y==10 or y==9]
        listall.extend(ll)
        start+=25
else:
    start=0
    while start<2000:
        print("the start is : ",start)
        ll=[]
        listf=client.get_user_followers(userId=userId,start=start,size=25)
        ll=[x for x,y in zip(listf.userId,listf.status) if y==10 or y==9]
        listall.extend(ll)
        start+=25
cpt=0
print("done !")
yyy=input(" you have "+str(len(listall)+" hidden and banned follower \ndo you delete him ? : ")
if yyy=="y":
    for x in listall:
        cpt+=1
        print(cpt,")- ",x,"testing ...")
        ret=1
        while ret!=200:
            if boolo:
                ret=sub.block(x)
            else:
                ret=client.block(x)
        ret=1
        while ret!=200:
            if boolo:
                ret=sub.unblock(x)
            else:
                ret=client.unblock(x)
        print(cpt,")-",x,"done !")
            
print("all done ! \n try after becouse the members letf that 2000 after this operations 👍")
_exit(1)
