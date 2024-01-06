#本程序从500人的队伍里随机挑出，如果满意就入选，不满意就归队
import random
volunteer = 500
while True:
    if volunteer <= 500-10:
        print('您已经选够10个人!')
        exit()
    test = random.randint(1,volunteer)
    if(input('还剩下' + str(volunteer) + '人,这是随机挑选的第' + str(test) + '号,您满意吗（y/n)?') == 'y':
        volunteer -= 1 #入选后队伍就会少1人     
