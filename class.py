class Computer:
    def config(self): # Self is the object you are passing 
        print("This is a machine with i5")

a = '0'

comp1 = Computer()

Computer.config(comp1) # mention the class 

comp1.config() # directly calling using object