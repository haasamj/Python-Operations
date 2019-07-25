# class A:
#     def feature1(self):
#         print("Feature 1 working")  # B is inheriting A features. It is single level inheritance
#
#     def feature2(self):
#         print("Feature 2 working")
#
# class B(A):
#     def feature3(self):
#         print("Feature 3 working")
#
#     def feature4(self):
#         print("Feature 4 working")
#
# a1 = A()
#
# a1.feature1()
# a1.feature2()
#
# b1 = B()
#
# b1.feature1()

#Multi-level Inheritance : B is inheriting A features and C is heriting B features so it means B is inheriting A features so C is also inheriting A features through B.

# class A:
#     def feature1(self):
#         print("Feature 1 working")
#
#     def feature2(self):
#         print("Feature 2 working")
#
# class B(A):
#     def feature3(self):
#         print("Feature 3 working")
#
#     def feature4(self):
#         print("Feature 4 working")
#
# class C(B):
#     def feature5(self):
#         print("Feature 5 working")
#
# a1 = A()
#
# a1.feature1()
#
# b1 = B()
#
# b1.feature1()
#
# c1 = C()
#
# c1.feature1()
# c1.feature3()

#Multiple Inheritance: C is inheriting multiple class like in this C is inheriting A and B both.
# class A:
#     def feature1(self):
#         print("Feature 1 working")
#
#     def feature2(self):
#         print("Feature 2 working")
#
# class B:
#     def feature3(self):
#         print("Feature 3 working")
#
#     def feature4(self):
#         print("Feature 4 working")
#
# class C(A,B):
#     def feature5(self):
#         print("Feature 5 working")
#
# c1 = C()
#
# c1.feature1()
# c1.feature3()