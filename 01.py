
def calculate(min,max,step):

    result = 0
    for i in range(min,max+1,step):
        result = result + i
    print(result)



calculate(1,3,1)
calculate(4,8,2)
calculate(-1,2,2)
