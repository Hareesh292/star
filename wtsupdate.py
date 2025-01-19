class v1():
    def __init__(self,name,mobno):
        self.name=name
        self.mobno=mobno
    def details(self):
        print(self.name)
        print(self.mobno)
class v2(v1):
    def __init__(self,name,mobno,email,gender):
        super().__init__(name,mobno)
        self.email=email
        self.gender=gender
    def details(self):
        super().details()
        print(self.email)
        print(self.gender)
class v3(v2):
    def __init__(self,name,mobno,email,gender,status,vdcall):
        super().__init__(name,mobno,email,gender)
        self.status=status
        self.vdcall=vdcall
    def details(self):
        super().details()
        print(self.status)
        print(self.vdcall)

obj=v3('hareesh',1234567891,'hari@gamil.com','male','posiible','possible')
obj.details()