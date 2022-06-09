# AVG_pro

price = int(input("price: "))
cash1 = int(input("cash1: "))
y = int(input("y: ")) # drop percentage
# first buy:
print("="*20)
buy1 = cash1/price
print(f"pieces: {buy1}")
print("="*20)


# 
# print(sum(avg_list))


# support_levels
x = price
x1 = (x-(x*y/100))
x2 = (x1-(x1*y/100))
x3 = (x2-(x2*y/100))
x4 = (x3-(x3*y/100))
x5 = (x4-(x4*y/100))
x6 = (x5-(x5*y/100))
x7 = (x6-(x6*y/100))
x8 = (x7-(x7*y/100))
x9 = (x8-(x8*y/100))
x10 = (x9-(x9*y/100))
# ===========
# avg_list = []
# avg_list.append(x)


print("support levels:")
print(f"level_1 : {x1}")
print(f"level_2 : {x2}")
print(f"level_3 : {x3}")
print(f"level_4 : {x4}")
print(f"level_5 : {x5}")
print(f"level_6 : {x6}")
print(f"level_7 : {x7}")
print(f"level_8 : {x8}")
print(f"level_9 : {x9}")
print(f"level_10 : {x10}")

# ==========================
# second buy
ask1 = input("if you want another buying write 2: ")
if int(ask1) == 2 :
    cash2 = int(input("cash2: "))
    print("="*20)
    buy2 = cash2/x1
    print(f"pieces: {buy2}")

    # avg_list.append(x1)
    # average = sum(avg_list) / len(avg_list)
    # print(f"average is: {average}==")

    avg1 = (x+x1)/2
    print(f"average is: {avg1}")
    print("="*20)
# third buy
ask2 = input("if you want another buying write 3: ")
if int(ask2) == 3 :
    cash3 = int(input("cash3: "))
    print("="*20)
    buy3 = cash3/x2
    print(f"pieces: {buy3}")

    # avg_list.append(x2)
    # average = sum(avg_list) / len(avg_list)
    # print(f"average is: {average}==")

    avg2 = (x+x1+x2)/3
    print(f"average is: {avg2}")
    print("="*20)

# fourth buy
ask3 = input("if you want another buying write 4: ")
if int(ask3) == 4 :
    cash4 = int(input("cash4: "))
    print("="*20)
    buy4 = cash4/x3
    print(f"pieces: {buy4}")

    # avg_list.append(buy4)
    # average = sum(avg_list) / len(avg_list)
    # print(f"average is: {average}==")

    avg3 = (x+x1+x2+x3)/4
    print(f"average is: {avg3}")
    print("="*20)
# fifth buy
ask4 = input("if you want another buying write 5: ")
if int(ask4) == 5 :
    cash5 = int(input("cash5: "))
    print("="*20)
    buy5 = cash5/x4
    print(f"pieces: {buy5}")

    # avg_list.append(buy5)
    # average = sum(avg_list) / len(avg_list)
    # print(f"average is: {average}==")

    avg4 = (x+x1+x2+x3)/5
    print(f"average is: {avg4}")
    print("="*20)
# sixth buy
ask5 = input("if you want another buying write 6: ")
if int(ask5) == 6 :
    cash6 = int(input("cash6: "))
    print("="*20)
    buy6 = cash6/x5
    print(f"pieces: {buy6}")

    # avg_list.append(buy6)
    # average = sum(avg_list) / len(avg_list)
    # print(f"average is: {average}==")

    avg5 = (x+x1+x2+x3+x4+x5)/4
    print(f"average is: {avg5}")
    print("="*20)










