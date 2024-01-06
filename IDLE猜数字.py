import random
key = str(random.randint(1,3))
if input("猜一猜1-3:")==key:
    print("你赢了!")
else:
    print("你输了,我想的是"+ key)
