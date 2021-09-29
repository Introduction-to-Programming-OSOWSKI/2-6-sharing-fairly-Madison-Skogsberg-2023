#WRITE YOUR CODE IN THIS FILE
#define function
#add parameters
def shareFair(x, y):
    if x % y == 0:
        return True
    else:
        return False
#run function
print(shareFair(10,6))