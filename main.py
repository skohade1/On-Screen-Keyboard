from tkinter import *
import ttkthemes as td 
from tkinter import ttk




global capital
capital =False

def select(key):
    b = key.widget
    value=b['text']
    if value == 'Space':
        textarea.insert(INSERT, ' ')
    
    elif value == 'Tab':
        textarea.insert(INSERT, '\t')

    elif value == 'Enter':
        textarea.insert(INSERT, '\n')

    elif value == 'Del':
        textarea.delete(1.0, END)

    elif value == 'Backspace':
        x = textarea.get(1.0, END)
        newtext=x[:-2]

        textarea.delete(1.0,END)
        textarea.insert(INSERT,newtext)
        
    elif value == 'Caps':
        buttoncapslock.grid_remove()
        buttonCAPSLOCK.grid()

        buttona.config(text='A')
        buttonb.config(text='B')
        buttonc.config(text='C')
        buttond.config(text='D')
        buttone.config(text='E')
        buttonf.config(text='F')
        buttong.config(text='G')
        buttonh.config(text='H')
        buttoni.config(text='I')
        buttonj.config(text='J')
        buttonk.config(text='K')
        buttonl.config(text='L')
        buttonm.config(text='M')
        buttonn.config(text='N')
        buttono.config(text='O')
        buttonp.config(text='P')
        buttonq.config(text='Q')
        buttonr.config(text='R')
        buttons.config(text='S')
        buttont.config(text='T')
        buttonu.config(text='U')
        buttonv.config(text='V')
        buttonw.config(text='W')
        buttonx.config(text='X')
        buttony.config(text='Y')
        buttonz.config(text='Z')


    elif value == 'CAPS':
        buttonCAPSLOCK.grid_remove()
        buttoncapslock.grid()

        buttona.config(text='a')
        buttonb.config(text='b')
        buttonc.config(text='c')
        buttond.config(text='d')
        buttone.config(text='e')
        buttonf.config(text='f')
        buttong.config(text='g')
        buttonh.config(text='h')
        buttoni.config(text='i')
        buttonj.config(text='j')
        buttonk.config(text='k')
        buttonl.config(text='l')
        buttonm.config(text='m')
        buttonn.config(text='n')
        buttono.config(text='o')
        buttonp.config(text='p')
        buttonq.config(text='q')
        buttonr.config(text='r')
        buttons.config(text='s')
        buttont.config(text='t')
        buttonu.config(text='u')
        buttonv.config(text='v')
        buttonw.config(text='w')
        buttonx.config(text='x')
        buttony.config(text='y')
        buttonz.config(text='z')

    else:
        textarea.insert(INSERT, value)


def Lshift():
    buttonapastrophy.grid_remove()
    button1.grid_remove()
    button2.grid_remove()
    button3.grid_remove()
    button4.grid_remove()
    button5.grid_remove()
    button6.grid_remove()
    button7.grid_remove()
    button8.grid_remove()
    button9.grid_remove()
    button0.grid_remove()
    buttonminus.grid_remove()
    buttonequalto.grid_remove()
    buttonopensqbrackets.grid_remove()
    buttonclosesqbracket.grid_remove()
    buttonforwardslash.grid_remove()
    buttonsemicolon.grid_remove()
    buttonsingleinverted.grid_remove()
    buttoncomma.grid_remove()
    buttonfullstop.grid_remove()
    buttonbackslash.grid_remove()



    buttontild.grid()
    buttonexclamation.grid()
    buttonattherate.grid()
    buttonhash.grid()
    buttondollar.grid()
    buttonpercent.grid()
    buttonpower.grid()
    buttonampresand.grid()
    buttonasterisk.grid()
    buttonopenparentheses.grid()
    buttoncloseparentheses.grid()
    buttonunderscore.grid()
    buttonplus.grid()
    buttonopenbrac.grid()
    buttonclosebrac.grid()
    buttoncolon.grid()
    buttondoubleinverted.grid()
    buttonlessthan.grid()
    buttongreaterthan.grid()
    buttonquestionmark.grid()



