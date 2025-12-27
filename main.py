def show_menu():
    print("\n====== 📱 Contact Book v2.2 ======")
    print("1. + Yangi kontakt qoshish")
    print("2. 📄 Barcha kontaktlarni korish")
    print("3. 🔍 Kontaktni ism boyicha qidirish")
    print("4. 📧 Faqat @gmail.com kontaktlarni korish")
    print("5. 🚪 Dasturni yakunlash")


def is_valid_contact(contact):
    name = contact[0]
    number = contact[1]
    gmail = contact[2]

    if name == "" or not name.isalpha():
        return False

    if number == "" or not number.isdigit() or not (9 <= len(number) <= 13):
        return False

    if gmail == "" or "@" not in gmail:
        return False

    return True


def add_contact(contacts):
    name = input("Ismni kiriting: ").strip()
    number = input("Nomerni  kiriting: ").strip()
    gmail = input("Gmailni kiriting: ").strip()

    contact = [name, number, gmail]
    if not is_valid_contact(contact):
        print("Kontak xato kiritildi! ")
        return
    
    contacts.append(contact)

    print("Kontak qo'shildi! ")


def list_contacts(contacts):
    if not contacts:
        print("Kontak mavjud emas! ")
        return
    for contact in contacts:
        print([contact[0], contact[1], contact[2]])    
        

def search_contact(contact_list):
    if not contact_list:
        print("Kontak mavjud emas! ")
        return 
    name = input("Qaysi isimni topmoqchisiz: ")
    topildi = False

    for contact in contact_list:
        if contact[0].lower() == name.lower():
            print(contact)
            topildi = True
            
    if not topildi:
        print("Bunday isim mavjud emas! ") 
              
  
def filter_gmail_contacts(contact_list):
    topildi = False

    for contact in contact_list:
        if contact[2].endswith("@gmail.com"):
            print(contact)
            topildi = True
            

    if not topildi:
        print("Gmail topilmadi: ")
        

def main():
    contacts = []

    while True:
        show_menu()
        choice = input("Tanlang (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            list_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            filter_gmail_contacts(contacts)
        elif choice == "5":
            print("👋 Dasturni yakunlayapmiz. Xayr!")
            break
        else:
            print("Notogri tanlov. Iltimos, 1 dan 5 gacha son kiriting.")

main()
