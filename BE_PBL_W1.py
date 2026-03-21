def get_input():
    name = input('✏️    아기 사자 이름을 입력하세요 (종료하려면 q 입력): ')
    return name    

def check_blank(name):
    if not name.strip():
        print("⚠️   이름이 비어있습니다. 다시 입력해주세요.")
        return False
    else:
        babylion.append(name)
        print(f'✅  {name} 이(가) 등록되었습니다.')
        return True

def end():
    print("\n📌  이름 입력을 종료합니다.\n")
    print("📋  현재 아기사자 명단입니다.")   
    for i in range(len(babylion)):
        print(f'🦁  {i+1}. {babylion[i]}')   

babylion = []
print(f'🦁  아기 사자 명단 관리 프로그램입니다.')
while True:
    name = get_input()
    if name == 'q':
        end()
        break
    
    if not check_blank(name):
        continue

