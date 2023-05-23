


class Library:
    def __init__(self,list,name ):
        self.booklist=list
        self.name=name
        self.lenddict = {}
    def displaybook(self):
        print(f"we Have following Book in the library {self.name}")
        for book in self.booklist:
            print(book)
        pass
    def lendbook(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Lender Book database has been updated . Now u can take the book")
        else:
            print(f"Book already taken by {self.lenddict[book]}")


    def addbook(self,book):
        self.booklist.append(book)
        print("Book has been added to book list ")
    def returnbook(self,book):
        self.lenddict.pop(book)


if __name__ == '__main__':
    harry= Library(['Java',"Python","Go Lang","Javascript","c++","c","Typescript"],"CODING BOOKS ")

    while (1):
        print(f"Welcome to {harry.name} Library ")
        print("Enter your choice to Continue")
        print("1 Display a Book ")
        print("2 Lend a Book ")
        print("3 Add a Book ")
        print("4 Return a Book ")
        user_choice=(input())
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            harry.displaybook()
        elif user_choice==2:
            book=input("Enter name of book you want to lend ")
            user=input("Enter Your Name ")
            harry.lendbook(user,book)
        elif user_choice == 3:
            book=input("Enter name of book you want to Add")
            harry.addbook(book)
        elif user_choice == 4:
            book=input("Enter name of book you wanr to return ")
            harry.returnbook(book)
        else: print("not A valid option  ")

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue


