#先把題目放這
#完成以下函式，正確計算出非 manager 的員工平均薪資，所謂非 manager 
#就是在資料中manager 欄位標註為 False (Python) 或 false (JavaScript) 的員工，
#程式需考慮員工資料數量不定的情況。

#avg是一個set
#employees對應了4個列表
#列表中，有字典，3個key-value


def avg(data):

# 請用你的程式補完這個函式的區塊
    count = 0
    total = 0
    # 測試抓資料印出結果用
    # print(data["employees"][1]["manager"])
    for i in range(len(data["employees"])):
        count += 1
        if  data["employees"][i]["manager"] == True:
            count -= 1
                        
    total = total + data["employees"][i]["salary"]


    print(total)




    




avg({
    "employees":[
        {
        "name":"John",
        "salary":30000,
        "manager":False
        },
        {
        "name":"Bob",
        "salary":60000,
        "manager":True
        },
        {
        "name":"Jenny",
        "salary":50000,
        "manager":False
        },
        {
        "name":"Tony",
        "salary":40000,
        "manager":False
        }
    ]
}) # 呼叫 avg 函式

