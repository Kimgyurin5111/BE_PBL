class Member:
    def __init__(self, name):
        self.name = name
    def role(self):
        return "역할"

class Lion(Member):
    def __init__(self, name, track, grade):
        super().__init__(name)
        
        if not name.strip():
            print("이름 공백 안됩니다.")
            return None
        if not grade.strip():
            print("기수 공백 안됩니다.")
            return None
        
        self.track = track
        self.grade = grade
        
    def role(self):
        return "아기사자"

class Staff(Member):
    def __init__(self, name):
        super().__init__(name)
    
    def role(self):
        return "운영진"

class Printer:
    def __init__(self):
        pass
    
    def fun_list_printer(self):
        print("📌 기능을 선택하세요")
        print("1️⃣  아기사자 등록")
        print("2️⃣  운영진 등록")
        print("3️⃣  전체 출력")
        print("4️⃣  종료")
    
    def new_lion_print(self):
        print("✅  아기사자가 등록되었습니다.\n")
    
    def new_staff_print(self):
        print("✅ 운영진이 등록되었습니다.\n")
        
    def lion_print(self, lion_list):
        for lion in lion_list:
            print(f'- 🦁 아기사자 : {lion.name} | {lion.track} | {lion.grade}')
        
    def staff_print(self, staff_list):
        for staff in staff_list:
            print(f'- 👩‍💻 운영진 : {staff.name} | {staff.role()} ')
        
    def nolion_print(self):
        print("⚠️  해당 이름의 아기사자를 찾을 수 없습니다.\n")
    
    def notrack_print(self):
        print("⚠️  해당 트랙을 찾을 수 없습니다.\n")

class SortName:
    def __init__(self):
        pass
    def sort(self, list):
        list.sort(key=lambda x : x.name)
        return list


def get_num():
    num = input("👉 선택: ")
    return num

def new_lion():
    name = input("🦁  이름: ")
    track = input("📚  트랙: ")
    grade = input("🎓  기수: ")
    
    printer.new_lion_print()
    return Lion(name, track, grade)

def new_staff():
    name = input("🧑‍🏫 이름: ")
    
    printer.new_staff_print()
    return Staff(name)


lion_list = []
staff_list = []
printer = Printer()
sort_name = SortName()
while True:
    printer.fun_list_printer()
    num = get_num()
    
    if num == '1':
        lion_list.append(new_lion())
    
    elif num == '2':
        staff_list.append(new_staff())
    
    elif num == '3':
        sort_name.sort(lion_list)
        sort_name.sort(staff_list)
        printer.lion_print(lion_list)
        printer.staff_print(staff_list)
    
    elif num == '4':
        print("📌  프로그램을 종료합니다. ")
        break
    else:
        print(">>잘못된 번호입니다. 다시 입력해주세요.\n")
