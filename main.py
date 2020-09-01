#imports
import math
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button

#app class
class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)

        self.cols = 1

        self.numbers = ['0','1','2','3','4','5','6','7','8','9']
        self.operators = ['+','-','*','/','%']
        
        self.last_was_operator = None
        self.dot_count = 0

        #output
        self.output = GridLayout()
        self.output.cols = 1

        self.heading = Label(text="Welcome to PCalc!!!",font_size=40)
        self.output.add_widget(self.heading)
        
        self.output_screen = TextInput(text='0',multiline=False,halign="right",font_size=30)
        self.output.add_widget(self.output_screen)
        
        self.add_widget(self.output)

        #input
        self.input = GridLayout()
        self.input.cols = 2

        self.input.numpad = GridLayout()
        self.input.numpad.cols = 8

        self.sine = Button(text = 'sin',background_color =(0.3, 0.3, 0.3, 1),on_press=self.trig)
        self.arcsine = Button(text = 'arcsin',background_color =(0.3, 0.3, 0.3, 1),on_press=self.trig)
        self.remainder = Button(text = '%',background_color =(0.3, 0.3, 0.3, 1),on_press=self.operator)
        self.gap1 = Label()
        self.bksp = Button(text = '<-',background_color =(0.3, 0.3, 0.3, 1),on_press=self.bk)
        self.clear = Button(text = 'C',background_color =(0.3, 0.3, 0.3, 1),on_press=self.cl)
        self.absval = Button(text = '|x|',background_color =(0.3, 0.3, 0.3, 1),on_press=self.ab)
        self.divide = Button(text = '/',background_color =(0.3, 0.3, 0.3, 1),on_press=self.operator)
        
        self.cosine = Button(text = 'cos',background_color =(0.3, 0.3, 0.3, 1),on_press=self.trig)
        self.arccosine = Button(text = 'arccos',background_color =(0.3, 0.3, 0.3, 1),on_press=self.trig)
        self.square = Button(text = 'x^2',background_color =(0.3, 0.3, 0.3, 1),on_press=self.sqr)
        self.gap2 = Label()
        self.seven = Button(text = '7',background_color =(0.1, 0.1, 0.1, 1),on_press=self.number)
        self.eight = Button(text = '8',background_color =(0.1, 0.1, 0.1, 1),on_press=self.number)
        self.nine = Button(text = '9',background_color =(0.1, 0.1, 0.1, 1),on_press=self.number)
        self.multiply = Button(text = '*',background_color =(0.3, 0.3, 0.3, 1),on_press=self.operator)

        self.tangent = Button(text = 'tan',background_color =(0.3, 0.3, 0.3, 1),on_press=self.trig)
        self.arctangent = Button(text = 'arctan',background_color =(0.3, 0.3, 0.3, 1),on_press=self.trig)
        self.root = Button(text = 'sqrt',background_color =(0.3, 0.3, 0.3, 1),on_press=self.sqrt)
        self.gap3 = Label()
        self.four = Button(text = '4',background_color =(0.1, 0.1, 0.1, 1),on_press=self.number)
        self.five = Button(text = '5',background_color =(0.1, 0.1, 0.1, 1),on_press=self.number)
        self.six = Button(text = '6',background_color =(0.1, 0.1, 0.1, 1),on_press=self.number)
        self.subtract = Button(text = '-',background_color =(0.3, 0.3, 0.3, 1),on_press=self.operator)

        self.pival = Button(text = 'pi',background_color =(0.3, 0.3, 0.3, 1),on_press=self.pi)
        self.epowx = Button(text = 'e^x',background_color =(0.3, 0.3, 0.3, 1),on_press=self.epowerx)
        self.gifx = Button(text = '[x]',background_color =(0.3, 0.3, 0.3, 1),on_press=self.gif)
        self.gap4 = Label()
        self.one = Button(text = '1',background_color =(0.1, 0.1, 0.1, 1),on_press=self.number)
        self.two = Button(text = '2',background_color =(0.1, 0.1, 0.1, 1),on_press=self.number)
        self.three = Button(text = '3',background_color =(0.1, 0.1, 0.1, 1),on_press=self.number)
        self.add = Button(text = '+',background_color =(0.3, 0.3, 0.3, 1),on_press=self.operator)

        self.logx = Button(text = 'log(x)',background_color =(0.3, 0.3, 0.3, 1),on_press=self.logarithm)
        self.tenpowx = Button(text = '10^x',background_color =(0.3, 0.3, 0.3, 1),on_press=self.tenpowerx)
        self.xfact = Button(text = 'x!',background_color =(0.3, 0.3, 0.3, 1),on_press=self.fact)
        self.gap5 = Label()
        self.dot = Button(text = '.',background_color =(0.3, 0.3, 0.3, 1),on_press=self.dt)
        self.zero = Button(text = '0',background_color =(0.1, 0.1, 0.1, 1),on_press=self.number)
        self.negate = Button(text = '+/-',background_color =(0.3, 0.3, 0.3, 1),on_press=self.ng)
        self.equal = Button(text = '=',background_color =(0, 1, 0, 1),on_press=self.equate)

        self.input.numpad.add_widget(self.sine)
        self.input.numpad.add_widget(self.arcsine)
        self.input.numpad.add_widget(self.remainder)
        self.input.numpad.add_widget(self.gap1)
        self.input.numpad.add_widget(self.bksp)
        self.input.numpad.add_widget(self.clear)
        self.input.numpad.add_widget(self.absval)
        self.input.numpad.add_widget(self.divide)
        
        self.input.numpad.add_widget(self.cosine)
        self.input.numpad.add_widget(self.arccosine)
        self.input.numpad.add_widget(self.square)
        self.input.numpad.add_widget(self.gap2)
        self.input.numpad.add_widget(self.seven)
        self.input.numpad.add_widget(self.eight)
        self.input.numpad.add_widget(self.nine)
        self.input.numpad.add_widget(self.multiply)
        
        self.input.numpad.add_widget(self.tangent)
        self.input.numpad.add_widget(self.arctangent)
        self.input.numpad.add_widget(self.root)
        self.input.numpad.add_widget(self.gap3)
        self.input.numpad.add_widget(self.four)
        self.input.numpad.add_widget(self.five)
        self.input.numpad.add_widget(self.six)
        self.input.numpad.add_widget(self.subtract)
        
        self.input.numpad.add_widget(self.pival)
        self.input.numpad.add_widget(self.epowx)
        self.input.numpad.add_widget(self.gifx)
        self.input.numpad.add_widget(self.gap4)
        self.input.numpad.add_widget(self.one)
        self.input.numpad.add_widget(self.two)
        self.input.numpad.add_widget(self.three)
        self.input.numpad.add_widget(self.add)
        
        self.input.numpad.add_widget(self.logx)
        self.input.numpad.add_widget(self.tenpowx)
        self.input.numpad.add_widget(self.xfact)
        self.input.numpad.add_widget(self.gap5)
        self.input.numpad.add_widget(self.dot)
        self.input.numpad.add_widget(self.zero)
        self.input.numpad.add_widget(self.negate)
        self.input.numpad.add_widget(self.equal)

        self.input.add_widget(self.input.numpad)
        self.add_widget(self.input)       

    def bk(self, instance):
        if len(str(self.output_screen.text))==1:
            self.output_screen.text = str('0')
        else:
            self.output_screen.text = str(self.output_screen.text)[:-1]
        self.last_was_operator=None

    def cl(self, instance):
        self.output_screen.text = '0'
        self.last_was_operator=None

    def ab(self, instance):
        try:
            if str(self.output_screen.text)[0]=='-':
                self.output_screen.text = str(self.output_screen.text)[1:]
            self.last_was_operator=None
        except ZeroDivisionError:
            self.output_screen.text = "cannot divide by zero!"
        except SyntaxError:
            self.output_screen.text = "invalid input!"
        except ValueError:
            self.output_screen.text = "invalid input!"
        except OverflowError:
            self.output_screen.text = "Overflow!"

    def dt(self, instance):
        if str(self.output_screen.text) not in ('invalid input!','cannot divide by zero!'):
            operator_list=[0]
            s = str(self.output_screen.text)
            self.dot_count = str(self.output_screen.text).count('.')
            for i in s:
                if i in self.operators:
                    operator_list.append(s.index(i))
            if s[max(operator_list)+1:].count('.')==0:
                if str(self.output_screen.text)[-1] in self.operators:
                    self.output_screen.text = str(self.output_screen.text)+'0.'
                else:
                    self.output_screen.text = str(self.output_screen.text)+'.'
            self.last_was_operator=None

    def ng(self, instance):
        try:
            if eval(str(self.output_screen.text))!=0:
                if str(self.output_screen.text)[0]=='-':
                    self.output_screen.text = str(self.output_screen.text)[1:]
                else:
                    self.output_screen.text = '-'+str(self.output_screen.text)
        except ZeroDivisionError:
            self.output_screen.text = "cannot divide by zero!"
        except SyntaxError:
            self.output_screen.text = "invalid input!"
        except ValueError:
            self.output_screen.text = "invalid input!"
        except OverflowError:
            self.output_screen.text = "Overflow!"
        self.last_was_operator=None

    def number(self, instance):
        if self.last_was_operator == "=":
            self.output_screen.text = '0'
        if str(instance.text) in self.numbers:
            if str(self.output_screen.text)=='0':
                self.output_screen.text = str(instance.text)
            elif str(self.output_screen.text)[-1]=='0' and str(self.output_screen.text)[-2] in self.operators:
                self.output_screen.text = str(self.output_screen.text)[:-1]+str(instance.text)
            elif self.last_was_operator=="pi":
                self.output_screen.text = str(self.output_screen.text)+'*'+str(instance.text)
            else:
                self.output_screen.text = str(self.output_screen.text)+str(instance.text)
        self.last_was_operator=None

    def operator(self, instance):
        if str(instance.text) in self.operators:
            if str(self.output_screen.text) in ('invalid input!','cannot divide by zero!'):
                self.output_screen.text = '0'+str(instance.text)
            else:
                if str(self.output_screen.text)[-1] not in self.operators:
                    self.equate(self)
                    self.output_screen.text = str(self.output_screen.text)+str(instance.text)
                else:
                    self.output_screen.text = str(self.output_screen.text)[:-1]+str(instance.text)
        self.last_was_operator=None

    def trig(self, instance):
        try:
            if str(instance.text)=='sin':
                self.output_screen.text = str(math.sin(float(self.output_screen.text)*math.pi/180))
            elif str(instance.text)=='cos':
                self.output_screen.text = str(math.cos(float(self.output_screen.text)*math.pi/180))
            elif str(instance.text)=='tan':
                self.output_screen.text = str(math.tan(float(self.output_screen.text)*math.pi/180))
            elif str(instance.text)=='arcsin':
                self.output_screen.text = str(math.asin(float(self.output_screen.text))*180/math.pi)
            elif str(instance.text)=='arccos':
                self.output_screen.text = str(math.acos(float(self.output_screen.text))*180/math.pi)
            elif str(instance.text)=='arctan':
                self.output_screen.text = str(math.atan(float(self.output_screen.text))*180/math.pi)
        except ZeroDivisionError:
            self.output_screen.text = "cannot divide by zero!"
        except SyntaxError:
            self.output_screen.text = "invalid input!"
        except ValueError:
            self.output_screen.text = "invalid input!"
        except OverflowError:
            self.output_screen.text = "Overflow!"
        self.last_was_operator = "="

    def sqr(self, instance):
        try:
            self.equate(self)
            self.output_screen.text = str(float(self.output_screen.text)**2)
        except ZeroDivisionError:
            self.output_screen.text = "cannot divide by zero!"
        except SyntaxError:
            self.output_screen.text = "invalid input!"
        except ValueError:
            self.output_screen.text = "invalid input!"
        except OverflowError:
            self.output_screen.text = "Overflow!"
        self.last_was_operator="="

    def sqrt(self, instance):
        try:
            self.equate(self)
            self.output_screen.text = str(float(self.output_screen.text)**0.5)
        except ZeroDivisionError:
            self.output_screen.text = "cannot divide by zero!"
        except SyntaxError:
            self.output_screen.text = "invalid input!"
        except ValueError:
            self.output_screen.text = "invalid input!"
        except OverflowError:
            self.output_screen.text = "Overflow!"
        self.last_was_operator="="

    def pi(self, instance):
        if self.last_was_operator == "=":
            self.output_screen.text = '0'
        if str(self.output_screen.text)=='0':
            self.output_screen.text = str(math.pi)
        elif str(self.output_screen.text)[-1]=='0' and str(self.output_screen.text)[-2] in self.operators:
            self.output_screen.text = str(self.output_screen.text)[:-1]+str(math.pi)
        elif str(self.output_screen.text)[-1] in ['1','2','3','4','5','6','7','8','9']:
            self.output_screen.text = str(self.output_screen.text)+'*'+str(math.pi)
        else:
            self.output_screen.text = str(self.output_screen.text)+str(math.pi)
        self.last_was_operator="pi"

    def equate(self, instance):
        try:
            self.output_screen.text = str(eval(str(self.output_screen.text)))
        except ZeroDivisionError:
            self.output_screen.text = "cannot divide by zero!"
        except SyntaxError:
            self.output_screen.text = "invalid input!"
        except ValueError:
            self.output_screen.text = "invalid input!"
        except OverflowError:
            self.output_screen.text = "Overflow!"
        self.last_was_operator = "="

    def tenpowerx(self, instance):
        try:
            self.equate(self)
            self.output_screen.text = str(10**float(self.output_screen.text))
        except ZeroDivisionError:
            self.output_screen.text = "cannot divide by zero!"
        except SyntaxError:
            self.output_screen.text = "invalid input!"
        except ValueError:
            self.output_screen.text = "invalid input!"
        except OverflowError:
            self.output_screen.text = "Overflow!"
        self.last_was_operator="="

    def epowerx(self, instance):
        try:
            self.equate(self)
            self.output_screen.text = str(math.e**float(self.output_screen.text))
        except ZeroDivisionError:
            self.output_screen.text = "cannot divide by zero!"
        except SyntaxError:
            self.output_screen.text = "invalid input!"
        except ValueError:
            self.output_screen.text = "invalid input!"
        except OverflowError:
            self.output_screen.text = "Overflow!"
        self.last_was_operator="="

    def logarithm(self ,instance):
        try:
            self.equate(self)
            self.output_screen.text = str(math.log(float(self.output_screen.text)))
        except ZeroDivisionError:
            self.output_screen.text = "cannot divide by zero!"
        except SyntaxError:
            self.output_screen.text = "invalid input!"
        except ValueError:
            self.output_screen.text = "invalid input!"
        except OverflowError:
            self.output_screen.text = "Overflow!"
        self.last_was_operator="="

    def gif(self ,instance):
        try:
            self.equate(self)
            self.output_screen.text = str(math.floor(float(self.output_screen.text)))
        except ZeroDivisionError:
            self.output_screen.text = "cannot divide by zero!"
        except SyntaxError:
            self.output_screen.text = "invalid input!"
        except ValueError:
            self.output_screen.text = "invalid input!"
        except OverflowError:
            self.output_screen.text = "Overflow!"
        self.last_was_operator="="

    def fact(self, instance):
        try:
            self.equate(self)
            self.output_screen.text = str(math.gamma(float(self.output_screen.text)+1))
        except ZeroDivisionError:
            self.output_screen.text = "cannot divide by zero!"
        except SyntaxError:
            self.output_screen.text = "invalid input!"
        except ValueError:
            self.output_screen.text = "invalid input!"
        except OverflowError:
            self.output_screen.text = "Overflow!"
        self.last_was_operator="="

#build class and app run
class MainApp(App):
    def build(self):
        return MyGrid()       

if __name__=='__main__':
    MainApp().run()