def Rshift():

    buttonapastrophy.grid()
    button1.grid()
    button2.grid()
    button3.grid()
    button4.grid()
    button5.grid()
    button6.grid()
    button7.grid()
    button8.grid()
    button9.grid()
    button0.grid()
    buttonminus.grid()
    buttonequalto.grid()
    buttonopensqbrackets.grid()
    buttonclosesqbracket.grid()
    buttonforwardslash.grid()
    buttonsemicolon.grid()
    buttonsingleinverted.grid()
    buttoncomma.grid()
    buttonfullstop.grid()
    buttonbackslash.grid()



    
    buttontild.grid_remove()
    buttonexclamation.grid_remove()
    buttonattherate.grid_remove()
    buttonhash.grid_remove()
    buttondollar.grid_remove()
    buttonpercent.grid_remove()
    buttonpower.grid_remove()
    buttonampresand.grid_remove()
    buttonasterisk.grid_remove()
    buttonopenparentheses.grid_remove()
    buttoncloseparentheses.grid_remove()
    buttonunderscore.grid_remove()
    buttonplus.grid_remove()
    buttonopenbrac.grid_remove()
    buttonclosebrac.grid_remove()
    buttoncolon.grid_remove()
    buttondoubleinverted.grid_remove()
    buttonlessthan.grid_remove()
    buttongreaterthan.grid_remove()
    buttonquestionmark.grid_remove()



    

root = td.ThemedTk()
root.get_themes()
root.set_theme('equilux')
root.title('On-Screen-Keyboard created by Saurabh Kohade')
root.config(bg="gray30")
root.resizable(0,0)

titlelabel=Label(root,text='On-Screen-Keyboard', font=("Helvetica", 20, "bold italic"),fg='white',bg='gray30')
titlelabel.grid(row=0,columnspan=40)
textarea=Text(root,font=('Times',15),height=10,width=100, wrap='word')
textarea.grid(row=1,columnspan=40)
textarea.focus_set()

keysframe=Frame(root,bg='gray30')
keysframe.grid(row=2)


buttonapastrophy=ttk.Button(keysframe,text='`',width=12)
buttonapastrophy.grid(row=0,column=0)
buttontild=ttk.Button(keysframe,text='~',width=12)
buttontild.grid(row=0,column=0)
buttontild.grid_remove()

button1=ttk.Button(keysframe, text='1',width=8)
button1.grid(row=0,column=1)
buttonexclamation=ttk.Button(keysframe, text='!',width=8)
buttonexclamation.grid(row=0,column=1)
buttonexclamation.grid_remove()

button2=ttk.Button(keysframe, text='2',width=8)
button2.grid(row=0,column=2)
buttonattherate=ttk.Button(keysframe, text='!',width=8)
buttonattherate.grid(row=0,column=2)
buttonattherate.grid_remove()

button3=ttk.Button(keysframe, text='3',width=8)
button3.grid(row=0,column=3)
buttonhash=ttk.Button(keysframe, text='#',width=8)
buttonhash.grid(row=0,column=3)
buttonhash.grid_remove()

button4=ttk.Button(keysframe, text='4',width=8)
button4.grid(row=0,column=4)
buttondollar=ttk.Button(keysframe, text='$',width=8)
buttondollar.grid(row=0,column=4)
buttondollar.grid_remove()

button5=ttk.Button(keysframe, text='5',width=8)
button5.grid(row=0,column=5)
buttonpercent=ttk.Button(keysframe, text='%',width=8)
buttonpercent.grid(row=0,column=5)
buttonpercent.grid_remove()

button6=ttk.Button(keysframe, text='6',width=8)
button6.grid(row=0,column=6)
buttonpower=ttk.Button(keysframe, text='^',width=8)
buttonpower.grid(row=0,column=6)
buttonpower.grid_remove()

