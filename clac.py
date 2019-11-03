from tkinter import*



#Calculator :

root=Tk()



#--------------Root and frame ::----------------------------
root.resizable(0,0)
root.option_add("*Entry.Background","light blue")
root.option_add("*Button.Background","light blue")
root.option_add("*Button.Font","arial,20,bold")


root.geometry("540x480")
root.title("Calculator")
root.configure(background="black")

numpad=Frame(root, width="400", height="600", background="black")
numpad.grid(row=1,column=0,pady=20,sticky="W",padx=35)

operator=Frame(root,width="150",height="350",background="black")
operator.grid(row=1,column=1,pady=20,padx=1)


#------------used Local and global Variable_______________

etext=StringVar()
equ=""


#--------------------Functions and Functions_____________________
def update(x):
    global equ
    equ=equ+x

def cb(r=1,c=0,t="num",s="W"):
    button=Button(numpad,text=t,relief=RIDGE,bd=4,
              width=7,font=("arial",15),command=lambda:[update(t),screen()])
    button.grid(row=r,column=c,sticky=s,padx=4,pady=5)




def ob(r=1,c=0,t="num",s="W"):
    button=Button(operator,text=t,relief=RIDGE,bd=4,
              width=7,font=("arial",15),command=lambda:[update(t),screen()])
    button.grid(row=r,column=c,sticky=s,padx=4,pady=5)

    
def screen():
    etext.set(equ)
    
    
def show():
    try:
        global equ
        equ=eval(equ)
        #equ=round(equ,4)
    
        equ=str(equ)
        etext.set(equ)
    except:
        etext.set("0")
        equ=""
    

def clean():
        global equ
        string2=""
        for x in range(len(equ)-1):
            string2=string2+equ[x]
        equ=string2


def empty():
    global equ
    equ=""
#--------------------------Buttons---------------------------------------


cb(1,0,"1")
cb(2,0,"4")
cb(3,0,"7")

cb(1,1,"2","W")
cb(2,1,"5","w")
cb(3,1,"8","W")

cb(1,2,"3")
cb(2,2,"6")
cb(3,2,"9")


ob(0,0,"+")
ob(1,0,"-")
ob(2,0,"*")
ob(3,0,"/")

cb(5,0,"(")
cb(5,1,")")
cb(5,2,"0")


cb(6,0,"<")
cb(6,1,">")
cb(6,2,".")



equal=Button(numpad,text="=",width=7,bd=4,
             relief=RIDGE,font=("arial",15),command=show)
equal.grid(row=7,column=0)


clear=Button(numpad,text="C",width=7,bd=4,font=("arial",15),
             relief=RIDGE,command=lambda:[clean(),screen()])
clear.grid(row=7,column=1)

empt=Button(numpad,text="CC",width=7,bd=4,font=("arial",15),
            relief=RIDGE,command=lambda:[empty(),screen()])
empt.grid(row=7,column=2)


entry=Entry(root,width=15,font=("arial",30),
            textvariable=etext,justify="right",state="normal")
entry.grid(row=0,column=0,pady=25,padx=30)




label=Label(root,text="©\nSANJAY SHAH",font=("arial",14),relief=FLAT,
            bg="black",fg="light blue")
label.grid(row=0,column=1)


deg_label=Label(root,text="......................................................",relief=FLAT
                ,bg="black",fg="red",font=("arial 15"))
deg_label.grid(row=2,column=0,sticky="W")


#.....KeyBoard..........Binding

def set_key(key="1"):
    root.bind(key,lambda x:[update(key),screen()])

set_key("1")
set_key("2")
set_key("3")
set_key("4")
set_key("5")
set_key("6")
set_key("7")
set_key("8")
set_key("9")
set_key("0")

set_key("+")
set_key("-")
set_key("*")
set_key("/")

set_key("(")
set_key(")")
set_key(".")

root.bind("<Return>",lambda x:[show()])
root.bind("<BackSpace>",lambda x:[clean(),screen()])
root.mainloop()



