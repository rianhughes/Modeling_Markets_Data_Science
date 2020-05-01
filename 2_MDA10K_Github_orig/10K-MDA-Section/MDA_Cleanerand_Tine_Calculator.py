"""
This program first identifies valid MD&A sections and then computes the tone of these sections.  The final output file will by 
SampleData.txt and it is saved in the file that you designate as filepath3.
"""
import csv
import re
import os

#This is the filepath of the Financial Statement text documents. This must be changed to your respective filepath.
#filepath="F:\\Financial Statements"
filepath="/home/rian/Desktop/1_Work/6_Jobs__Quant_RiskManagmemnt_DS/Modeling_the_Market/1_MDA10K_GitHub/MDA_Data/"
#This is the filepath of the word dictionary files.  This must be changed to your respective filepath.
#filepath2="D:\\Dropbox\\Documents\Data\\SEC FILING DATA\\Current 10K Scrape\\Word Files"
filepath2="/home/rian/Desktop/1_Work/6_Jobs__Quant_RiskManagmemnt_DS/Modeling_the_Market/2_MDA10K_Github_orig/10K-MDA-Section/Word_Dictionaries/"
#This is where you would like the cleaned / identied MD&A section text files to be written.  This file must also include the 
#downloadlog file from the previously run MASTERSCRAPE.py program.
#filepath3="C:\\Users\\rdf0969\\Documents\\Python Scripts\\test"
filepath3="/home/rian/Desktop/1_Work/6_Jobs__Quant_RiskManagmemnt_DS/Modeling_the_Market/1_MDA10K_GitHub/MD-A-10-K-data/output/"

NEGATIVE=os.path.join(filepath2,"NEGATIVE.txt")
POSITIVE=os.path.join(filepath2,"POSITIVE.txt")
SD=os.path.join(filepath3,"SampleData.txt")
download=os.path.join(filepath3,"DOWNLOADLOG.txt")

'''
This section will upload the dictionaries
'''
NEGATIVE=open(NEGATIVE, 'r').readlines()
NEGATIVE=map(str.strip, NEGATIVE)
NEGATIVE=[x.lower() for x in NEGATIVE]
POSITIVE=open(POSITIVE, 'r').readlines()
POSITIVE=map(str.strip, POSITIVE)
POSITIVE=[x.lower() for x in POSITIVE]
'''
DONE
'''

'''
The following are the phrases that must be identified for a particular section to be considered a MD&A section.
'''
sayings=["the following discussion","this discussion and analysis","should be read in conjunction", "should be read together with", "the following managements discussion and analysis"]
acq=["Acquisition","acquisition","merger","Merger","Buyout","buyout"]    
'''
DONE
'''

