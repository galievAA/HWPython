class Contact:
    id: str
    name:str
    phone:str
    comment:str

    def __init__(self,id:str, name:str,phone:str, comment:str):
        self.id = id
        self.name = name
        self.phone = phone
        self.comment = comment

    def show(self):
        return(self.id,self.name,self.phone,self.comment)

    def set_name(self,name:str):
        self.name = name


artur = Contact('1', 'artur', '89154908846', 'home')
print(artur.show())
artur.set_name('artur')
print(artur.show)
