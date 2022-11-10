from Classes import Contact


class Phonebook:
    contact:list = []
    last_id:str = ''

    def __init__(self):
        pass

    def add(self, name:str, phone:str, comment:str):
        user = Contact.Contact(self.last_id, name, phone, comment)
        self.last_id = str(int(self.last_id) + 1)
        self.contact.append(user)

book = Phonebook()
book.add('artur', '34534534', '343434')
print(book.contact[0].show())