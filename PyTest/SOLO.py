#第一步：定义变量
#第二部：双方选择人物
#第三步：进入对战
#第四部：战斗结束，打印对战结果

import random
import time

name_player1 = name_player2 = ""      #玩家1和玩家2的名称
hp_player1 = hp_player2 = 100         #两个2玩家的血量
mp_player1 = mp_player2 = 50          #两个玩家的蓝量
attack_player1 = attack_player2 = 0   #两个玩家的攻击力,后面每轮对战随机生成
choice = ""                           #玩家对菜单的选择
#菜单
print("欢迎进入LOLsolo自走棋".center(46,"*"))    #两种方法打印菜单效果一样
print("{:*^46}".format("欢迎进入LOLsolo自走棋"))
print("\t\t请选择您的角色：1-青钢影\t2-放逐之刃")
choice = input("\t\t请输入您的选择(1-2之间的数字):") #此处虽然输入的是数字但是程序认为是字符串
#此处没有进行验证，判断方法为：如果输入的不是1，默认为2
if choice == "1":
    name_player1,name_player2 = "青钢影","放逐之刃"
else :
    name_player2,name_player1 = "青钢影","放逐之刃"
print("\t\t{}  vs  {}".format(name_player1,name_player2))

#技能系统
skill1 = "精准礼仪"  #施放技能后的第一次攻击伤害+3，第二次攻击伤害+8
skill2 = "折翼之舞"  #施放技能后的三下攻击每次+3
i = 0

#开始对战
while hp_player1 > 0 and hp_player2 > 0:  #两个玩家有一个血量小于0跳出循环
    i +=1
    print("\n")
    print("第{}回合".format(i).center(40,"-"))
    print("\n")
    num_rand = random.randint(0,9)       #每次攻击前随机判断谁先攻击
    if num_rand % 2 == 1:                 #奇数，玩家1先攻击
        attack_player1 = random.randint(5,15) #玩家1随机产生伤害
        skill1_rand = random.randint(1,10)   #判断是否施放技能
        if skill1_rand < 8:                 #释放 则加伤害
            attack_player1 +=8 
            hp_player2 -= attack_player1
            print("\t  {}使用了{}".format(name_player1,skill1))
            print("\t  {}被攻击，掉了{}血!!".format(name_player2,attack_player1))
            print("{}------------------------------{}".format(name_player1,name_player2))
            print("{}Hp{}                              {}Hp{}".format(hp_player1,mp_player1,hp_player2,mp_player2))
        else:                              #不释放 则普通攻击
            hp_player2 -= attack_player1
            print("\t  {}被攻击，掉了{}血!!".format(name_player2,attack_player1))
            print("{}------------------------------{}".format(name_player1,name_player2))
            print("{}Hp{}                              {}Hp{}".format(hp_player1,mp_player1,hp_player2,mp_player2))
        #time.sleep(0.2)
        
        attack_player2 = random.randint(5,15)  #玩家2后攻击
        skill2_rand = random.randint(1,10)      #玩家2判断技能
        if skill2_rand < 7:                       
            attack_player2 +=10                 #释放加伤害
            hp_player1 -= attack_player2
            print("\t  {}使用了{}".format(name_player2,skill2))
            print("\t  {}被攻击，掉了{}血!!".format(name_player1,attack_player2))
            print("{}------------------------------{}".format(name_player1,name_player2))
            print("{}Hp{}                              {}Hp{}".format(hp_player1,mp_player1,hp_player2,mp_player2))
        else:                                    #不释放则普通攻击
            hp_player1 -= attack_player2
            print("\t  {}被攻击，掉了{}血!!".format(name_player1,attack_player2))
            print("{}------------------------------{}".format(name_player1,name_player2))
            print("{}Hp{}                              {}Hp{}".format(hp_player1,mp_player1,hp_player2,mp_player2))
        time.sleep(0.2)
    else:                                  #玩家2先攻击
        attack_player2 = random.randint(5,15)
        skill2_rand = random.randint(1,10)
        if skill2_rand < 7:                 #玩家2施放技能
            attack_player2 +=10 
            hp_player1 -= attack_player2
            print("\t  {}使用了{}".format(name_player2,skill2))
            print("\t  {}被攻击，掉了{}血!!".format(name_player1,attack_player2))
            print("{}------------------------------{}".format(name_player1,name_player2))
            print("{}Hp{}                              {}Hp{}".format(hp_player1,mp_player1,hp_player2,mp_player2))
        else:
            hp_player1 -= attack_player2
            print("\t  {}被攻击，掉了{}血!!".format(name_player1,attack_player2))
            print("{}------------------------------{}".format(name_player1,name_player2))
            print("{}Hp{}                              {}Hp{}".format(hp_player1,mp_player1,hp_player2,mp_player2))
        #time.sleep(0.2)
        attack_player1 = random.randint(5,15)   #玩家1后攻击
        skill1_rand = random.randint(1,10)
        if skill1_rand < 8:                 #释放 则加伤害
            attack_player1 +=8 
            hp_player2 -= attack_player1
            print("\t  {}使用了{}".format(name_player1,skill1))
            print("\t  {}被攻击，掉了{}血!!".format(name_player2,attack_player1))
            print("{}------------------------------{}".format(name_player1,name_player2))
            print("{}Hp{}                              {}Hp{}".format(hp_player1,mp_player1,hp_player2,mp_player2))
        else:
            hp_player2 -= attack_player1
            print("\t  {}被攻击，掉了{}血!!".format(name_player2,attack_player1))
            print("{}------------------------------{}".format(name_player1,name_player2))
            print("{}Hp{}                              {}Hp{}".format(hp_player1,mp_player1,hp_player2,mp_player2))
        time.sleep(0.2)
        
        
print("\t\t对战结束:")
if hp_player1 <= 0 and hp_player2 <= 0:
    print("\t\t双方KO!平局!")
elif hp_player1 <= 0 and hp_player2 > 0:
    print("\t\t{}胜利!!".format(name_player2))
elif hp_player1 > 0 and hp_player2 <= 0:
    print("\t\t{}胜利!!".format(name_player1))






