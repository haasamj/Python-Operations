class Pycharm:

    def execute(self):
        print("compiling")
        print("running")

class MyEditor:

    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:

    def code(self, ide):
        ide.execute()

i = MyEditor()

lap1 = Laptop()

lap1.code(i)

