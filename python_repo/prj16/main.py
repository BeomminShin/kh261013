class MapleStory:
    def __init__(self, char, atk, hp, arm):
        self.character = char
        self.attack = atk
        self.hp = hp
        self.armor = arm

    def __str__(self):
        return f"닉네임 = {self.character} / 공격력 = {self.attack} / 체력 = {self.hp} / 방어력 = {self.armor}"

    def hunt(self):
        print(f"{self.character}이(가) 사냥을 시작합니다!")
        damage = 25 - self.armor
        if damage < 5:
            damage = 5
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"체력이 {damage} 감소했습니다. (현재 체력: {self.hp})")

    def heal(self):
        print(f"체력을 회복합니다!")
        self.hp += 30
        print(f"체력이 30 회복되었습니다. (현재 체력: {self.hp})")

    def upgrade_weapon(self):
        print(f"장비를 강화합니다!")
        self.attack += 5
        self.armor += 2
        print(f"강화 성공! 공격력 +5, 방어력 +2")


def main():
    print("=== 메이플스토리 캐릭터 관리 프로그램 ===")

    user_name = input("생성할 캐릭터의 닉네임을 입력하세요: ")

    my_char = MapleStory(user_name, 15, 100, 10)

    while True:
        print("-------------------------")
        print("1. 캐릭터 정보 보기")
        print("2. 사냥하기")
        print("3. 체력 회복")
        print("4. 장비 강화")
        print("5. 게임 종료")
        print("-------------------------")

        c = input("원하는 메뉴의 번호를 입력하세요: ")

        if c == '1':
            print("[현재 캐릭터 상태]")
            print(my_char)
        elif c == '2':
            if my_char.hp <= 0:
                print("체력이 0입니다! 먼저 체력을 회복하세요.")
            else:
                my_char.hunt()
        elif c == '3':
            my_char.heal()
        elif c == '4':
            my_char.upgrade_weapon()
        elif c == '5':
            print(f"프로그램을 종료합니다.")
            break
        else:
            print("올바른 번호를 입력해주세요.")


if __name__ == "__main__":
    main()