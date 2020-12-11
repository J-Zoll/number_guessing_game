import tkinter as tk
from tkinter import font
import math

class GuessingGame:
    UPPER_LIMIT = 101
    LOWER_LIMIT = 1

    def __init__(self):
        self.model = BinarySearch(GuessingGame.LOWER_LIMIT, GuessingGame.UPPER_LIMIT)
        self.view = View()
        self.controller = Conroller(self.model, self.view)

        self.view.register(self.controller)
    
    def start(self):
        self.view.show()


class Observer():
    def update(self):
        pass


class Observable():
    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)
    
    def updateObs(self, message):
        for obs in self.observers:
            obs.update(message)


class Conroller(Observer):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        view.update(model.getNum())

    def update(self, str):
        if(str == 'correct'):
            print('nice!')
            exit()
        elif(str == 'lower'):
            self.model.lower()
            new_num = self.model.getNum()
            self.view.update(new_num)
        elif(str == 'higher'):
            self.model.higher()
            new_num = self.model.getNum()
            self.view.update(new_num)


class BinarySearch:
    def __init__(self, lower_limit=0, upper_limit=100):
        self.upper_limit = upper_limit
        self.lower_limit = lower_limit
        self.num = self._get_center()

    def _get_center(self):
        return math.floor( (self.upper_limit - self.lower_limit) / 2) + self.lower_limit
    
    def lower(self):
        self.upper_limit = self.num
        self.num = self._get_center()

    def higher(self):
        self.lower_limit = self.num
        self.num = self._get_center()

    def getNum(self):
        return self.num

class View(Observer, Observable):
    FRAME_WIDTH = 600
    FRAME_HEIGHT = 450

    INTRO_TEXT = 'Is it this number?'
    DEFAULT_NUMBER_TEXT = 'NaN'

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('guessing game')
        self.root.geometry(f'{View.FRAME_WIDTH}x{View.FRAME_HEIGHT}')
        self.root.resizable(False, False)

        font_intro = font.Font(family='sans-serif', size=20, weight=tk.font.BOLD)
        font_number = font.Font(family='sans-serif', size=200, weight=tk.font.BOLD)
        font_btn = font.Font(family='sans-serif', size=30, weight=tk.font.BOLD)

        lbl_intro = tk.Label(text=View.INTRO_TEXT, font=font_intro)
        self.lbl_number = tk.Label(text=View.DEFAULT_NUMBER_TEXT, font=font_number)

        btn_lower = tk.Button(self.root, text='lower', font=font_btn, command=(lambda : self.updateObs('lower')))
        btn_correct = tk.Button(self.root, text='correct', font=font_btn, command=(lambda : self.updateObs('correct')))
        btn_higher = tk.Button(self.root, text='higher', font=font_btn, command=(lambda : self.updateObs('higher')))

        lbl_intro.grid(row=1, column=1, columnspan=3, pady=10)
        self.lbl_number.grid(row=2, column=1, columnspan=3, pady=25)

        btn_lower.grid(row=3, column=1, padx=10)
        btn_correct.grid(row=3, column=2, padx=10)
        btn_higher.grid(row=3, column=3, padx=10)

        Observable.__init__(self)
        Observer.__init__(self)

    def show(self):
        self.root.mainloop()
    
    def update(self, new_num):
        self.lbl_number.config(text=new_num)



def main():
    game = GuessingGame()
    game.start()


if __name__ == "__main__":
    main()
