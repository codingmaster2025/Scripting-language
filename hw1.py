#Jinwei Zhou
#Jinwzhou
#114177591

#problem 1
def is_nice(s):
    listS= {}
    for i in range(len(s)):
        listS[s[i]]=1+listS.get(s[i],0)
    
    
    for j in range(len(s)-1):
        if listS[s[j]]!= listS[s[j+1]]:
            return "HARD NO"

    return "HARD YES"

print("Problem 1 test part:")
print(is_nice("aabbcd"))
print(is_nice("abcdefghhgfedcba"))
print(is_nice("abcdefghhgfedecba"))


print("\n")

#problem 2
def is_balanced(s):
    
    stack= []
    for char in s: 
        if (char=="(" or char=="[" or char=="{"):
            stack.append(char)
        else:
            if(not stack):
                return False
            else:
                pop=stack.pop()
                if(char==")" and pop!="("):
                    return False
                if(char=="}" and pop!="{"):
                    return False
                if(char=="]" and pop!="["):
                    return False
    return (len(stack)==0)

print("Problem 2 test part:")
print(is_balanced("{[()]}"))
print(is_balanced("{[(])}"))
print(is_balanced("{{[[(())]]}}"))
print("\n")



#problem 3

def even(x):
     return x % 2 == 0

def apply_fun(a,even):
    return [x for x in range(len(a)) if even(a[x])]
   

print("Problem 3 test part:")

a = [2,3,4,5,6,8]
print(apply_fun(a,even))
print("\n")

#problem 4


class FS_Item():
    def __init__(self,name):
        self.name=name
class Folder(FS_Item):
    def __init__(self,name):
        super().__init__(name)
        self.items=[]
    def add_item(self,item):
        self.items.append(item)

        
class File(FS_Item):
    def __init__(self, name, size):
        super().__init__(name)
        self.size=size


def load_fs(ls_output):
    
    def is_path(line):
        if line[0]== ".":
            return True
        return False
    def is_folder(line):
        if(line[:3]=="drw"):
            return True
        return False
    def is_file(line):
        if (line[:3]=="-rw"):
            return True
        return False
    
    with open(ls_output,'r') as f:
        lines= f.readlines()
        
    dummy=Folder(lines[0][0])
    curr=dummy
    
    Hash={}
    for i in range(1, len(lines)):
        
        line=lines[i]
        if(is_path(line)):
            

            currline=line[:-2]
            
            if currline in Hash:
                curr= Hash[currline]
                #print("check curr:"+str(curr))
                

        if(is_folder(line)):
            list= line.split(" ")
            f=Folder(curr.name+"/"+list[-1][:-1])
            curr.add_item(f)

            s=curr.name+"/"+list[-1][:-1]
            Hash[s]=f
            

        elif(is_file(line)): 
            list= line.split(" ")
            index=3
            while(not list[index].isdigit()):
                index=index+1
            curr.add_item(File(curr.name+"/"+list[-1],list[index]))
            
        else:# other cases
            pass
        

    
    return dummy

print("Problem 4 test part: ")
q=load_fs("lsoutput.txt")
print(q)






#Problem 5
def decode(ct):
    def first_letter(c):
        for i in range(10):
            if ((ord(c)-ord('A'))+i*26-17)>= 65 and (ord(c)-ord('A'))+i*26-17<= 90:
                return chr(ord(c)-ord('A')+i*26-17)
    def first_letter2(c):
        for i in range(10):
            if ((ord(c)-ord('a'))+i*26-17)>= 97 and (ord(c)-ord('A'))+i*26-17<= 122:
                return chr(ord(c)-ord('a')+i*26-17)
    def lower_decoded(pre,c):
        for i in range(10):
            if ((ord(c)-ord('a'))+i*26-ord(pre))>= 97 and (ord(c)-ord('a'))+i*26-ord(pre)<= 122:
                return chr(ord(c)-ord('a')+i*26-ord(pre))
    def upper_decoded(pre,c):
        for i in range(10):
            if ((ord(c)-ord('A'))+i*26-ord(pre))>= 65 and (ord(c)-ord('A'))+i*26-ord(pre)<= 90:
                return chr(ord(c)-ord('A')+i*26-ord(pre))
            
    res=""
    pre_letter=""
    index=0

    # step1
    for i in range(len(ct)):
        if ct[i].isalpha():
            index=i;
            break;
        else: res+=ct[i]

    if(ct[index].isupper()):
        res+=first_letter(ct[index])
        pre_letter=first_letter(ct[index])
 
    else:
        #res+=first_letter(ct[index].upper()).lower()
        #pre_letter=first_letter(ct[index].upper()).lower()
        res+=first_letter2(ct[index])
        pre_letter=first_letter2(ct[index])


    # step2
    for char in ct[index+1:]:
        if char.isalpha():
            
            if(char.isupper()):
                curr=curr.upper()
                curr=upper_decoded(pre_letter,char)
            else:
                curr=lower_decoded(pre_letter,char)
            res+=curr
            pre_letter=curr;
        else:   
            res+=char

    return res


print("Problem 5 test part:")
print(decode("M oy fxhh dnw."))

print(decode("Xgbm mm e fjix"))
print(decode("Gpxsy kuz rw v33q xoefiw."))
print(decode('''"M qcura wthl rrscmc q yyew qsxgthhh drkjh F vtoyat bw qgvlhqnr pmdjrb, rhz ymxd B fhqxftpt R qcura poqsiw xmx scmzvhdt uvut df vdsjhwfuhlcds hvtzmdbp godulyt dn smx scmnbzx cefjbifnji. Gh mtp qrud vmbi lvlh 35000 khuxv sr vs smhbs jmxd, vqnm lxnfi knt rsiv fsxgthlhf, thz usrbnnyv, M rdn's pjnw, i xfnyqb ktcth 35000 khuxv sf dmvpyi, wihluxp, fboko, tmxkc, ezc bsymw qcnrysct. Jy e txqdwqbiw oefifhf eyovbhd, S kie e fjhulvyb vrufrxh." --Wmxgthebt'''))