'''
Beginning of the program
'''
print(download)
with open(download, 'r') as txtfile:
    #reader = csv.reader(txtfile, delimiter=',')
    reader = csv.reader(txtfile, delimiter='\t')
    next(reader, None)
    print(reader)
    for line in reader:
        #print([line[0], line[1]])
        FileNUM=line[0].strip()
        Sections=int(line[1].strip())
        if Sections!=0:
            Filer=os.path.join(filepath,str(FileNUM)+".txt")
            CLEAN=os.path.join(filepath3,str(FileNUM)+".txt")
            SIC=""
            Info=[str(FileNUM)]
            hand=open(Filer)
            for line in hand:    
                line=line.strip()
                if re.findall('^COMPANY NAME:',line):
                    COMNAM=line.replace("COMPANY NAME: ","")
                if re.findall('^CIK:',line):
                    CIK=line.replace("CIK: ","")
                if re.findall('^SIC:',line):
                    SIC=line.replace("SIC: ","")
                if re.findall('^REPORT PERIOD END DATE:',line):
                    REPDATE=line.replace("REPORT PERIOD END DATE: ","")
            Info.append(COMNAM)
            Info.append(CIK)
            if SIC=="":
                SIC='9999'
                Info.append(SIC)
            else:
                Info.append(SIC)
                
            Info.append(REPDATE)
            Info.append(str(Sections))
         
            str1=open(Filer).read()
            locations=[]
            for m in re.finditer("<SECTION>",str1):
                a=m.end()
                locations.append(a)
            for m in re.finditer("</SECTION>",str1):
                a=m.start()
                locations.append(a)
            if locations!=[]:
                locations.sort()
                            
            if Sections==1:
                substring1=str1[locations[0]:locations[1]]
                substring1=substring1.lower()
                substring1=re.sub('\d','',substring1)
                substring1=substring1.replace(',','')
                substring1=substring1.replace(':',' ')
                substring1=substring1.replace('?','')
                substring1=substring1.replace('.','')
                substring1=substring1.replace('$','')
                substring1=substring1.replace('(','')
                substring1=substring1.replace(')','')
                substring1=substring1.replace('%','')
                substring1=substring1.replace('"','')
                substring1=substring1.replace('-',' ')
                substring1=substring1.replace('[','')
                substring1=substring1.replace(';',' ')
                substring1=substring1.replace(']','')
                substring1=substring1.replace('_','')
                substring1=substring1.replace('|','')
                substring1=substring1.replace('/','')
                substring1=substring1.replace('`','')
                substring1=substring1.replace("'",'')
                substring1=substring1.replace('&','')
                substring1=substring1.split()
                TWORD=0
                TWORD=len(substring1)
                Post=[]
                Post.extend(Info)
                Post.append(str(TWORD))
                PLUS=0
                NEG=0
                ACQ=0
                for s in substring1:
                    if s in POSITIVE:
                        PLUS=PLUS+1    
                    if s in NEGATIVE:
                        NEG=NEG+1
                    if s in acq:
                        ACQ=ACQ+1
                Post.append(str(PLUS))
                Post.append(str(NEG))
                Post.append(str(ACQ))
                
                with open(CLEAN,'a') as f:
                    f.write("<SECTION>\n")
                    f.write(' '.join(substring1)+"\n")
                    f.write("</SECTION>\n")
                    f.close()
                with open(SD,'a') as f:
                    f.write(','.join(Post)+'\n')
                    f.close    
                print Post
                print [PLUS, NEG, float (PLUS-NEG)/(PLUS+NEG)]
                Post=[]
            else:
                for k in range(0,len(locations),2):
                    filed=0
                    substring1=str1[locations[0+k]:locations[1+k]]
                    substring1=substring1.lower()
                    substring1=substring1.split(". ")
                    if len(substring1)>5:
                        for j in range(0,6):
                            if any(s in substring1[j] for s in sayings):
                                filed=1
                                break
                    if filed==1:
                        substring1=str1[locations[0+k]:locations[1+k]]
                        substring1=substring1.lower()
                        substring1=re.sub('\d','',substring1)
                        substring1=substring1.replace(',','')
                        substring1=substring1.replace(':',' ')
                        substring1=substring1.replace('?','')
                        substring1=substring1.replace('.','')
                        substring1=substring1.replace('$','')
                        substring1=substring1.replace('(','')
                        substring1=substring1.replace(')','')
                        substring1=substring1.replace('%','')
                        substring1=substring1.replace('"','')
                        substring1=substring1.replace('-',' ')
                        substring1=substring1.replace('[','')
                        substring1=substring1.replace(';',' ')
                        substring1=substring1.replace(']','')
                        substring1=substring1.replace('_','')
                        substring1=substring1.replace('|','')
                        substring1=substring1.replace('/','')
                        substring1=substring1.replace('`','')
                        substring1=substring1.replace("'",'')
                        substring1=substring1.replace('&','')
                        substring1=substring1.split()
                        TWORD=0
                        TWORD=len(substring1)
                        Post=[]
                        Post.extend(Info)
                        Post.append(str(TWORD))
                        PLUS=0
                        NEG=0
                        ACQ=0
                        for s in substring1:
                            if s in POSITIVE:
                                PLUS=PLUS+1
                            if s in NEGATIVE:
                                NEG=NEG+1
                            if s in acq:
                                ACQ=ACQ+1
                        Post.append(str(PLUS))
                        Post.append(str(NEG))
                        Post.append(str(ACQ))
                        
                        with open(CLEAN,'a') as f:
                            f.write("<SECTION>\n")
                            f.write(' '.join(substring1)+"\n")
                            f.write("</SECTION>\n")
                            f.close()
                        with open(SD,'a') as f:
                            f.write(','.join(Post)+'\n')
                            f.close   
                        print Post
                        Post=[]
