def tag_content_extractor(s,tag,id="I dont' know"):
    '''Here, s is the source html.
        tag is the name of the tag,for eg, 'p' , 'div'.
        id is the attribute or property identifier string like 'title="Updated:'.
    '''
    
    i=0
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
        
        
def cleanify(s):
    '''
        For eg: s=cleanify('atul<br>tripathi')
        now s is 'atultripathi'
    '''
    
    i=0
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
        
        