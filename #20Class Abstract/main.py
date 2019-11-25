#membuat class abstract 

#import ABC untuk abstract (Abstract Base Class)
from abc import ABC, abstractmethod

class Button(ABC): #menjadi class abstract

    @abstractmethod
    def click(self):
        pass

class PushButton(Button):

    def click(self):
        print("push button click")

class RadioButton(Button):

    def click(self):
        print("radio button click")

tombol1 = PushButton()
tombol2 = RadioButton()

tombol1.click()
tombol2.click()
help(tombol1)