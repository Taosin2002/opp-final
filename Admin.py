class Admin:
    admin_acounts = []
    def __init__(self,name,password) -> None:
        self.name = name
        self.password = password
        self.admin_acounts.append(self)

    def all(self):
        for acount in Admin.admin_acounts:
            print(acount.name,acount.password)

