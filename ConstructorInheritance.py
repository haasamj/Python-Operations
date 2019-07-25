class A:

    def __init__(self):
        print("init of A")

    def featureA(self):
        print("Feature A Working")

class B:

    def __init__(self):
        super().__init__() # it is inheritaning constructor
        print("init of B")



    def featureA(self):
        super().featureA() #it is inheriting same name function
        print("Feature BA Working")

class C(B,A):

    def __init__(self):
        super().__init__() #It is inheriting constructor
        print("init of C")

    def featureA(self):
        super().featureA()
        print("Feature CBA Working")

b1 = C()

b1.featureA()