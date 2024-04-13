#######################
# Signal and slot
#######################
import time
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt


class Ui_Functions():
    def __init__(self, window):
        self.ui = window.ui

        #######################
        # Define Variables
        #######################
        # it saves main number that will be displayed to the main display
        self.number = 0
        # it saves number after operator button is pressed. This number will be shown to the sub display above the main
        # diaplay
        self.subline_number = 0

        # it saves previous operator action
        self.subLine_action = None

        # When this afterEqual is on and if any keypad is pressed,
        # first clears the display and then add that keypad number.
        self.afterEqual = False

        # When decimal point is clicked, add decimal number.
        self.decimal_on = False
        ###################################################################

        #######################
        # Signal and slots
        #######################

        # Connect keypad buttons to pressed actions
        self.ui.button_0.clicked.connect(lambda: self.keypad_pressed(0))
        self.ui.button_1.clicked.connect(lambda: self.keypad_pressed(1))
        self.ui.button_2.clicked.connect(lambda: self.keypad_pressed(2))
        self.ui.button_3.clicked.connect(lambda: self.keypad_pressed(3))
        self.ui.button_4.clicked.connect(lambda: self.keypad_pressed(4))
        self.ui.button_5.clicked.connect(lambda: self.keypad_pressed(5))
        self.ui.button_6.clicked.connect(lambda: self.keypad_pressed(6))
        self.ui.button_7.clicked.connect(lambda: self.keypad_pressed(7))
        self.ui.button_8.clicked.connect(lambda: self.keypad_pressed(8))
        self.ui.button_9.clicked.connect(lambda: self.keypad_pressed(9))

        # This clears display and inside numbers
        self.ui.AC_buttom.clicked.connect(self.allClear_display)
        self.ui.C_button.clicked.connect(self.clear_display)
        # Calculates result using operator saved in self.subline_action and
        #               numbers saved in self.number and self.subline_number
        self.ui.equal_button.clicked.connect(self.equal_pressed)
        self.ui.add_button.clicked.connect(lambda: self.calcButton_pressed("add"))
        self.ui.subtract_button.clicked.connect(lambda: self.calcButton_pressed("substract"))
        self.ui.multi_button.clicked.connect(lambda: self.calcButton_pressed("multi"))
        self.ui.divide_button.clicked.connect(lambda: self.calcButton_pressed("divide"))

        # Multiply self.number by -1
        self.ui.sign_button.clicked.connect(self.reverseSign)

        # add decimal point to the self.number
        self.ui.dp_button.clicked.connect(self.decimal_clicked)

    def print_inside(self):
        print(f"self.number -> {self.number}")
        print(f"self.subLine_number -> {self.subLine_number}")
        print(f"self.subline_action -> {self.subline_action}")
    #######################
    # functions for slots
    #######################

    def update_number(self):
        self.ui.display_textLine.setText(str(self.number))

    def update_subline(self):
        self.ui.display_textSubLine.setText(str(self.subLine_number) + str(self.subline_action))

    # Define actions when one of keypad is pressed.
    def keypad_pressed(self, number):
        print(f"keypad_pressed -> {number}")

        self.number = self.number * 10 + number
        self.update_number()
        self.print_inside()


    # Just reverse sign, Positive becomes negative, negative becomes positive
    def reverseSign(self):
        print("reverseSign")
        self.print_inside()

    # Clear all
    def allClear_display(self):
        print("allClear_display")
        self.print_inside()

    # Clear only number and display
    def clear_display(self):
        print("clear_display")
        self.print_inside()

    # Add decimal point and go into decimal mode.
    def decimal_clicked(self):
        # Prevent user from inputting multiple decimal points Eg) 23....... No! 23. <= cannot put more dots
        print("decimal_clicked")
        self.print_inside()

    # Calculate answer
    def equal_pressed(self):
        # ユーザーが等号の前にoperatorのボタンを押したことを確認する。=　オペレータがNONEではない
        #ユーザが+や-などのoperatrorを入力していない場合, # self.subline_actionはNoneとなる.
        if self.subLine_actionine_action != None:
        # サブディスプレイに3+ or - or * or /が表示され、メインディスプレイに4が表示され、 =がクリックされた場合、
            if self.subLine_action == "+":
                self.subline_number += self.number
            elif self.subLine_action == "-":
                self.subline_number -= self.number
            elif self.subLine_action == "*":
                self.ubline_number *= self.number
            elif self.subLine_action == "/":
                self.subline_number /= self.number

        # サブ表示が空になり, メイン表示が7になる.
        # 次に入力された数字がクリアされ、その数字が表示される
        # イコールの後: メインディスプレイ: 7 (これは前の計算の答え)
        # 4 がクリックされると、メインディスプレイは 74 ではなく 4 になる。


        self.print_inside()

    def calcButton_pressed(self, action):
        # もしoperatorがsubline_actionに保存されていれば、その方程式を計算し、サブディスプレイを更新する。
        # sub displayには3+が表示され、main displayには4が表示される、
        # sub display は7+となり、main displayは0となる。
        if self.subLine_action != None:
            if self.subLine_action == "+":
                self.subline_number += self.number
            elif self.subLine_action == "-":
                self.subline_number -= self.number
            elif self.subLine_action == "*":
                self.subline_number *= self.number
            elif self.subLine_action == "/":
                self.subline_number /= self.number

        else:
            self.subLine_number = self.number
        if action == "add":
            self.subline_action = "+"
        elif action == "substract":
            self.subline_action = "-"
        elif action == "multi":
            self.subline_action = "*"
        elif action == "divide":
            self.subline_action = "/"

        self.print_inside()





    # Not used in this project but if you wanna have key input then set this part up
    ########################
    # Key Setting (ASCII)###
    ########################
    def key_event(self, event):
        # event.key() to get keyboard input
        print(event.key())
        key = event.key()
        if 48 <= key <= 57:
            self.ui.update_pass(int(chr(key)))

        # 16777220 is Enter key code
        if key == 16777220:
            self.ui.mousePressEvent()
