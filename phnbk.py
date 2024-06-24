def work_with_phonebook():
    phone_book=read_txt('phon.txt')
    choice=show_menu()
    while (choice!=7):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            for j, z in find_by_lastname(phone_book,last_name).items():
                print(j, z)
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new  number ')
            change_number(phone_book,last_name,new_number)
        elif choice==4:
            add_user(phone_book)
        elif choice==5:
            last_name=input('lastname ')
            phone_book.remove(find_by_lastname(phone_book, last_name))
        elif choice==6:
            num_string = input('Введите номер строки ')
            copy_user(phone_book, num_string)
        choice=show_menu()
    write_txt('phon.txt', phone_book)


def show_menu():
    print("\nВыберите необходимое действие:\n",
          "1. Отобразить весь справочник\n",
          "2. Найти абонента по фамилии\n",
          "3. Изменить номер телефона у абонента\n",
          "4. Добавить абонента в справочник\n", 
          "5. Удалить пользователя по фамилии\n",
          "6. Копировать пользователя\n",
          "7. Завершить работу")
    choice = int(input())
    return choice


def print_result(phnbk):
    for i in phnbk:
        print(i)


def find_by_lastname(phnbk, lstnm):
    for i in phnbk:
       if i.get('Фамилия') == lstnm:
            return i
               

def change_number(phnbk, lstnm, nwnmbr):
    find_by_lastname(phnbk, lstnm)['Телефон'] = nwnmbr
 

def add_user(phnbk):                
    last_name = input('Введите фамилию ')
    name = input('Введите имя ')
    number = input('Введите номер ')
    discribe = input('Введите описание ')
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    data = [last_name, name, number, discribe + '\n']
    phnbk.append(dict(zip(fields, data)))


def read_txt(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book


def write_txt(filename , phone_book):
    with open('phon.txt','w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}')


def copy_user(phnbk, nmstr):
    s = phnbk[int(nmstr)-1].values()
    with open('text.txt', 'a', encoding='utf-8') as file:
        file.writelines(s)


work_with_phonebook()