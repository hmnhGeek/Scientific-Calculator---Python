from Tkinter import *
from math import *
import os

root = Tk()
root.title("Scientific Calculator")
root.state('zoomed')
root.iconbitmap('calculator.ico')

E = Entry(root)
E.pack()
E.place(x = 560, y = 2)

secL = Label(root)
secL.pack()
secL.place(x = 600, y = 25)


L = Label(root)
L.pack()
L.place(x = 600, y = 48)

Lresult = Label(root, text = 'expression1')
Lresult.pack()
Lresult.place(x = 400, y = 2)

new = Label(root)
new.pack()
new.place(x = 600, y = 65)

secLresult = Label(root, text = 'expression2')
secLresult.pack()
secLresult.place(x = 400, y = 25)

res1 = Label(root, text = 'expression2 = ')
res1.pack()
res1.place(x = 400, y = 65)

res2 = Label(root, text = 'expression1 = ')
res2.pack()
res2.place(x = 400, y = 48)

storing = ' '
plusminusstatus = False

def display():
    f = open("About.txt", 'r')
    s = f.read()
    f.close()
    rev = Tk()
    rev.title("About")
    rev.iconbitmap('calculator.ico')
    scrollbar = Scrollbar(rev)
    scrollbar.pack(side = RIGHT, fill = Y)
    area = Text(rev, yscrollcommand = scrollbar.set)
    area.pack()
    area.insert(END, s)
    scrollbar.config(command = area.yview)
    rev.resizable(height = FALSE, width = FALSE)
    rev.mainloop()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="About", command=display)
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

def populate():
    c = 'null'
    d = 'null'
    try:
        if E.get() == '':
            pass
        else:
            myexpr = eval(E.get())
            c = myexpr
            L.config(text = myexpr)
        
    except:
        L.config(text = "<Error>")

    try:
        if secL['text'] == '':
            pass
        else:
            secondExp = eval(secL['text'])
            d = secondExp
            new.config(text = secondExp)
    
    except:
        new.config(text = "<Error>")

    f = open('history.txt', 'a')
    f.write(E.get()+' = '+str(c)+'\n')
    f.write(secL['text']+' = '+str(d)+'\n')
    f.write('-----------------------------------------------------------\n')
    f.close()

def ce():
    global storing
    global plusminusstatus
    L.config(text = ' ')
    secL.config(text = ' ')
    new.config(text = ' ')
    E.delete(0, END)
    #Lresult.config(text = ' ')
    #secLresult.config(text = ' ')
    storing = ' '
    plusminusstatus = False

