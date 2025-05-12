class Animal ():
    def sound(self):
        return "Various types of sound..!"

class dog():
    def sound(self):
        return "Bark"

object=Animal()
print(object.sound())

object=dog()
print(object.sound())


