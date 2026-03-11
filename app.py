from database import create_tables
from models import register_user, add_course, enroll_user_in_course

create_tables()

def main():
    while True:
        print("\n--- Onlayn Öyrənmə platforması ---")
        print("1. Qeydiyyat")
        print("2. Kurs əlavə et")
        print("3. Kursa qoşul")
        print("0. Çıxış")

        choice=input("Seçim: ")

        if choice == "1":
            username=input("İstifadəçi adı: ")
            password=input("Şifrə: ")
            if register_user(username, password):
                print("Qeydiyyat uğurludur!")
            else:
                print("Qeydiyyat alınmadı!")

        elif choice == "2":
            name=input("Kurs adı: ")
            description=input("Təsvir: ")
            if add_course(name, description):
                print("Kurs əlavə olundu!")
            else:
                print("Kurs əlavə etmək alınmadı!")

        elif choice == "3":
            try:
                user_id=int(input("İstifadəçi ID: "))
                course_id=int(input("Kurs ID: "))
                if enroll_user_in_course(user_id, course_id):
                    print("Kursa qoşuldunuz!")
                else:
                    print("Qoşulmaq alınmadı!")
            except ValueError:
                print("ID-lər yalnız rəqəm ola bilər!")

        elif choice == "0":
            print("Çıxılır...")
            break

        else:
            print("Yalnış seçim!")


if __name__ == '__main__':
    main()