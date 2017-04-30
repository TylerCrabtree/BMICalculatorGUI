import Tkinter
import tkMessageBox



top = Tkinter.Tk()
top.resizable(width=False, height=False)
top.minsize(width=375, height=200)
top.maxsize(width=50, height=200)

def helloCallBack():
   tkMessageBox.showinfo( "BMI",bmi)


def grab():
   print E1.get()
   print E2.get()
   E1int = float(E1.get())
   E2int= float(E2.get())
   bmi = E1int/E2int 
   var = bmi
   tkMessageBox.showinfo( "BMI",bmi)
   print bmi
  

a = Tkinter.Button(top, text ="Go", command = grab, bd=6, height = 10,padx = 50)
#b = Tkinter.Button(top, text ="2", command = helloCallBack,bd=6,pady = 10)

a.pack()
a.flash()


L1 = Tkinter.Label(top, text="Enter Weight (pounds)")
L2 = Tkinter.Label(top, text="Enter Height (inches)")


L1.pack( side = Tkinter.LEFT)
L2.pack( side = Tkinter.RIGHT)

E1 = Tkinter.Entry(top, bd =5 )
E1.pack(side = Tkinter.LEFT)

E2 = Tkinter.Entry(top, bd =5)
E2.pack(side = Tkinter.RIGHT)

a.place(x=200, y=5)
L1.place(x=10,y=5)
E1.place(x=10,y=25)
L2.place(x=10,y=55)
E2.place(x=10,y=75)



top.mainloop()