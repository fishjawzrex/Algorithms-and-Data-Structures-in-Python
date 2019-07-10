class Pet(object):
    def __init__(self, name):
        self.name = name
        self.fur_color = None
    def change_name(self, new_name):
        self.name = new_name
    def get_name(self):
        return self.name
    def change_color(self, new_color):
        self.fur_color = new_color
    def get_color(self):
        return self.fur_color
    def implicit(self):
        print "PARENT IMPLICIT()"
    def override(self):
        print "PARENT OVERRIDDEN()"
    def alter(self):
        print "PARENT ALTERED()"
    def __str__(self):
        return "My name is " + str(self.name) + \
               " and I am " + str(self.fur_color) + \
               " in color."

#the dog class inherits from the Pet parent class 
class Dog(Pet):
    #we can use a parent method after it has been overridden
    def alter(self):
        print "CHILD ALTERED"
        super(Dog, self).alter()#call alter method from parent class
        print "CHILD AFTER ALTERED"

#note that the cat class is not a child of the Pet class        
class Cat(object):  
    def __init__(self, name, eye_color):
        #self.name = name 
        self.pet = Pet(name)#composition like __init__, but a method
        self.eye_color = eye_color#inititalize extra parameter
        
fluffy = Dog("fluffy")
fluffy.alter()
print fluffy.get_name()
print fluffy.__str__()
mittens = Cat("mittens", "red")
mittens.pet.implicit()

print mittens
        