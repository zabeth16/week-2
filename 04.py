

def maxProduct(nums):
# 請用你的程式補完這個函式的區塊
    a1 = []
    multiA = 0
    result = 0
    for a in range(len(nums)-1):
        for b in range(a+1,len(nums)):
            multiA = nums[a] * nums[b]
            #print(multiA)

            a1.append(multiA)
            #print(a1)
                        
            result = max(a1)
            

    return print(result)




maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10

