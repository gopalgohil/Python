# File input/ output
# RAM : Volatile , HDD : Non Volatile

'''
Types of File in python:
 There are Two Types of File:
                             1) Text files(.txt)
                             2) binary files(.jpg,.dat etx)
'''
'''
# open file
f = open("file.txt")
data = f.read()
print(data)
f.close()
# write a file
str = "Good Morning"
f = open("myFile.txt","w")
f.write(str)
print(f)
'''
'''
f = open("file.txt")
lines = f.readline()
print(lines,type(lines))
f.close()
'''
'''
# while loop to print the line
f = open("file.txt")
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
print(line,type(line))
f.close()
'''
'''
str = "harry"
f = open("file.txt","a")
lines = f.write(str)

# with is used to without write close tag to create file
with open("file.txt") as f:
    print(f.read())
'''

# write  a program to find the word in your file
'''
with open("find.txt") as f :
    content = f.read()
    print(content)
    if("gopal" in content):
        print("This word is present in the content")
    else:
        print("This word is not present int content")
'''
'''
def generate(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    with open(f"tables/table{n}","w") as f:
        f.write(table)
for i in range(2,21):
    generate(i)
'''
'''
for n in range(2,15):              
    str = ""
    for i in range(1,11):
        str +=f" {n} X {i} = {n*i}\n"
    
        f = open(f"tables/table{n}","w")
        f.write(str)
        f.close()
    
'''
# replace the jaynit to gopal
'''
con = "jaynit"

with open("file.txt","r") as f:
    read = f.read()
    readNew = read.replace(con,"gopal")
    print(read)
with open("file.txt","w") as f:
   writeNew= f.write(readNew)
'''
'''
lists = ["gopal","jaynit","hemil"]

with open("file.txt","r") as f:
    content=f.read()
  
for list in lists:
    newContent = content.replace(list,"*" * len(list))
with open("file.txt","w") as f:
    f.write(newContent)
'''
'''
word = "hello"
with open("hello.txt","r") as f:
    newRead = f.read()
    print(newRead)
    if(word in newRead):
        print("This world is present")
    else:
        print("This word is not present ")
with open("hello.txt","w") as f:
    f.write(newRead)
'''

# write a program to copy txt one file to another
'''

with open("second.txt","r") as f:
   read= f.read()
   print(read)
with open("third.txt","w") as f:
   f.write(read)
'''
# compare text in file so text is match to second file then print "yess"
'''
with open("second.txt") as f:
   read1= f.read()

with open("third.txt") as f:
    read2= f.read()
if(read1==read2):
    print("yes")
else:
    print("no")
'''