button7=ttk.Button(keysframe, text='7',width=8)
button7.grid(row=0,column=7)
buttonampresand=ttk.Button(keysframe, text='&',width=8)
buttonampresand.grid(row=0,column=7)
buttonampresand.grid_remove()

button8=ttk.Button(keysframe, text='8',width=8)
button8.grid(row=0,column=8)
buttonasterisk=ttk.Button(keysframe, text='*',width=8)
buttonasterisk.grid(row=0,column=8)
buttonasterisk.grid_remove()

button9=ttk.Button(keysframe, text='9',width=8)
button9.grid(row=0,column=9)
buttonopenparentheses=ttk.Button(keysframe, text='(',width=8)
buttonopenparentheses.grid(row=0,column=9)
buttonopenparentheses.grid_remove()

button0=ttk.Button(keysframe, text='0',width=8)
button0.grid(row=0,column=10)
buttoncloseparentheses=ttk.Button(keysframe, text=')',width=8)
buttoncloseparentheses.grid(row=0,column=10)
buttoncloseparentheses.grid_remove()

buttonminus=ttk.Button(keysframe, text='-',width=8)
buttonminus.grid(row=0,column=11)
buttonunderscore=ttk.Button(keysframe, text='_',width=8)
buttonunderscore.grid(row=0,column=11)
buttonunderscore.grid_remove()

buttonequalto=ttk.Button(keysframe, text='=',width=8)
buttonequalto.grid(row=0,column=12)
buttonplus=ttk.Button(keysframe, text='+',width=8)
buttonplus.grid(row=0,column=12)
buttonplus.grid_remove()

buttonbackspace=ttk.Button(keysframe, text='Backspace',width=18)
buttonbackspace.grid(row=0,column=13)

buttontab=ttk.Button(keysframe, text='Tab',width=12)
buttontab.grid(row=1,column=0)
buttonq=ttk.Button(keysframe, text='q',width=8)
buttonq.grid(row=1,column=1)
buttonw=ttk.Button(keysframe, text='w',width=8)
buttonw.grid(row=1,column=2)
buttone=ttk.Button(keysframe, text='e',width=8)
buttone.grid(row=1,column=3)
buttonr=ttk.Button(keysframe, text='r',width=8)
buttonr.grid(row=1,column=4)
buttont=ttk.Button(keysframe, text='t',width=8)
buttont.grid(row=1,column=5)
buttony=ttk.Button(keysframe, text='y',width=8)
buttony.grid(row=1,column=6)
buttonu=ttk.Button(keysframe, text='u',width=8)
buttonu.grid(row=1,column=7)
buttoni=ttk.Button(keysframe, text='i',width=8)
buttoni.grid(row=1,column=8)
buttono=ttk.Button(keysframe, text='o',width=8)
buttono.grid(row=1,column=9)
buttonp=ttk.Button(keysframe, text='p',width=8)
buttonp.grid(row=1,column=10)

buttonopensqbrackets=ttk.Button(keysframe, text='[',width=8)
buttonopensqbrackets.grid(row=1,column=11)
buttonopenbrac=ttk.Button(keysframe, text='{',width=8)
buttonopenbrac.grid(row=1,column=11)
buttonopenbrac.grid_remove()


buttonclosesqbracket=ttk.Button(keysframe, text=']',width=8)
buttonclosesqbracket.grid(row=1,column=12)
buttonclosebrac=ttk.Button(keysframe, text='}',width=8)
buttonclosebrac.grid(row=1,column=12)
buttonclosebrac.grid_remove()

buttonbackslash=ttk.Button(keysframe, text='\\', width=18)
buttonbackslash.grid(row=1,column=13)
buttonbackslash=ttk.Button(keysframe, text='\\', width=18)
buttonbackslash.grid(row=1,column=13)
buttonbackslash.grid_remove()

