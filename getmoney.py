import random

def generate_number():
    n = random.randint(1, 5)
    abcdef = random.randint(0, 999999)
    return f"{n}조 {abcdef:06d}"

print("연금복권 번호 생성기")
print("엔터를 누를 때마다 새 번호가 생성됩니다. 종료하려면 q 입력")

while True:
    user_input = input("> ")
    if user_input.lower() == "q":
        break
    print(generate_number())