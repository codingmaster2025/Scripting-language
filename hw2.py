import re


#p1
def highlight(pattern, string):
    pattern= re.compile(pattern)
    match =pattern.search(string)
    if match == None:
        return None
    return re.sub(pattern,"<"+match.group(0)+">",string)



print("test part for p1:")
print(highlight(r'[a-zA-Z]\d',"ShepardN7"))

strings = ["bookstore", "booking","textbooks","audiobook"]
pattern = r'\bbook\B'

for s in strings:
    print(highlight(pattern,s))


print("...\n")



#p2
def highlight_all(pattern, string):
    pattern= re.compile(pattern)
    if pattern.search(string)==None:
        return None
    
    matchs =pattern.finditer(string)
    

    res=""
    curr_index=0
    
    for match in matchs:
        res+=string[curr_index: match.start()]+"<"+match.group()+">"
        curr_index=match.end()
    res+=string[curr_index:]

    return res

print("test part for p2:")
pattern = r'o\w+'
string = "I'm Commander Shepard and this is my favorite store on the Citadel."

print(highlight_all(pattern, string))
print("...\n")


#p3
def ruin_a_webpage(filename):
    pattern= re.compile(r'.*\.(html|htm)$')

    if pattern.search(filename) == None:
        return None

    with open(filename,'r') as f:
        content= f.read()

    out_f=open("ruined.html",'w')
    
    pat_content=re.compile(r'<p>((.|\s)*?)</p>')
    pat_span=re.compile(r'<span>((.|\s)*?)</span>')

    matches=pat_content.finditer(content)

    res=""
    curr_index=0
    for match in matches:
        res+=content[curr_index: match.start()]+ match.group(1)+ "<br><br>"
        curr_index=match.end()
    res+=content[curr_index:]

    match= pat_span.search(res)

    while match is not None:
        res= re.sub(pat_span, match.group(1),res, 1)
        match=pat_span.search(res)

    
    out_f.write(res)
    out_f.close()

    return True

print("test part for p3:")
print(ruin_a_webpage("sample.html"))
print("...\n")



#p4
def decompose_path(path):
    pattern=re.compile(r':')
    
    if pattern.search(path)==None:
        return []

    matchs = pattern.finditer(path)
    list=[]
    curr_index=0
    for match in matchs:
        list.append(path[curr_index:match.start()])
        curr_index=match.end()
    list.append(path[curr_index:])

    if(list[0]==""):
        list.remove(list[0])
    if(list[len(list)-1]==""):
        list.remove(list[len(list)-1])
    
    return list

print("test part for p4:")
path =":/usr/openwin/bin:/usr/ucb:/usr/bin:/bin:/etc:/usr/local/bin:/usr/local/lib:/usr/shareware/bin:/usr/shareware/lib:"
print(decompose_path(path))
print("...\n")


#p5

def link_mapper(filename):
    pattern= re.compile(r'.*\.(html|htm)$')

    if pattern.search(filename) == None:
        return None
    list=[]
    Hash={filename:list}

    anchor=re.compile(r'<a href="([\w\W]*?)">(.*?)</a>')
    with open(filename, 'r') as f:
        content=f.read()
    
    matchs=anchor.finditer(content)
    
    for match in matchs:
        tuple=(match.group(2),match.group(1))
        list.append(tuple)
        

    return Hash

    

print("test part for p5:")
print(link_mapper("example.htm"))
print("...\n")


#p6



def grammarly(text):
    rule1=re.compile(r'\b(i)\b')
    rule2=re.compile(r'^[a-z]')
    rule3=re.compile(r'a(\s[aeiouAEIOU])')
    rule4=re.compile(r'(\b\w+\b)\s+\1',re.I)
    rule5=re.compile(r'(.*,.+?)\sand\s')
    
                    
    res=""


    prev=False
    index=0
    for char in text: 
        
        #
        if prev==False and char==")":
            index=0
            pass
        
        #(
        elif prev==True and char==")":
            res+=char
            prev=False
            index=0
        #(
        elif prev==True and char== "(":
            res=res[:index]+res[index+1:]
            index=len(res)-1
            res+=char
            
            
        #
        elif prev== False and char =="(":
            prev=True
            res+=char
            index=len(res)-1
            
        else:
            res+=char
    

    if prev==True:

        res=res[:index]+res[index+1:]
        

    sentences= res.split(". ")
    
    res=""

    for sentence in sentences:
        #1."i" instead of "I"
        match=rule1.search(sentence)
        while match is not None:
            sentence=re.sub(rule1, match.group(1).upper(),sentence)
            match=rule1.search(sentence)
            
        #2.Uncapitalized beginning of a sentence.    
        match= rule2.search(sentence)
        while match is not None:
            sentence=re.sub(rule2, match.group(0).upper(),sentence)
            match=rule2.search(sentence)
            
        #3.Using "a" when you should use "an"
        match= rule3.search(sentence)
        while match is not None:
            sentence=re.sub(rule3, "an"+ match.group(1), sentence)
            match=rule3.search(sentence)
            
        #4.Repeated word
        match= rule4.search(sentence)
        while match is not None:
            sentence=re.sub(rule4, match.group(1), sentence)
            match=rule3.search(sentence)
        
        #5.Missing Oxford Comma
        match= rule5.search(sentence)
        while match is not None:
            sentence=re.sub(rule5, match.group(1)+",", sentence)
            match=rule5.search(sentence)
        res+=sentence+". "
        

     
    res=res[:-2]
        
    return res
    

print("test part for p6:")
print(grammarly("apple ApplE"))
print(grammarly("This string contains a enormous number of mistakes mistakes. how anyone (could make more mistakes) in a string than i have, I don't know.  (It contains bad capitalization, unbalanced parentheses and repeated words."))





