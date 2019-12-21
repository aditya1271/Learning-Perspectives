from googlesearch import search
import requests
import re
import csv
data=[]
a=[]
student="Manan"
def swap(text,j):
    temp1=text[j]
    temp2=text[j+1]
    temp3=text[j+2]
    temp4=text[j+3]
    text[j]=text[j+4]
    text[j+1]=text[j+5]
    text[j+2]=text[j+6]
    text[j+3]=text[j+7]
    text[j+4]=temp1
    text[j+5]=temp2
    text[j+6]=temp3
    text[j+7]=temp4

def sort_urls(data):
    newdata=[]
    for word,text in zip(a,data):
        text=text.split()      
        i=0
        
        while(i<len(text)-4):
            j=0
            while(j<len(text)-5):
                if(  int(text[j+1])<int(text[j+5])  ):
                    swap(text,j)
                elif(int(text[j+1])==int(text[j+5])):
                    if( min(int(text[j+3]), min(int(text[j+1]),int(text[j+2]))) < min(int(text[j+7]), min(int(text[j+6]),int(text[j+5]))  )):
                        swap(text,j)
                    elif(  int(text[j+3])==0 or int(text[j+1])==0 or int(text[j+2])==0 and (int(text[j+7])!=0 and int(text[j+6]) !=0 and int(text[j+5])!=0 )  ):
                        swap(text,j)
                    elif(  int(text[j+3]) + int(text[j+1]) + int(text[j+2]) < int(text[j+7]) + int(text[j+6]) + int(text[j+5])!=0   ):
                        swap(text,j)
                j=j+4
            i=i+4
        strtemp=""
        i=0
        while(i<len(text)-4):
            strtemp+=text[i]+"\n"+text[i+1]+" "+text[i+2]+"  "+text[i+3]+"\n"
            i=i+4
        strtemp=strtemp+"-1\n"
        newdata.append(strtemp)
    #for x in newdata:
     #   print (x)
    return newdata

def read_from_file():

    try:
        fin = open("Experiment2/urlw8"+student+".txt")
    except :
        return 0
    query=fin.readline()
    strtemp=""
    query=query.replace("\n","")
    var=query
    while(query):
        while(query and query!="-1"):
            query=fin.readline()
            strtemp+=query
            query=query.replace("\n","")
        query=fin.readline()
        query=query.replace("\n","")
        if(query):
            a.append(var)
            data.append(strtemp)
            strtemp=""
            var=query
            
     
    fin.close()
    
    
    return 1

read_from_file()
data=sort_urls(data)
open("Experiment2/urlw8"+student+".txt","w").close()
fout= open("Experiment2/urlw8"+student+".txt","w")
list_1=[]
for x,y in zip(a,data):
    fout.write(x+"\n")
    fout.write(y)
    #----------------------------------
    temp12=y
    temp12=temp12.splitlines()
    i=0
    while( i < len(temp12)-1):
        templist=[]
        if ( temp12[i]=="-1" or temp12[i+1]=="-1" ) :
            i=i+2
    
        else:
            templist.append(x)
            templist.append(temp12[i])
            w8=temp12[i+1].split()
            templist.append(w8[0])
            templist.append(w8[1])
            templist.append(w8[2])
            #print(templist)
            list_1.append(templist)
            i=i+2
        #print("\n")

#-------------------------------------------------------------------
header = ['Label', 'URL', ' Label Weight', 'Esemble Weight','ML Weight']
with open('Experiment2/'+student+'.csv', 'wt') as f:
    csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)

    csv_writer.writerow(header) # write header

    csv_writer.writerows(list_1)

    

fin1 = open("Experiment2/Results(Mam).txt","r")
fin2 = open("Experiment2/Results("+student+").txt","r")
    
set1=fin1.readline()
set2=fin2.readline()
set1=set1.split(" ,")
set2=set2.split(" ,")
words=list(set(set1)-set(set2))

#word1=word1.replace("\n","")
i=0
#print(a)
while(i<len(words)) :
    word1=words[i]
    i=i+1
    if word1 not in a:
        regex1='\W'+word1+'\W'
        regex2='\Wensemble\W'
        regex3='\Wmachine learning\W'
        
        query='"'+word1+'" + "ensemble" + "machine learning" '
        fout.write(word1+"\n")
        print(word1)
        for url in search(query, tld='com', stop=10):
            if(url.find(".pdf",len(url)-5)==-1):
                test=1
                try:
                    page=requests.get(url).text
                except :
                    test=0
                if test!=0 :
                    print(url)
                    fout.write(url)
                    fout.write("\n")    
                    fout.write(str(len(re.findall(regex1, page ,  re.IGNORECASE) ) )  )
                    fout.write(" ")    
                    fout.write(str(len(re.findall(regex2, page ,  re.IGNORECASE) ) )  )
                    fout.write(" ")    
                    fout.write(str(len(re.findall(regex3, page ,  re.IGNORECASE) ) )  )
                    fout.write("\n")
        fout.write("-1\n")
fout.write("-2\n")


