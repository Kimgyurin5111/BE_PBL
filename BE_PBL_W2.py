def fun_list():
    print("기능을 선택하세요")
    print("1. 아기사자 등록")
    print("2. 이름으로 검색")
    print("3. 트랙으로 조회")
    print("4. 종료")

def get_num():
    num = input("선택: ")
    return num

def new_lion():
    info = {}
    name = input("🦁  이름을 입력하세요: ")
    track = input("📚  트랙을 입력하세요: ")
    grade = input("🎓  기수를 입력하세요: ")
    info = { 
        "name" : name,
        "track" : track,
        "grade" : grade
    }
    print("✅  아기사자가 등록되었습니다.\n")
    return info

def search_name(lion_list):
    name = input("🔍  검색할 이름을 입력하세요: ")
    
    for lion in lion_list:
        if lion["name"] == name:
            print(f'\n📋 검색 결과\n\n이름: {lion["name"]}\n트랙: {lion["track"]}\n기수: {lion["grade"]}\n')
            break
    else:
        print("⚠️  해당 이름의 아기사자를 찾을 수 없습니다.\n")
        return


def search_track(lion_list):
    track = input("📂 조회할 트랙을 입력하세요: ")
    if lion_list:
        track_lion = [l for l in lion_list if l["track"] == track]
        
        if track_lion:
            print(f'\n📋 {track} 트랙 아기사자 명단')
            for l in track_lion:
                print(f'- {l["name"]} ({l["grade"]})')
            print("\n")
        else:
            print("⚠️  해당 트랙을 찾을 수 없습니다.\n")


lion_list = []
while True:
    fun_list()
    num = get_num()
    
    if num == '1':
        lion_list.append(new_lion())
    
    elif num == '2':
        search_name(lion_list)
    
    elif num == '3':
        search_track(lion_list)
    
    elif num == '4':
        print("📌  프로그램을 종료합니다. ")
        break
    else:
        print(">>잘못된 번호입니다. 다시 입력해주세요.\n")
