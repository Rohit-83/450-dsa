#Write a code to check whether a string is a rotation of another

def is_rotation(str1,new_str):
    temp = str1+str1
    if new_str in temp:
        return True
    else:
        return False

if __name__ == '__main__':
    str1 = 'abcd'
    new_str = 'acbd'
    print(is_rotation(str1,new_str))