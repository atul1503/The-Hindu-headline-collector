from selenium import webdriver


def hindu_extractor(source):
    i=0
    story=''
    while i<len(source):
        if source[i:i+15]=='class="paywall"':
            j=i+15
            while '<script' not in source[j:j+14]:
                story=story+source[j]
                j=j+1
            return story
                
        i=i+1
                
def tag_hider(source,hide='a'):
    i=0  
    story=''
    while i<len(source):
        if source[i:i+len(hide)+1]=='<'+hide:
            j=i+len(hide)
            while source[j]!='>':
                j=j+1
                
            j=j+1
            while source[j:j+len(hide)+3]!='</'+hide+'>':
                story=story+source[j]
                j=j+1
                
            i=j+len(hide)+2
        else:
            story=story+source[i]
        i=i+1
    return story
            
        
def para_extractor(source,skip='p'):           
    i=0
    story=''
    while i<len(source):
        if source[i]=='<':
            if source[i:i+len(skip)+2]=='<'+skip+'>':
                j=i+len(skip)+2
                while source[j:j+len(skip)+3]!='</'+skip+'>':
                    story=story+source[j]
                    j=j+1
                i=j+len(skip)+2
                story=story+'\n'
        i=i+1
    return story
    
def block_tag_skipper(source):
    i=0
    if '</' in source:
        while i<len(source):
            if source[i]=='<' and source[i+1]!='/':
                b=source[:i]
                tag='</'
                j=i+1
                while (source[j]!=' ' and source[j]!='>'):
                    tag=tag+source[j]
                    j=j+1
                tag=tag+'>'
                while source[j:j+len(tag)]!=tag:
                    j=j+1
                j=j+len(tag)
                af=source[j:]
                source=b+af
                i=j
            i=i+1
        return block_tag_skipper(source)
    return source    

def get_title(html):
    s=str(html)
    i=0
    t=''
    while i<len(s):
        if s[i:i+3]=='<h1':
            while s[i]!='>':
                i=i+1
            i=i+1
            while s[i:i+2]!='</':
                t=t+s[i]
                i=i+1
            return t
        i=i+1

def surf(site,b,f):
    b.get(site)
    html=b.page_source
    html2=html
    html2=get_title(html)
    html=hindu_extractor(html)
    html=tag_hider(html)
    html=para_extractor(html)
    html=block_tag_skipper(html)
    f.write(' '*40+html2+'\n\n\n'+html+'-'*100+'\n')
    return f,b
    
        
       
def main():
    mainsite='thehindu.com'
    mainsite='https://'+mainsite
    b=webdriver.Chrome()
    b.get(mainsite)
    html=b.page_source
    sites=[]
    i=0
    while i<len(html):
        link=''
        if html[i:i+2]=='<a':
            flag=1
            while html[i:i+6]!='href="':
                i=i+1
            i=i+6
            while html[i]!='"':
                link=link+html[i]
                i=i+1
            j=i
            while html[i:i+15]!='title="Updated:':
                if html[i]=='>':
                    flag=0
                    break
                i=i+1
            if flag:
                sites.append(link)
                
        i=i+1
        
    
    f=open('article.txt','w',encoding='utf-16')
    f.write('-'*15+'THE HINDU'+'-'*15+'\n\n\n'+'-'*60)
    for i in sites:
        try:
            f,b=surf(i,b,f)
        except:
            pass
    f.close()
    b.close()
    print('---------DONE--------------')
                    
                
main()
    
                
                                