buttoncapslock=ttk.Button(keysframe, text="Caps",width=12)
buttoncapslock.grid(row=2,column=0)
buttonCAPSLOCK=ttk.Button(keysframe, text="CAPS",width=12)
buttonCAPSLOCK.grid(row=2,column=0)
buttonCAPSLOCK.grid_remove()





buttona=ttk.Button(keysframe, text="a",width=8)
buttona.grid(row=2,column=1)
buttons=ttk.Button(keysframe, text="s",width=8)
buttons.grid(row=2,column=2)
buttond=ttk.Button(keysframe, text="d",width=8)
buttond.grid(row=2,column=3)
buttonf=ttk.Button(keysframe, text="f",width=8)
buttonf.grid(row=2,column=4)
buttong=ttk.Button(keysframe, text="g",width=8)
buttong.grid(row=2,column=5)
buttonh=ttk.Button(keysframe, text="h",width=8)
buttonh.grid(row=2,column=6)
buttonj=ttk.Button(keysframe, text="j",width=8)
buttonj.grid(row=2,column=7)
buttonk=ttk.Button(keysframe, text="k",width=8)
buttonk.grid(row=2,column=8)
buttonl=ttk.Button(keysframe, text="l",width=8)
buttonl.grid(row=2,column=9)

buttonsemicolon=ttk.Button(keysframe, text=";",width=8)
buttonsemicolon.grid(row=2 ,column=10)
buttoncolon=ttk.Button(keysframe, text=":",width=8)
buttoncolon.grid(row=2 ,column=10)
buttoncolon.grid_remove()

buttonsingleinverted=ttk.Button(keysframe, text=str("'"),width=8)
buttonsingleinverted.grid(row=2,column=11)
buttondoubleinverted=ttk.Button(keysframe, text=('"'),width=8)
buttondoubleinverted.grid(row=2,column=11)
buttondoubleinverted.grid_remove()

buttonenter=ttk.Button(keysframe, text='Enter',width=30)
buttonenter.grid(row=2,column=12, columnspan=40)


buttonlshift=ttk.Button(keysframe, text="Lshift",width=12,command=Lshift)
buttonlshift.grid(row=3,column=0)
buttonz=ttk.Button(keysframe, text="z",width=8)
buttonz.grid(row=3,column=1)
buttonx=ttk.Button(keysframe, text="x",width=8)
buttonx.grid(row=3,column=2)
buttonc=ttk.Button(keysframe, text="c",width=8)
buttonc.grid(row=3,column=3)
buttonv=ttk.Button(keysframe, text="v",width=8)
buttonv.grid(row=3,column=4)
buttonb=ttk.Button(keysframe, text="b",width=8)
buttonb.grid(row=3,column=5)
buttonn=ttk.Button(keysframe, text="n",width=8)
buttonn.grid(row=3,column=6)
buttonm=ttk.Button(keysframe, text="m",width=8)
buttonm.grid(row=3,column=7)
buttoncomma=ttk.Button(keysframe, text=",",width=8)
buttoncomma.grid(row=3,column=8)
buttonlessthan=ttk.Button(keysframe, text="<",width=8)
buttonlessthan.grid(row=3,column=8)
buttonlessthan.grid_remove()

buttonfullstop=ttk.Button(keysframe, text=".",width=8)
buttonfullstop.grid(row=3 ,column=9)
buttongreaterthan=ttk.Button(keysframe, text=">",width=8)
buttongreaterthan.grid(row=3 ,column=9)
buttongreaterthan.grid_remove()

buttonforwardslash=ttk.Button(keysframe, text=str( "/" ),width=8)
buttonforwardslash.grid(row=3,column=10)
buttonquestionmark=ttk.Button(keysframe, text=('?'),width=8)
buttonquestionmark.grid(row=3,column=10)
buttonquestionmark.grid_remove()
buttondelete=ttk.Button(keysframe, text="Del",width=8)
buttondelete.grid(row=3,column=11)

