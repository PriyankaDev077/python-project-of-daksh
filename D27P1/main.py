class myClass:
    __privateVar = 27;
def __privMeth(self):
    print("I'm inside myClass")
    def hello(self):
       	print("Private Variable value: ",myClass.__privateVar)
foo = myclass()
foo.hello()
foo.privmeth