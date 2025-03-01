# readme
# s is saari chats
# colon mtlb saari chats colon se phle ki
# count2 take account of ki sahaj ke kitne msg h
# count1 take account of ki meet ke kinte msg h 
# whole count total number of msg
# data is dictionary jo krega ki yha pe msg by person switch huye 
# timing take account of time ki in data ki kha kha pe switch hua 
# timing dono ko lekr chlta h jisme first msg even pe h and second msg odd pe
# datetime h us us time ki timing or date h jha par msg switch huye h
# data me date h jisme person switch huye h 
# time me time h jisme person switch huye h with pm
# time 2 me time split hoke h in 24 hours format
# delay pta rha h kitne der me next msg aya in minutes
# sum 1 sum2 use in avg finding
# file .read se change krna h jiise code socha hojayega 



#most chats month 
# how long youve been chaating done
# time spent toghether
# months ka toh hogya years ka rh rha h
# can we do like jitne bhi total no.of msg honge mlutiply by 40seconds to get time spend toghether
# first message kiske jyada the 
# interset level bhi firs tmessage se niklegs 
import os
from flask import Flask,render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.sql import func

app=Flask(__name__)

@app.route("/")
def upload_page():
    return render_template('upload.html')
    # text = request.form.get('fileContent', '')
    # print("Received file content:")
    # print(text)  # This will appear in your terminal


    # xx()
@app.route("/process", methods=['POST','GET'])
def process():
    # Get the file content from the hidden textarea in upload.html
    text = request.form.get('fileContent')
    print("Received file content:")
    print(text)  # This will print the file's text in your terminal

    # Process the file content and compute the required variables
    result = xx(text)

    # After processing, render the frontend page with the computed variables
    return render_template('frontend.html', **result)


@app.route("/upload-again", methods=['GET'])
def upload_again():
    return render_template('upload.html')
