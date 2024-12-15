class computer:
    def __init__(self):
        self.name = "Sanjay"
        self.work = "Engineer"
    
    work = ""
    def update(work,changed_val):
        work = changed_val
        # print(work)

c1 = computer()
c2 = computer()

print(c1.name)
print(c2.work)
print(c1.work)

c2.update("change")

print(c1.work)
print(c2.work)