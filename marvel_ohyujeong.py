class Marvel:
    def __init__(self,name,offensive,defensive,health):
        self.name=name
        self.offensive=offensive
        self.defensive=defensive
        self.health=health
    def character_info(self):
        print(" 이름 {0}\n 공격력: {1} \n 방어력: {2} \n 체력: {3}\n".format(self.name,self.offensive,self.defensive,self.health))
    def attack(self,other):
        other.health=other.health-(self.offensive-other.defensive)
    def defend(self,other):
        self.health=self.health-(other.offensive-self.defensive)
    def power_up_1(self):
        self.health=100
        self.defensive+=10
    def power_up_2(self):
        self.power_up_1()
        self.offensive+=10
        self.defensive=self.defensive
        self.health+=200

class IronMan(Marvel):
    pass
class CaptainAmerica(Marvel):
    pass
class Thor(Marvel):
    pass
class Thanos(Marvel):
    pass

IronMan=IronMan("IronMan",70,50,100)
CaptainAmerica=CaptainAmerica("CaptainAmerica",60,50,100)
Thor=Thor("Thor",90,20,100)
Thanos=Thanos("Thanos",100,50,300)

print("1.IronMan 2.CaptainAmerica 3.Thor")
select=int(input("당신의 캐릭터 번호를 선택해주세요(1,2,3) : "))

import random

if select == 1 :
    enemy_list=[Thor,CaptainAmerica]
    enemy=random.choice(enemy_list)
    enemy_list.remove(enemy)
    print("--내 캐릭터--")
    IronMan.character_info()
    print("--적 캐릭터--")
    enemy.character_info()
    print('--배틀--\n')
    while True:
        IronMan.attack(enemy)
        IronMan.defend(enemy)
        if enemy.health<=0:
            print('당신이 이겼습니다!')
            print("\n***두 번째 스테이지***")
            IronMan.power_up_1()
            print("--내 캐릭터--")
            IronMan.character_info()
            enemy=random.choice(enemy_list)
            print("--적 캐릭터--")
            enemy.character_info()
            print('--배틀--\n')
            break
        elif IronMan.health<=0 and enemy.health>0:
            print('당신이 졌습니다!')
            break
    while True:
      if IronMan.defensive==60:
          IronMan.attack(enemy)
          IronMan.defend(enemy)
          if enemy.health<=0:
              print('당신이 이겼습니다!')
              print("\n***세 번째 스테이지***")
              IronMan.power_up_2()
              print('--내 캐릭터--')
              IronMan.character_info()
              print('--적 캐릭터--')
              Thanos.character_info()
              print('--배틀--\n')
              break
          elif IronMan.health<=0:
                print('당신이 졌습니다!')
                break
      else:
          break
    while True:
        if IronMan.health<=300 and IronMan.health>0:
           IronMan.attack(Thanos)
           IronMan.defend(Thanos)
           if Thanos.health<=0 and IronMan.health>0:
               print('당신이 이겼습니다!')
               break
           elif IronMan.health<=0 and Thanos.health>0:
               print('당신이 졌습니다!')
               break
        else:
            break
elif select == 2 :
    enemy_list=[IronMan,Thor]
    enemy=random.choice(enemy_list)
    enemy_list.remove(enemy)
    print("--내 캐릭터--")
    CaptainAmerica.character_info()
    print("--적 캐릭터--")
    enemy.character_info()
    print('--배틀--\n')
    while True:
        CaptainAmerica.attack(enemy)
        CaptainAmerica.defend(enemy)
        if enemy.health<=0:
            print('당신이 이겼습니다!')
            print("\n***두 번째 스테이지***")
            CaptainAmerica.power_up_1()
            print("--내 캐릭터--")
            CaptainAmerica.character_info()
            enemy=random.choice(enemy_list)
            print("--적 캐릭터--")
            enemy.character_info()
            print('--배틀--\n')
            break
        elif CaptainAmerica.health<=0 and enemy.health>0:
            print('당신이 졌습니다!')
            break
    while True:
      if CaptainAmerica.defensive==60:
          CaptainAmerica.attack(enemy)
          CaptainAmerica.defend(enemy)
          if enemy.health<=0:
              print('당신이 이겼습니다!')
              print("\n***세 번째 스테이지***")
              CaptainAmerica.power_up_2()
              print('--내 캐릭터--')
              CaptainAmerica.character_info()
              print('--적 캐릭터--')
              Thanos.character_info()
              print('--배틀--\n')
              break
          elif CaptainAmerica.health<=0:
                print('당신이 졌습니다!')
                break
      else:
          break
    while True:
        if CaptainAmerica.health<=300 and CaptainAmerica.health>0:
           CaptainAmerica.attack(Thanos)
           CaptainAmerica.defend(Thanos)
           if Thanos.health<=0:
               print('당신이 이겼습니다!')
               break
           elif CaptainAmerica.health<=0 and Thanos.health>0:
               print('당신이 졌습니다!')
               break
        else:
            break
elif select == 3 :
    enemy_list=[IronMan,CaptainAmerica]
    enemy=random.choice(enemy_list)
    enemy_list.remove(enemy)
    print("--내 캐릭터--")
    Thor.character_info()
    print("--적 캐릭터--")
    enemy.character_info()
    print('--배틀--\n')
    while True:
        Thor.attack(enemy)
        Thor.defend(enemy)
        if enemy.health<=0:
            print('당신이 이겼습니다!')
            print("\n***두 번째 스테이지***")
            Thor.power_up_1()
            print("--내 캐릭터--")
            Thor.character_info()
            enemy=random.choice(enemy_list)
            print("--적 캐릭터--")
            enemy.character_info()
            print('--배틀--\n')
            break
        elif Thor.health<=0 and enemy.health>0:
            print('당신이 졌습니다!')
            break
    while True:
      if Thor.defensive==30:
          Thor.attack(enemy)
          Thor.defend(enemy)
          if enemy.health<=0 and Thor.health>0:
              print('당신이 이겼습니다!')
              print("\n***세 번째 스테이지***")
              Thor.power_up_2()
              print('--내 캐릭터--')
              Thor.character_info()
              print('--적 캐릭터--')
              Thanos.character_info()
              print('--배틀--\n')
              break
          elif Thor.health<=0:
                print('당신이 졌습니다!')
                break
      else:
          break
    while True:
        if Thor.health<=300 and Thor.health>0:
           Thor.attack(Thanos)
           Thor.defend(Thanos)
           if Thanos.health<=0 and Thor.health>0:
               print('당신이 이겼습니다!')
               break
           elif Thor.health<=0 and Thanos.health>0:
               print('당신이 졌습니다!')
               break
        else:
            break