def xx(text):
    # f = open("C:\\Users\\meet1\\OneDrive\\Desktop\\New folder\\new.txt",'r',errors="ignore")
    # sx=f.readlines()
    data=text
    # print('as it ease')
    # print(data)
    userdata = [line.replace('\u202f', 'â€¯').strip() + '\n' for line in data.replace('\r', '').split('\n') if line.strip()]
    # xy=s.split('\n')
    # print("what i processed")
    # print(pro)
    # print('what i want')
    # print(sx)
    s=userdata
    # uploaded_file = request.files.get('file')
    # if not uploaded_file:
    #     print("No file uploaded")
    # s = uploaded_file.read().decode('utf-8', errors='ignore').splitlines()

    import re

    pattern = r'^\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2}â€¯[AP]M - .+?: '
    pro=[]
    # Ya agar Unicode me likhna chahte ho:
    # pattern = r'^\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2}\u202F[AP]M - .+?: '
    for i in range(len(s)):
        if re.match(pattern,s[i]):
            pro.append(s[i])
            # print("true")
        else:
            if pro:
            
                pro[-1]=pro[-1].rstrip("\n") + " " + s[i]
                
            
                # print("false")
    # print(pro)
    s=pro




    colon=[]
    msg=[]

    for line in s:
        x=line.split(": ")
        colon.append(x[0])
        msg.append(x[1])
    #print(colon)

    #extracting names of person
    sirfname=[]
    nameforset=[]
    for line in colon:
        x=line.split('-',1)
        sirfname.append(x[1])

    print(sirfname)
    for i in sirfname:
        if i not in nameforset:
            nameforset.append(i)


        
    print(nameforset)
    name1 = nameforset[0].split(':')[0].strip().lower() 
    name2 = nameforset[1].split(':')[0].strip().lower()
    name1=name1.strip()
    print(name1)
    name2=name2.strip()
    print(name2)
    print(type(name1))

    print(type('sahaj dce'))
    count2=0
    count1=0
    wholecount=1
    data={}
    monthc={}
    countmonth=[]
    for line in colon:
        if line.lower().count(name1): 
            data[wholecount]=True
            count1+=1
        if line.lower().count(name2):
            count2+=1
            data[wholecount]=False
        
        wholecount+=1
    print("no. of msg of first person : " , count1)
    print("no. of msg of second person : " , count2)
    print("total no . of msg" , (wholecount-1))
    dateall=set()
    yearall=set()
    monthall=set()
    #split date 
    for line in colon:
        x=line.split(", ")
        y=x[0].split("/") #3/31/34,301 pm -> 3,31,24 
    
        z=y[2].split("/") # date part ayega 
        yearall.add(int(z[0]))
        dateall.add(int(y[1]))
        monthall.add(int(y[0]))
    wholecount2=0
    yearc={}
    for line in colon:
        monthc={}
        for line in colon:
            
            x=line.split(", ")
            y=x[0].split("/") #3/31/34,301 pm -> 3,31,24 
            z=y[2].split("/")# date part ayega 
            wholecount2+=1
            monthc[y[0]]=monthc.get((y[0]),0)+1
        yearc[y[2]]=monthc
    print("wiat")   
    print(monthc)


    # print(wholecount2)



    # print("x",x)
    # print("y",y)
    # y m h saari date
    for i in range(len(y)):
        y[i]=int(y[i])

    lastdate=y

    # print("z",z)
    # print("monthall",monthall)
    # print("yearall",yearall)
    # print("dateall",dateall)
    yearall=list(yearall)

    x=yearall[0]
    y=yearall[len(yearall)-1]
    # print(y-x)



    for line in range(1):
        x=colon[line].split(", ")
        y=x[0].split("/")
        z=y[2].split("/")
    # print("accesing first meesage")
    # print(x,y,z)
    # y me sara maal h 
    for i in range(len(y)):
        y[i]=int(y[i])

    firstdate=y
    print("first date",firstdate)
    print("lastdate" , lastdate)
    timespent=[]
    for i in range(len(lastdate)):
        timespent.append(lastdate[i]-firstdate[i])
    # print("time spend",timespent)
    


    # Calculate components
    mahina = timespent[0]
    din = timespent[1]
    saal = timespent[2]

    # Adjust negative days by borrowing from months
    if din < 0:
        din += 30
        mahina -= 1

    # Adjust negative months by borrowing from years
    if mahina < 0:
        mahina += 12
        saal -= 1

    # Build the result string
    kitnedin = ""
    if saal != 0:
        kitnedin += f"{saal} years "
    if mahina != 0:
        kitnedin += f"{mahina} months "
    if din != 0:
        kitnedin += f"{din} day"

    print("kitnedin", kitnedin)


    #print(data)

    y=data[1] # kyuki 1 se hi start h it point first element
    timing=[1] # yeh like first msg tha kiska woh dekhega iske bina first is not accesible or first toh kisika msg toh hoga 
    for i,j in data.items():
        if j!=y:
            #print(i,"Number of line",j)
            timing.append(i)
            y=not(y)
    # print("timing",timing)
    datetime=[]
    for i in timing:
        y=colon[i-1]
        x=y.split(" - ")

        datetime.append(x[0])

    # print("datetime",datetime)
    date=[]
    time=[]
    for i in datetime:
        x=i.split(",")
        date.append(x[0])
        y=x[1].strip().split("â€¯")
        time.append(y)
    # print("dATE" ,date)
    # print("time" ,time)

    time2=[]
    for i in time:
        x=i[0].split(":")
        if i[1]=="PM":
            if i[0][0:2]=="12":
                time2.append([int(x[0]), int(x[1])])
            else:
                x[0]=int(x[0])+12
                time2.append([x[0],int(x[1])])
        else :
            x[0]=int(x[0]) 
            time2.append([x[0],int(x[1])])

    # print("time2",time2)
    delay=[]
    for i in range(len(date)-1):
        # print(i)
        if date[i]==date[i+1]:# date same
            # print(date[i])
            x=time2[i+1][0]-time2 [i][0]
            # print("x = ", x)
            y=time2[i+1][1]-time2[i][1]
            # print("y = ", y)
            x=x*60
            delay.append(x+y)
            # print(delay)

    # print(delay)
    sum1=0
    sum2=0
    # count1=0
    for i in range(len(delay)):
        if i%2 == 0:
            sum1=sum1+delay[i]

        else:
            sum2=sum2+delay[i]
    # print(sum1,sum2)
    if (len(delay)%2==0):
        avg1=sum1/(len(delay)/2)
        avg2=sum2/(len(delay)/2)
    else:
        avg1=sum1/(len(delay)/2+1)
        avg2=sum2/(len(delay)/2)
    print("person 1 in minutes",avg1)#in minutes
    print("person 2 in minutes",avg2)#in minutes
            
    # message per month






    text=" ".join(msg).replace("\n"," ")
    words=text.split(" ")# split into words
    # print(words)
    counter={}


    # for i in words:
    #     if i in counter:
    #         counter[i]+=1
    #     else:
    #         counter[i]=1
    # print(counter)
    # counter1=counter.items()
    # # print("items",counter1)
    # counter1=sorted(counter1,key=lambda x:x[1],reverse=True) # hum x[1] derhe h ki is basis pe sort kro
    # counter1=dict(counter1)
    # print("wait")
    # print(counter1)
    # # print(counter1)
    # filtered = filter(lambda x: len(x) > 2, counter1)
    # filtered_dict = dict((k, counter1[k]) for k in filtered)
    # # print(filtered_dict)
    # xx=list(filtered_dict)
    # print("your most used words is :")
    # for i in range(3):
    #     print(xx[i])
    def findingname(s):
        nameset=[]
        l=[]
        for line in s:
            x=line.split(" - ")
            y=x[1].split(":")
            l.append(y[0])

        for i in l:
            if i not in nameset:
                nameset.append(i)
        print(nameset) 
        name1=nameset[0]
        name2=nameset[1]
        return name1,name2
    name1,name2=findingname(s)

    li=[] #li me saare naam like line wise ki sahaj fir meet fir sahaj
    for line in s:
            x=line.split(" - ")
            y=x[1].split(":")
            li.append(y[0])
    # print(li)
    name1c=[] #kis kis jgh pe sahaj ka msg h index wise btayega
    name2c=[] # kis kis jgh pe meet ka msg h
    for i in range(len(li)):
        if li[i]==name1:
            name1c.append(i) #[0, 3, 4, 6, 7, 9]
        elif li[i] == name2:
            name2c.append(i) #[1, 2, 5, 8, 10]
    # print(name1c)
    # print(name2c)

    msg1=[]
    msg2=[]
    for i in range(len(msg)):
        if i in name1c:
            msg1.append(msg[i]) # ab yeh msg bhar rhe h good approach 
        elif i in name2c:
            msg2.append(msg[i])
    msg1=" ".join(msg1).replace('\n'," ")

    msg1=msg1.split(" ")

    msg2=" ".join(msg2).replace('\n'," ")
    msg2=msg2.split(" ")


    msg1d={} # msg1 dictionary
    msg2d={}
    for i in msg1: # yeh dictionary bnarhe h hum or hum word cound kr rhe h 
        if i in msg1d:
            msg1d[i]+=1
        else:
            msg1d[i]=1
    # print(msg1d)
    for i in msg2: #similar word count for msg2
        if i in msg2d:
            msg2d[i]+=1
        else:
            msg2d[i]=1
    # print(msg1d) 
    msg1d=msg1d.items() #items me toda
    msg2d=msg2d.items()

    msg1ds=sorted(msg1d,key=lambda x:x[1],reverse=True)
    msg1ds=dict(msg1ds)
    msg2ds=sorted(msg2d,key=lambda x:x[1],reverse=True)
    msg2ds=dict(msg2ds)
    # print(msg1ds)
    # print(msg2ds)
    filter1=filter(lambda x:len(x)>2,msg1ds)
    filter2=filter(lambda x:len(x)>2,msg2ds)
    # filter1=filter(lambda x:x!="<Media omitted>",msg1ds)

    filter1d=dict((k,msg1ds[k])for k in filter1)
    filter2d=dict((k,msg2ds[k])for k in filter2)
    try :
        filter1d.pop('omitted>')
    except KeyError: 
        pass
    try :
        filter2d.pop('omitted>')
    except KeyError: 
        pass

    print(f"{name1} most used word in the chat is ")
    filter1dl=list(filter1d)
    for i in range(3):
        print(filter1dl[i])
    print(f"{name2} most used word in the chat is ")
    filter2dl=list(filter2d)
    for i in range(3):
        print(filter2dl[i])
    # print(filter2d)
    print("next")


    print("space")
    # print(filter1d)


    #interest level 
    # avg response time ;
    # no. of messages 
    # length count in messages 
    str1=" "
    for i in msg1:
        str1 = str1 + i
    # print(str1)
    print("length count of msg1",len(str1))
    msgcountperson1=len(str1)

    str2=" "
    for i in msg2:
        str2=str2+i
    # print(str2)
    print("length count of msg2",len(str2))
    msgcountperson2=len(str2)


    interest1=[avg1,count1,len(str1)]
    interest2=[avg2,count2,len(str2)]
    print(interest1)
    print("breaK")
    print(interest2)
    # len(str)10 % jyada h 
    # count 20 % kam h 
    # reply speed 1500% jyada h 

    # delay mtlb kon kitna deri se msg bhej rha h 
    # highes probab
    def viaword(f1,f2,len1,len2):
    
        if len1>len2:
            bda=len1
            chota=len2
        else:
            bda=len2
            chota=len1

            
        if (chota+chota)<=bda:
            # print("+15% - 6%")
            plus=15
            minus=6
        elif(chota+(chota*0.75))<=bda:
            # print("+9.5 + krdo avg1 me , -2.38 avg2 me")
            plus=9.5
            minus=2.38
        elif(chota+(chota*0.5))<=bda:
            # print("+6.5 add krdo and --1.75 add krdo")
            plus=6.5
            minus=1.75
        elif(chota+(chota*0.25))<=bda:
            # print("+2.75%,add 0")
            plus=2.75
            minus=0
        elif(chota+(chota*0.05))<=bda:
            # print("+0,-0")
            plus=0
            minus=0
        if (len1>=len2):
            # jiska jyada h usime plus ho
            f1=f1+plus
            f2=f2-minus
            
        
            # print("first person is on lead")
            # print("second person :",f1)
            # print("first person :",f2)
            
            
        else:
        
            f2=f2+plus
            f1=f1-minus
        
            # print("second person is on lead")
            # print("second person :",f1)
            # print("first person :",f2)
        return f1,f2


    def findinginterestviadelay(avg1,avg2,len1,len2):
        print(avg1,avg2)
        # avg1=int(avg1)
        # avg2=int(avg2)
        maxavg=max(avg1,avg2)
        if maxavg==avg1:
            # print("avg1 is bda")
            bda=avg1
            chota=avg2
        else:
            # print("avg1 is chota")
            bda=avg2
            chota=avg1
            
        # minavg=min(avg1,avg2)

        int1=50
        int2=50
        # for message delay
        if (chota+chota)<=bda:
            # print("+32% - 15%")
            plus=32
            minus=15
        elif(chota+(chota*0.75))<=bda:
            # print("15.5 + krdo avg1 me ,- 7.5 avg2 me")
            plus=15.5
            minus=7.5
        elif(chota+(chota*0.5))<=bda:
            # print("10 add krdo and -5 add krdo")
            plus=10
            minus=5
        elif(chota+(chota*0.25))<=bda:
            plus=5
            minus=0
            # print("+5%,add 0")
        elif(chota+(chota*0.05))<=bda:
            # print("+20 +20")
            plus=20
            minus=-20
        # else:
        #     plus=7.5
        #     minus=3.75
        #     # print("7.5 ,-3.75")
        if (avg1>=avg2):
            f2=int2+plus
            f1=int1-minus
            # print("first person is on lead")
            # print("second person :",f1)
            # print("first person :",f2)
        else:
            f1=int1+plus
            f2=int2-minus
            # print("second person is on lead")
            # print("second person :",f1)
            # print("first person :",f2)
        print(f1,f2)
        f1,f2=viaword(f1,f2,len1,len2)
        return f1,f2



    p1int,p2int=findinginterestviadelay(avg1,avg2,len(str1),len(str2))
    print(p1int)
    print("break")
    print(p2int)
    # print(findinginterestviadelay(20,5,200,100))
    import math
    avg1 = math.trunc(avg1 * 100) / 100
    print(avg1)  # Output: 35.67
    avg2 = math.trunc(avg2 * 100) / 100
    print(avg2)  # Output: 35.67

    # @app.route("/")
    # def runn():
    #     return render_template('frontend.html',count1=count1,count2=count2,
    #                        wholecount=wholecount-1,firstdate=firstdate,
    #                        lastdate=lastdate,kitnedin=kitnedin,avg1=avg1,
    #                        avg2=avg2,name1=name1,name2=name2,filter1dl=filter1dl,
    #                        filter2dl=filter2dl,msgcountperson1=msgcountperson1,
    #                        msgcountperson2=msgcountperson2,interest1=interest1,
    #                        interest2=interest2,p1int=p1int,p2int=p2int,monthc=monthc)

    # Return all computed variables in a dictionary
    result = {
        "count1": count1,
        "count2": count2,
        "wholecount": wholecount - 1,
        "firstdate": firstdate,
        "lastdate": lastdate,
        "kitnedin": kitnedin,
        "avg1": avg1,
        "avg2": avg2,
        "name1": name1,
        "name2": name2,
        "filter1dl": filter1dl,
        "filter2dl": filter2dl,
        "msgcountperson1": msgcountperson1,
        "msgcountperson2": msgcountperson2,
        "interest1": interest1,
        "interest2": interest2,
        "p1int": p1int,
        "p2int": p2int,
        "monthc": monthc
    }
    return result
    
if __name__=="__main__":
    app.run(debug=True)


