class sanjay():
    def __init__(self):
        self.name = "Sanjay"
        self.age = 22
    def update(self):
        self.age = 30
    def compare(self,other):
        return True if self.age == other.age else False
        # this is a conditional expresion or ternary operation
    
sa = sanjay()
s2 = sanjay()

s2.update()

if sa.compare(s2):
    print("Both are same")
else:
    print("Both are different")

