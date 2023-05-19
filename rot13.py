#ROT13 encryption
#Declaration part
char='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str_in=''
str_out=''
str_len=0
i=0

print("Welcome to ROT13 encryption!")
print("Type as many lines you want and type :q to end")

#Function for getting input
def get_input():
    global i,str_in,str_out,str_len
    while True:
        i+=1
        print(f"Enter line{i}")
        a=input()
        if ':q' in a:
            break
        str_in+=a+'\n'
    str_len=len(str_in)
    encrypt()

#function for encrypting by ROT13
def encrypt():
    global str_in,str_out,str_len
    for i in range(str_len):
        a=str_in[i]
        if a=='?' or a=='<' or a=='>' or a=='\n' or a==' ' or a=='.' or a==',' or a=='\t' or a=="\"" or a=="\'" or a==':' or a==';' or a=='!' or a=='&' or a=='%' or a=='$' or a=='@' or a=='#':
            str_out+=a
            continue
        loc=char.find(a.upper())
        new_loc=(loc+13)%26 #We're using modulus so that the range stays between 26
        str_out+=char[new_loc]

#function for writing to a file
def filer():
    global str_out
    f=open("output.txt",'w+')
    try:
        f.writelines(str_out.lower())
    except:
        print("Writing failed!")
    else:
        print("The encrypted message is written to output.txt")
    f.close()
get_input()
filer()