buttonrshift=ttk.Button(keysframe, text='Rshift',width=30,command=Rshift)
buttonrshift.grid(row=3,column=12, columnspan=40)

buttonspace=ttk.Button(keysframe, text='Space',width=50)
buttonspace.grid(row=4,column=0, columnspan=20)



buttontild.bind('<Button-1>',select)
buttonapastrophy.bind('<Button-1>',select)
button1.bind('<Button-1>',select)
buttonexclamation.bind('<Button-1>',select)
button2.bind('<Button-1>',select)
buttonattherate.bind('<Button-1>',select)
button3.bind('<Button-1>',select)
buttonhash.bind('<Button-1>',select)
button4.bind('<Button-1>',select)
buttondollar.bind('<Button-1>',select)
button5.bind('<Button-1>',select)
buttonpercent.bind('<Button-1>',select)
button6.bind('<Button-1>',select)
buttonpower.bind('<Button-1>',select)
button7.bind('<Button-1>',select)
buttonampresand.bind('<Button-1>',select)
button8.bind('<Button-1>',select)
buttonasterisk.bind('<Button-1>',select)
button9.bind('<Button-1>',select)
buttonopenparentheses.bind('<Button-1>',select)
button0.bind('<Button-1>',select)
buttoncloseparentheses.bind('<Button-1>',select)
buttonminus.bind('<Button-1>',select)
buttonunderscore.bind('<Button-1>',select)
buttonequalto.bind('<Button-1>',select)
buttonplus.bind('<Button-1>',select)
buttonbackspace.bind('<Button-1>',select)
buttontab.bind('<Button-1>',select)
buttonq.bind('<Button-1>',select)
buttonw.bind('<Button-1>',select)
buttone.bind('<Button-1>',select)
buttonr.bind('<Button-1>',select)
buttont.bind('<Button-1>',select)
buttony.bind('<Button-1>',select)
buttonu.bind('<Button-1>',select)
buttoni.bind('<Button-1>',select)
buttono.bind('<Button-1>',select)
buttonp.bind('<Button-1>',select)
buttonopensqbrackets.bind('<Button-1>',select)
buttonclosesqbracket.bind('<Button-1>',select)
buttonbackslash.bind('<Button-1>',select)
buttoncapslock.bind('<Button-1>',select)
buttonCAPSLOCK.bind('<Button-1>',select)
buttona.bind('<Button-1>',select)
buttons.bind('<Button-1>',select)
buttond.bind('<Button-1>',select)
buttonf.bind('<Button-1>',select)
buttong.bind('<Button-1>',select)
buttonh.bind('<Button-1>',select)
buttonj.bind('<Button-1>',select)
buttonk.bind('<Button-1>',select)
buttonl.bind('<Button-1>',select)
buttonsemicolon.bind('<Button-1>',select)
buttoncolon.bind('<Button-1>',select)
buttonsingleinverted.bind('<Button-1>',select)
buttondoubleinverted.bind('<Button-1>',select)
buttonenter.bind('<Button-1>',select)
buttonz.bind('<Button-1>',select)
buttonx.bind('<Button-1>',select)
buttonc.bind('<Button-1>',select)
buttonv.bind('<Button-1>',select)
buttonb.bind('<Button-1>',select)
buttonn.bind('<Button-1>',select)
buttonm.bind('<Button-1>',select)
buttonfullstop.bind('<Button-1>',select)
buttonlessthan.bind('<Button-1>',select)
buttongreaterthan.bind('<Button-1>',select)
buttoncomma.bind('<Button-1>',select)
buttonquestionmark.bind('<Button-1>',select)
buttonforwardslash.bind('<Button-1>',select)
buttonspace.bind('<Button-1>',select)
buttondelete.bind('<Button-1>',select)












root.mainloop()
