# method resolution order // multiple inheritance

class A:
    def show(self):
        print("ini adalah show a")

class B:
    def show(self):
        print("ini adalah show b")


class C(A, B): #tergantung urutan saat inherit
    pass

object = C()
object.show()

#cara melihat urutan eksekusi (method resolution order)
help(object)
