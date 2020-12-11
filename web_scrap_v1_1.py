from selenium import webdriver

def tag_finder_by_string(s,tag,id="I dont' know"):

    '''
        This function extracts the contents of the tag that contains id string in its attribute from the s string.
        s is a string which represents html source.
        Here, s is the source html.
        tag is the name of the tag,for eg, 'p' , 'div'.
        id is the attribute or property identifier string like 'title="Updated:'.
        for eg:
        s='atul<div id="this">Say Something.</div>Hidden'
        print(tag_finder_by_string(s,'div','id="this"')
        output is:  'Say Something.'
    '''
    
    i=0
    s=escape(s)
    content=''
    while i<len(s):
        if id!="I dont' know":
            if s[i:i+len(tag)+1]=='<'+tag:
                isCorrectTag=1
                while s[i:i+len(id)]!=id:
                    if s[i]=='>':
                        isCorrectTag=0
                        break
                    i=i+1
                
                if isCorrectTag:
                    count=0
                    while s[i]!='>':
                        i=i+1
                    i=i+1
                    while s[i:i+len(tag)+3]!='</'+tag+'>' or  count!=0:
                        if s[i:i+len(tag)+1]=='<'+tag:
                            count=count+1
                        elif s[i:i+len(tag)+3]=='</'+tag+'>':
                            count=count-1
                        content=content+s[i]
                        i=i+1
                    return content
        else:
            if s[i:i+len(tag)+1]=='<'+tag:
                count=0
                while s[i]!='>':
                    i=i+1
                i=i+1
                while s[i:i+len(tag)+3]!='</'+tag+'>' or  count!=0:
                    if s[i:i+len(tag)+1]=='<'+tag:
                        count=count+1
                    elif s[i:i+len(tag)+3]=='</'+tag+'>':
                        count=count-1
                    content=content+s[i]
                    i=i+1
                return content
        i=i+1
        
        
def hard_cleanify(s):
    '''
        s is a string which represents html source.
        For eg: s=cleanify('atul<br>tripathi')
        now s is 'atultripathi'
        For eg: s=hard_cleanify('atul<img fix>Gigantico</img> Tripathi')
        now s is 'atul Tripathi'
    '''
    
    i=0
    s=escape(s)
    content=''
    if '</' in s:
        while s[i]!='<':
            content=content+s[i]
            i=i+1
        while s[i:i+2]!='</':
            i=i+1
        while s[i]!='>':
            i=i+1
        content=content+s[i+1:]
        return cleanify(content)
    elif ('<' and '>') in s:
        while s[i]!='<':
            content=content+s[i]
            i=i+1
        while s[i]!='>':
            i=i+1
        content=content+s[i+1:]
        return cleanify(content)
    else:
        return s
        
        
def tag_finder_by_num(s,tag,tag_number):
    '''
        s is a string which represents html source.
        extracts the contents of tag which appears in the tag_number'th location in the web page.
        here tag_number is a list.
        For eg.
        s='atul<div> this is div </div><div>Put</div><img wuiici>Ignore</img>'
        s=tag_finder_by_num(s,'div',[2])
        print(s)
        output is='Put'
    
    '''
    i=0
    s=escape(s)
    count=0
    content=''
    while i<len(s):
        if s[i:i+len(tag)+1]=='<'+tag:
            count=count+1
            if count in tag_number:
                content=content+tag_finder_by_string(s[i:],tag)
        
        i=i+1
    return content
        
        
        
def visit(site):
    '''
    visits website in site via chrome webdriver and returns its html source.site is a string.No need to put http or https in site
    '''
    
    b=webdriver.Chrome()
    b.get('https://'+site)
    return b.page_source,b
    
    

    


def soft_cleanify(s,gfn):
    '''
        returns a string which is free from tag names,present in gfn parameter.
        s is the source string.
        gfn is a string which contains tag names like '<div>' or '<img>' or '<p>'.For eg- '<div>,<img>'
        For eg.
        s='atul<img>hi how are you?</img>tripathi'
        print(soft_cleanify(s,'<img>'))
        the output will be-   'atultripathi'
    '''
    i=0
    s=escape(s)
    content=''
    while i<len(s):
        if s[i]=='<':
            j=int(i)
            tag=''
            ignoreFlag=0
            isInline=0
            j=j+1
            while s[j]!='>' and s[j]!=' ':
                tag=tag+s[j]
                j=j+1
                
            if '<'+tag+'>' in gfn:
                ignoreFlag=1
                
            if '</'+tag not in s[j:]:
                isInline=1
                if s[j]==' ':
                    while s[j]!='>':
                        j=j+1
                if ignoreFlag==0:
                    content=content+s[i:j+1]
                i=j
                
                
            
            if isInline==0:
                count=0
                while s[j:j+len(tag)+3]!='</'+tag+'>' or  count!=0:
                    if s[j:j+len(tag)+1]=='<'+tag:
                        count=count+1
                    elif s[j:j+len(tag)+3]=='</'+tag+'>':
                        count=count-1
                    j=j+1
            
                j=j+len(tag)+3
                if ignoreFlag==0:
                    content=content+s[i:j]
                
                i=j-1    
                
        else:
            content=content+s[i]
            
            
        i=i+1
    return content
    

    
def extract_all_tags(s):
    '''
    
    Extracts all contents of all tags in s string.


    '''
    i=0
    s=escape(s)
    content=''
    while i<len(s):
        if s[i]=='<':
            j=int(i+1)
            isInline=0
            tag=''
            while s[j]!='>' and s[j]!=' ':
                tag=tag+s[j]
                j=j+1
                
            if '</'+tag not in s[j:]:
                isInline=1
                
                
            if s[j]==' ':
                while s[j]!='>':
                    j=j+1
            
            if isInline==0:
                j=j+1
                count=0
                while s[j:j+len(tag)+3]!='</'+tag+'>' or count!=0:
                    if s[j:j+len(tag)+1]=='<'+tag:
                        count=count+1
                    elif s[j:j+len(tag)+3]=='</'+tag+'>':
                        count=count-1
                
                    content=content+s[j]
                    j=j+1
                
                i=j+len(tag)+2
                
            else:
                i=j
            
            
        else:
            content=content+s[i]
            
            
            
        i=i+1
        
    return content
            
            
def escape(s):
    '''
    Removes all the < or > in the attribute names of all tags.
    Quite necessary this.
    '''
    i=0
    content=''
    while i<len(s):
        if s[i]=='"':
            content=content+s[i]
            i=i+1
            while s[i]!='"':
                if s[i]!='>' and s[i]!='<':
                    content=content+s[i]
                i=i+1
            content=content+s[i]
                
        else:
            content=content+s[i]
        
        i=i+1
        
    return content