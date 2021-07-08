
def dup_char(str):
    #we use a dictionary to store the str
    dict = {}
    for i in range(len(str)):
        if str[i] in dict:
            dict[str[i]]+=1
        else:
            dict[str[i]]=1
    for key,value in dict.items():
        if value>1:
            print(key,end="")

if __name__ == '__main__':
    str ='sfgweafdfbegt'
    str.split()
    dup_char(str)