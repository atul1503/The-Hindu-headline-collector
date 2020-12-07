from selenium import webdriver
import time



def parser(s):
    if '</' in s:
        j=0
        while s[j:j+2]!='</':
            j=j+1
        while s[j]!='>':
            j=j+1
        return parser(s[j+2:])
    return s
            
        
        
        
        
        

w=webdriver.Chrome()
w.get('https://www.thehindu.com/')
time.sleep(3)
html=w.page_source
w.close()
headlines=[]
i=0
while i<len(html):
	if html[i:i+15]=='title="Updated:':
		j=i+15
		while html[j]!='>':
			j=j+1
			
		k=j+1
		news=''
		while html[k:k+4]!='</a>':
			news=news+html[k]
			k=k+1
		headlines.append(news)
	i=i+1
	
    
for i in range(len(headlines)):
    headlines[i]=parser(headlines[i])
    headlines[i]=headlines[i].strip().strip('"')
        
f=open('the_hindu_headlines.txt','w',encoding='utf-16')
line=1
for i in headlines:
    f.write(str(line)+'. '+i+'.\n')
    line=line+1
f.close()
print('-----------------')
print('Done!!!')
	