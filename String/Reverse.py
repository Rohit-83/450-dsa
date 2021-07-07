#reverse a String using Stack

def reverse_stack(str):
    stack = []
    for i in range(len(str)):
        stack.append(str[i])
    for i in range(len(stack)):
        str[i] = stack.pop()

#iterative using two pointer

def iterative_reverse(str):
    #we have to take two pointer
    i=0
    j=len(str)-1
    while i<j:
        str[i],str[j] = str[j],str[i]
        i+=1
        j-=1
    return str


if __name__ == '__main__':
    str = ['a','b','c','d']
    #reverse_stack(str)
    result = iterative_reverse(str)
    print(''.join(result))