def enter1():
    global storing
    mystr = secL['text']
    mystr+=str(1)
    secL.config(text = mystr)
    temp = ''
    for i in range(-1, -len(mystr)-1, -1):
        if mystr[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
            temp+=mystr[i]
        else:
            break
    storing = temp[-1:-len(temp)-1:-1]
    #print storing

def enter2():
    global storing
    mystr = secL['text']
    mystr+=str(2)
    secL.config(text = mystr)
    temp = ''
    for i in range(-1, -len(mystr)-1, -1):
        if mystr[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
            temp+=mystr[i]
        else:
            break
    storing = temp[-1:-len(temp)-1:-1]
    #print storing

def enter3():
    global storing
    mystr = secL['text']
    mystr+=str(3)
    secL.config(text = mystr)
    temp = ''
    for i in range(-1, -len(mystr)-1, -1):
        if mystr[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
            temp+=mystr[i]
        else:
            break
    storing = temp[-1:-len(temp)-1:-1]
    #print storing

def enter4():
    global storing
    mystr = secL['text']
    mystr+=str(4)
    secL.config(text = mystr)
    temp = ''
    for i in range(-1, -len(mystr)-1, -1):
        if mystr[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
            temp+=mystr[i]
        else:
            break
    storing = temp[-1:-len(temp)-1:-1]
    #print storing

def enter5():
    global storing
    mystr = secL['text']
    mystr+=str(5)
    secL.config(text = mystr)
    temp = ''
    for i in range(-1, -len(mystr)-1, -1):
        if mystr[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
            temp+=mystr[i]
        else:
            break
    storing = temp[-1:-len(temp)-1:-1]
    #print storing
def enter6():
    global storing 
    mystr = secL['text']
    mystr+=str(6)
    secL.config(text = mystr)
    temp = ''
    for i in range(-1, -len(mystr)-1, -1):
        if mystr[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
            temp+=mystr[i]
        else:
            break
    storing = temp[-1:-len(temp)-1:-1]
    #print storing
def enter7():
    global storing
    mystr = secL['text']
    mystr+=str(7)
    secL.config(text = mystr)
    temp = ''
    for i in range(-1, -len(mystr)-1, -1):
        if mystr[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
            temp+=mystr[i]
        else:
            break
    storing = temp[-1:-len(temp)-1:-1]
    #print storing
def enter8():
    global storing
    mystr = secL['text']
    mystr+=str(8)
    secL.config(text = mystr)
    temp = ''
    for i in range(-1, -len(mystr)-1, -1):
        if mystr[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
            temp+=mystr[i]
        else:
            break
    storing = temp[-1:-len(temp)-1:-1]
    #print storing
def enter9():
    global storing
    mystr = secL['text']
    mystr+=str(9)
    secL.config(text = mystr)
    temp = ''
    for i in range(-1, -len(mystr)-1, -1):
        if mystr[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
            temp+=mystr[i]
        else:
            break
    storing = temp[-1:-len(temp)-1:-1]
    #print storing
def enter0():
    global storing
    mystr = secL['text']
    mystr+=str(0)
    secL.config(text = mystr)
    temp = ''
    for i in range(-1, -len(mystr)-1, -1):
        if mystr[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
            temp+=mystr[i]
        else:
            break
    storing = temp[-1:-len(temp)-1:-1]
    #print storing
    

def enterplus():
    global storing
    mystr = secL['text']
    mystr+='+'
    secL.config(text = mystr)
    storing = '+'

def enterminus():
    global storing
    mystr = secL['text']
    mystr+='-'
    secL.config(text = mystr)
    #storing = '-'
    
def entermul():
    global storing
    mystr = secL['text']
    mystr+='*'
    secL.config(text = mystr)
    #storing = '*'
    
def enterdiv():
    global storing
    mystr = secL['text']
    mystr+='/'
    secL.config(text = mystr)
    #storing = '/'
    
def enterleft():
    global storing
    mystr = secL['text']
    mystr+='('
    secL.config(text = mystr)
    #storing = '('

def enterright():
    global storing
    mystr = secL['text']
    mystr+=')'
    secL.config(text = mystr)
    #storing = ')'

def entercmp():
    global storing
    mystr = secL['text']
    mystr+='j'
    secL.config(text = mystr)
    #storing = 'j'
    temp = ''
    for i in range(-1, -len(mystr)-1, -1):
        if mystr[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'j', '.']:
            temp+=mystr[i]
        else:
            break
    storing = temp[-1:-len(temp)-1:-1]
   # print storing

def backspace():
    global storing
    mystr = secL['text']
    mystr = mystr[0:len(mystr)-1]
    secL.config(text = mystr)
    #storing = ' '


def sqroot():
    
    mystr = secL['text']
    
    mystr += 'sqrt('
    secL.config(text = mystr)

def plusminus():
    global storing
    global plusminusstatus
    #print plusminusstatus
    mystr = secL['text']
    
    if mystr[-1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'j', 'i', 'e']:
        if not plusminusstatus:
            mystr = mystr.rstrip(storing)
            mystr += '(-'+storing+')'
            secL.config(text = mystr)
            plusminusstatus = True
        else:
            
            for i in range(-1, -len(mystr)-1, -1):
                if mystr[i] is ')':
                    init = i
                elif mystr[i] is '(':
                    terminate = i
                    break
            mystr = mystr[0:len(mystr)+terminate]
            mystr+=storing
            secL.config(text = mystr)
            plusminusstatus = False
            
    else:
        if not plusminusstatus:
            pass
        else:
            for i in range(-1, -len(mystr)-1, -1):
                if mystr[i] is ')':
                    init = i
                elif mystr[i] is '(':
                    terminate = i
                    break
            mystr = mystr[0:len(mystr)+terminate]
            mystr+=storing
            secL.config(text = mystr)
            plusminusstatus = False

def dot():
    global storing
    mystr = secL['text']
    mystr+='.'
    secL.config(text = mystr)
    temp = ''
    for i in range(-1, -len(mystr)-1, -1):
        if mystr[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', 'pi', 'e']:
            temp+=mystr[i]
        else:
            break
    storing = temp[-1:-len(temp)-1:-1]

def power():
    mystr = secL['text']
    mystr+='**'
    secL.config(text = mystr)
    
def pie():
    global storing
    mystr = secL['text']
    mystr+='pi'
    secL.config(text = mystr)
    storing = 'pi'

def Sin():
    
    mystr = secL['text']
    mystr+='sin('
    secL.config(text = mystr)

def Cos():
    
    mystr = secL['text']
    mystr+='cos('
    secL.config(text = mystr)

def Tan():
    
    mystr = secL['text']
    mystr+='tan('
    secL.config(text = mystr)
  
def arcsin():
    
    mystr = secL['text']
    mystr+='asin('
    secL.config(text = mystr)

def arccos():
    
    mystr = secL['text']
    mystr+='acos('
    secL.config(text = mystr)

def arctan():
    
    mystr = secL['text']
    mystr+='atan('
    secL.config(text = mystr)

def rads():
    
    mystr = secL['text']
    mystr+='radians('
    secL.config(text = mystr)

def degs():
    
    mystr = secL['text']
    mystr+='degrees('
    secL.config(text = mystr)

def imag():
    mystr = secL['text']
    mystr+='.imag'
    secL.config(text = mystr)
def real():
    mystr = secL['text']
    mystr+='.real'
    secL.config(text = mystr)

def conj():
    mystr = secL['text']
    mystr+='.conjugate()'
    secL.config(text = mystr)

def magnitude(cmpno):

    re = eval(str(cmpno)+'.real')
    im = eval(str(cmpno)+'.imag')

    return sqrt((re**2)+(im**2))

def mag():

    mystr = secL['text']
    mystr+='magnitude('
    secL.config(text = mystr)

def pol(cmpno):
    magn = magnitude(cmpno)
    re = eval(str(cmpno)+'.real')
    im = eval(str(cmpno)+'.imag')
    angle = degrees(atan(im/re))
    return "r = "+str(magn)+', theta = '+str(angle)

def polar():
    mystr = secL['text']
    mystr+='pol('
    secL.config(text = mystr)

def rec(r, theta):
    
    x = r*cos(theta)
    y = r*sin(theta)
    return str(x)+'+'+str(y)+'j'

def rectangular():
    mystr = secL['text']
    mystr+='rec('
    secL.config(text = mystr)

def comma():
    mystr = secL['text']
    mystr+=','
    secL.config(text = mystr)

def Log():
    mystr = secL['text']
    mystr+='log('
    secL.config(text = mystr)

def const_e():
    mystr = secL['text']
    mystr+='e'
    secL.config(text = mystr)
    global storing
    storing = 'e'

def factorial(n):

    fac = 1
    while n<>0:
        fac*=n
        n-=1
    return fac

def fact():
    mystr = secL['text']
    mystr+='factorial('
    secL.config(text = mystr)

def antilog(n, base):
    return base**n
def anti():
    mystr = secL['text']
    mystr+='antilog('
    secL.config(text = mystr)

def history():
    rev = Tk()
    rev.title("History")
    rev.iconbitmap('calculator.ico')
    scrollbar = Scrollbar(rev)
    scrollbar.pack(side = RIGHT, fill = Y)
    area = Text(rev, yscrollcommand = scrollbar.set)
    area.pack()
    f = open('history.txt', 'r')
    s = f.read()
    f.close()
    area.insert(END, s)
    scrollbar.config(command = area.yview)
    rev.resizable(height = FALSE, width = FALSE)
    rev.mainloop()

def histClr():
    os.remove('history.txt')
    f = open('history.txt', 'w')
    f.close()
    mystr = '--cleared--'
    secL.config(text = mystr)

b = Button(root, text = '=', command = populate, width = 5, bg = 'green', fg = 'black')
b.pack()
b.place(x = 550, y = 100)
ce = Button(root, text = 'C', command = ce, width = 5, bg = 'red')
ce.pack()
ce.place(x = 650, y = 310)
b1 = Button(root, text = '1', command = enter1, width = 5, bg = 'white')
b1.pack()
b1.place(x = 600, y = 100)
b2 = Button(root, text = '2', command = enter2, width = 5, bg = 'white')
b2.pack()
b2.place(x = 650, y = 100)
b3 = Button(root, text = '3', command = enter3, width = 5, bg = 'white')
b3.pack()
b3.place(x = 550, y = 130)
b4 = Button(root, text = '4', command = enter4, width = 5, bg = 'white')
b4.pack()
b4.place(x = 600, y = 130)
b5 = Button(root, text = '5', command = enter5, width = 5, bg = 'white')
b5.pack()
b5.place(x = 650, y = 130)
b6 = Button(root, text = '6', command = enter6, width = 5, bg = 'white')
b6.pack()
b6.place(x = 550, y = 160)
b7 = Button(root, text = '7', command = enter7, width = 5, bg = 'white')
b7.pack()
b7.place(x = 600, y = 160)
b8 = Button(root, text = '8', command = enter8, width = 5, bg = 'white')
b8.pack()
b8.place(x = 650, y = 160)
b9 = Button(root, text = '9', command = enter9, width = 5, bg = 'white')
b9.pack()
b9.place(x = 550, y = 190)
b0 = Button(root, text = '0', command = enter0, width = 5, bg = 'white')
b0.pack()
b0.place(x = 600, y = 190)
bleft = Button(root, text = '(', command = enterleft, width = 5, bg = 'white')
bleft.pack()
bleft.place(x = 650, y = 190)
bright = Button(root, text = ')', command = enterright, width = 5, bg = 'white')
bright.pack()
bright.place(x = 550, y = 220)
bcomma = Button(root, text = ',', command = comma, width = 5, bg = 'white', font = ('consolas',10))
bcomma.pack()
bcomma.place(x = 600, y = 220)
bcps = Button(root, text = '<--', command = backspace, width = 5, bg = 'white')
bcps.pack()
bcps.place(x = 650, y = 220)

bplus = Button(root, text = '+', command = enterplus, width = 5, bg = 'white', fg = 'orange', font = ('consolas',10))
bplus.pack()
bplus.place(x = 550, y = 250)
bminus = Button(root, text = '-', command = enterminus, width = 5, bg = 'white', fg = 'orange', font = ('consolas',10))
bminus.pack()
bminus.place(x = 600, y = 250)
bmul = Button(root, text = '*', command = entermul, width = 5, bg = 'white', fg = 'orange', font = ('consolas',10))
bmul.pack()
bmul.place(x = 650, y = 250)
bdiv = Button(root, text = '/', command = enterdiv, width = 5, bg = 'white', fg = 'orange', font = ('consolas',10))
bdiv.pack()
bdiv.place(x = 550, y = 280)
bsqrt = Button(root, text = 'sqroot', command = sqroot, width = 5, bg = 'white', fg = 'blue')
bsqrt.pack()
bsqrt.place(x = 650, y = 280)
bplusminus = Button(root, text = '+/-', command = plusminus, width = 5, bg = 'white', fg = 'blue', font = ('consolas',10))
bplusminus.pack()
bplusminus.place(x = 550, y = 310)
bdot = Button(root, text = '.', command = dot, width = 5, bg = 'white', fg = 'blue', font = ('consolas',10))
bdot.pack()
bdot.place(x = 600, y = 310)
bpow = Button(root, text = 'x^y', command = power, width = 5, bg = 'white', fg = 'blue')
bpow.pack()
bpow.place(x = 600, y = 280)
#----------------------------------------------------------------------------------------------------------------
newplate = Label(root, text = "Trigonometric functions")
newplate.pack()
newplate.place(x = 300, y = 360)

bsin = Button(root, text = 'sin', command = Sin, width = 5, bg = 'white', fg = 'blue')
bsin.pack()
bsin.place(x = 300, y = 390)
bcos = Button(root, text = 'cos', command = Cos, width = 5, bg = 'white', fg = 'blue')
bcos.pack()
bcos.place(x = 350, y = 390)
btan = Button(root, text = 'tan', command = Tan, width = 5, bg = 'white', fg = 'blue')
btan.pack()
btan.place(x = 400, y = 390)
basin = Button(root, text = 'arcsin', command = arcsin, width = 5, bg = 'white', fg = 'blue')
basin.pack()
basin.place(x = 300, y = 420)
bacos = Button(root, text = 'arccos', command = arccos, width = 5, bg = 'white', fg = 'blue')
bacos.pack()
bacos.place(x = 350, y = 420)
batan = Button(root, text = 'arctan', command = arctan, width = 5, bg = 'white', fg = 'blue')
batan.pack()
batan.place(x = 400, y = 420)
brad = Button(root, text = 'radians', command = rads, width = 5, bg = 'white', fg = 'blue')
brad.pack()
brad.place(x = 300, y = 450)
bdeg = Button(root, text = 'degrees', command = degs, width = 5, bg = 'white', fg = 'blue')
bdeg.pack()
bdeg.place(x = 350, y = 450)
bpi = Button(root, text = 'pi', command = pie, width = 5, bg = 'white', fg = 'blue')
bpi.pack()
bpi.place(x = 400, y = 450)
#--------------------------------------------------------------------------------------------------------------

complexPlate = Label(root, text = "Complex functions")
complexPlate.pack()
complexPlate.place(x = 570, y = 360)

bimg = Button(root, text = 'Img', command = imag, width = 5, bg = 'white', fg = 'red')
bimg.pack()
bimg.place(x = 550, y = 390)
breal = Button(root, text = 'Real', command = real, width = 5, bg = 'white', fg = 'red')
breal.pack()
breal.place(x = 600, y = 390)
bconj = Button(root, text = 'Conj', command = conj, width = 5, bg = 'white', fg = 'red')
bconj.pack()
bconj.place(x = 650, y = 390)
bmag = Button(root, text = 'Mag', command = mag, width = 5, bg = 'white', fg = 'red')
bmag.pack()
bmag.place(x = 550, y = 420)
bpolar = Button(root, text = 'Polar', command = polar, width = 5, bg = 'white', fg = 'red')
bpolar.pack()
bpolar.place(x = 600, y = 420)
brec = Button(root, text = 'Rect', command = rectangular, width = 5, bg = 'white', fg = 'red')
brec.pack()
brec.place(x = 650, y = 420)
bcmp = Button(root, text = 'j', command = entercmp, width = 5, bg = 'white', fg = 'red')
bcmp.pack()
bcmp.place(x = 600, y = 450)
#---------------------------------------------------------------------------------------------------------------

basicplate = Label(root, text = "Basic functions")
basicplate.pack()
basicplate.place(x = 840, y = 360)

blog = Button(root, text = 'LOG', command = Log, width = 5, bg = 'white', fg = 'orange')
blog.pack()
blog.place(x = 800, y = 390)
be = Button(root, text = 'e', command = const_e, width = 5, bg = 'white', fg = 'orange')
be.pack()
be.place(x = 850, y = 390)
bfact = Button(root, text = '!', command = fact, width = 5, bg = 'white', fg = 'orange')
bfact.pack()
bfact.place(x = 900, y = 390)
bantilog = Button(root, text = 'antilog', command = anti, width = 5, bg = 'white', fg = 'orange')
bantilog.pack()
bantilog.place(x = 850, y = 420)
#------------------------------------------------------------------------------------------------------------------

histplate = Label(root, text = 'History')
histplate.pack()
histplate.place(x = 600, y = 530)

bhist = Button(root, text = 'History', command = history, width = 5, bg = 'white', fg = 'orange')
bhist.pack()
bhist.place(x = 570, y = 560)
bclr = Button(root, text = 'Clear', command = histClr, width = 5, bg = 'white', fg = 'orange')
bclr.pack()
bclr.place(x = 630, y = 560)

root.resizable(height = FALSE, width = FALSE)
root.mainloop()
