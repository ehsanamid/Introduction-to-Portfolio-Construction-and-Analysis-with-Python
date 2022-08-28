a =13
b = 14
c = 15

def buy_goods(cost, savings):
    if(cost < savings* 0.05):
        return True
    return False
    




print(buy_goods(15, 200))

print(buy_goods(2, 100))

print(buy_goods(35, 1000))
