class A:

    def method_a(self):
        print("ini adalah method a")


class B:

     def method_b(self):
        print("ini adalah method b")
    

class C(A,B):
    pass

object = C()

object.method_a()
object.method_b()