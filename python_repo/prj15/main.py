import random
from pokemon.pokemon import Pokemon

def process_attack(attacker, defender):
    while True:
        print(f"{attacker.name}의 공격 !")
        dmg = attacker.atk - defender.arm
        defender.hp -= dmg
        print(f"데미지 : {dmg}")
        print(f" {defender.name} 의 남은 체력 : {defender.hp}")
        if defender.hp <= 0:
            print(f"Game Set, {defender.name} lose TnT")
            return True
        else:
            return False

print("=== 너로 정했다 ===")
print("1. 피카츄 2. 꼬부기 3. 파이리")
p1 = Pokemon("피카츄", 100, 10, 3)
p2 = Pokemon("꼬부기", 110, 8, 5)
p3 = Pokemon("파이리", 90, 12, 1)

n = int(input("선택할 포켓몬 번호 : "))
match n:

    case 1:
        user = Pokemon("피카츄", 100, 10, 3)
    case 2:
        user = Pokemon("꼬부기", 110, 8, 5)
    case 3:
        user = Pokemon("파이리", 90, 12, 1)
    case _:
        user = None

r = random.randint(1, 3)
match r:
    case 1:
        com = Pokemon("피카츄", 100, 10, 3)
    case 2:
        com = Pokemon("꼬부기", 110, 8, 5)
    case 3:
        com = Pokemon("파이리", 90, 12, 1)
    case _:
        com = None

print(f"user {user}")
print(f"com {com}")

#battle

while True:
    #user -> com
    is_finish = process_attack(user, com)
    if is_finish: break

    # com -> user
    is_finish = process_attack(com,user)
    if is_finish: break
