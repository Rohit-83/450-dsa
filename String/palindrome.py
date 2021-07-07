#simple approach we check if its reverse is equal to original str then it is palindrome

#two pointer approach
def palindrome_check(str):
    i = 0
    j = len(str)-1
    while i<j:
        if str[i]!=str[j]:
            return False
        i+=1
        j-=1
    return True

#recursive approach
def palin_checker(str):
    if len(str)==0 or len(str)==1:
        return True
    n = len(str)
    if str[0]==str[n-1]:
        return palin_checker(str[1:n-1])
    else:
        return False

if __name__ == '__main__':
    str = ['n','a','a','n']
    print(palindrome_check(str))
    print(palin_checker(str))
