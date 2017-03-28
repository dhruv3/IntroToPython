def catchTraders(input):
    illegaltradeMap = set()
    tradeMap = dict()
    current_price = 0
    for line in input:
        arr = line.split("|")
        day = int(arr[0])
        if len(arr) != 2:
            if day not in tradeMap:
                tradeMap[day] = []
            trader_name = arr[1]
            buy = len(arr[2]) == 3
            amt = int(arr[3])            
            tradeMap[day].append((trader_name, buy, current_price, amt))
			
        else:
            current_price = int(arr[1])
            for x in range(day - 3, day):
                if x in tradeMap:
                    for (trader_name, buy, price, amt) in tradeMap[x]:
                        if (x, trader_name) in illegaltradeMap:
                            continue
                        if buy:
                            flag = (current_price - price) * amt >= 5000000
                        else:
                            flag = (price - current_price) * amt >= 5000000
                        if flag:
                            illegaltradeMap.add((x, trader_name))
    illegaltradeMap = sorted(list(illegaltradeMap))
    return list(map(lambda x: str(x[0]) + "|" + str(x[1]), illegaltradeMap))
 
 
#Testing
 
line1 = """0|1000
0|Shilpa|BUY|30000
0|Will|BUY|50000
0|Tom|BUY|40000
0|Kristi|BUY|15000
1|Kristi|BUY|11000
1|Tom|BUY|1000
1|Will|BUY|19000
1|Shilpa|BUY|25000
2|1500
2|Will|SELL|7000
2|Shilpa|SELL|8000
2|Kristi|SELL|6000
2|Tom|SELL|9000
3|500
38|1000
78|Shilpa|BUY|30000
79|Kristi|BUY|60000
80|1100
81|1200"""
 
input1 = line1.split("\n")
 
out1 = catchTraders(input1)

for res_cur in out1:
    print( str(res_cur))
 
line2 = """0|20
0|Kristi|SELL|3000
0|Will|BUY|5000
0|Tom|BUY|50000
0|Shilpa|BUY|1500
1|Tom|BUY|1500000
3|25
5|Shilpa|SELL|1500
8|Kristi|SELL|600000
9|Shilpa|BUY|500
10|15
11|5
14|Will|BUY|100000
15|Will|BUY|100000
16|Will|BUY|100000
17|25"""
 
input2 = line2.split("\n")
 
catchTraders(input2)
