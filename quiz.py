from tkinter import *
import random

root1 = Tk()
root1.title("Quiz Game")
root1.geometry("700x450")


def ex() :
    root1.destroy()

title = Label(root1,text="Welcome To the Quiz",font=("arial",50)).pack(padx=10,pady=(20,20))
bdy = Label(root1,text="This is a test to your knowledge",font=("arial",25)).pack(pady=(10,15))
tbut = Button(text="START",command=ex,bg="green",font=("Times",25)).pack(pady=(5,25))
rule1 = Label(root1,text="There will be 10 questions in this quiz.\nEach question is valued at 1 point.\nNO GOING BACK : Once a question is answered,that is the final answer.\nYour Score will be shown at the end of the quiz.",bg="black",fg="yellow",font=("arial",15),width=600).pack(pady=(68,0),anchor=S)

root1.mainloop()

root = Tk()
root.title("Quiz Game")
root.geometry("1300x700")
root.configure(background='skyblue')

tst =[{
'1':'The Binary system uses power of',
'2':'Who is the father of computer',
'3':'Which Penguin is the mascot of Linux Operating system',
'4':'A language which is close to that used within the computer is',
'5':'"OS" computer abbreviation usually means',
'6':'".jpeg" extension refers usually to what kind of file?',
'7':"''.MOV' extension refers usually to what kind of file?",
'8':'Which Indian state implemented "Cyber Grameen"',
'9':'Differentiation of Sin(x)',
'10':'"Oruma" is Linux based software development by',
'11':'GPS was developed by?',
'12':'Which famous web site was found by Jeffry Bezos',
'13':'What is three finger salutes?',
'14':'Longhorn was the code name of ?',
'15':'What is the extension of PDF?',
'16':'A computer program that converts assembly language to machine language is ',
'17':'The time required for the fetching and execution of one simple machine instruction is',
'18':'An optical input device that interprets pencil marks on paper media is',
'19':"Which IT company's nickname is ' The Big Blue ' ?",
'20':' One Gigabyte is approximately equal to:',
'21':'What type of process creates a smaller file that is faster to transfer over the internet?',
'22':'Which of the following is an example of non-volatile memory?',
'23':'The term referring to evacuating the content of some part of the machine is known as',
'24':'The hexadecimal number system consists of the symbols',
'25':'A microprocessor unit, a memory unit, and an input/output unit form a:',
'26':'An assembler is',
'27':'Which one is the first fully supported 64-bit Operating System',
'28':'The list of coded instructions is called',
'29':'A program that converts computer data into some code system other than the normal one is known as',
'30':'The first generation of computers available was based on the bit micro processors'
},
{
'1':['2','4','8'],
'2':['Steve Jobs','Charles Babbage','Bill Gates'],
'3':['Steve','Kowalski','Tux'],
'4':['High-level language','Assembly language','Low-level language'],
'5':['Operating System','Open Source','Optical Sensor'],
'6':['image','audio','video'],
'7':['Image File','Animation/Movie File','Audio File'],
'8':['Karnataka ','Tamil Nadu','Andhra Pradesh'],
'9':['Cotx','Tanx','Cosx'],
'10':['Kerala State Elecric Board','Karnataka Elecric Board','Tamil Nadu Elecric Board'],
'11':['Oracle','US Army','IBM'],
'12':['Reddit','Yahoo','Amazon'],
'13':['ctrl+alt+delete','a last ditch effort to save the pc','all of the above'],
'14':['windows xp','windows vista','windows 7'],
'15':['Portable Document Format','Printable Document Format','Private Document Format'],
'16':['Assembler','Compiler','Interpreter'],
'17':['Delay time','CPU cycle','Real time'],
'18':['O.M.R','Punch card reader','Optical scanners'],
'19':['IBM','Windows','Ocean Man'],
'20':['1000,000 bytes','1000,000,000 bytes','1000,000,000,000 bytes'],
'21':["Compression","Fragmentation","Encapsulation"],
'22':["RAM","LSI","ROM"],
'23':["Down",'Compiler','Dump'],
'24':['0-9,A-F','0-9,A-Z','0-8,A-F'],
'25':["CPU",'Microcomputer','ALU'],
'26':['Machine dependant','Software Dependant','Code Dependant'],
'27':["Windows","MacOS","Linux"],
'28':["Algorithm","Computer Program","Utility Program"],
'29':['Encoder','Emulator','Coding'],
'30':['4','8','64']
}]

q = [x for x in tst[0].values()]
opt=[x for x in tst[1].values()]
ans= [1,2,3,3,1,1,2,3,3,1,2,3,3,2,1,1,2,1,1,2,1,3,3,1,2,1,3,2,1,2]
ui = []
rval = IntVar()
ind = []

def gen():
    global ind
    while(len(ind) < 10):
        x = random.randint(0,29)
        if x in ind:
            continue
        else:
            ind.append(x)

def qcons(i) :
    global ifr
    ifr = Frame(root,bg="skyblue")
    ifr.pack(pady=(100,20))
    qlab = Label(ifr,text=q[ind[i]],font =("Times",25),width=100,bg="yellow").pack(pady=(52,20))
    r1 = Radiobutton(ifr,text = opt[ind[i]][0],value=1,variable=rval,font =("arial",15),bg="grey",width=25).pack(pady=3)
    r2 = Radiobutton(ifr,text = opt[ind[i]][1],value=2,variable=rval,font =("arial",15),bg="grey",width=25).pack(pady=3)
    r3 = Radiobutton(ifr,text = opt[ind[i]][2],value=3,variable=rval,font =("arial",15),bg="grey",width=25).pack(pady=3)
    nbut = Button(ifr,text="NEXT",command=lambda:select(i),bg="orange",font=('impact',30)).pack(pady=50)


def select(i) :
    r = rval.get()
    ui.append(r)
    rval.set(None)
    qchange(i)


def qchange(i) :
    if i+1 < 10 :
        i += 1
        ifr.destroy()
        qcons(i)
    else :
        ifr.destroy()
        test(0)

def test(a) :
    score = 0
    while a < 10 :
        if ui[a] == ans[ind[a]] :
            score += 1
        a += 1
    lbl1 = Label(root,text=("Your score is "+str(score)),font=("Arial Round Mt bold",20),bg="orange",fg="white",width=60)
    lbl1.pack(pady=(70,0))
    if score < 5 :
        Better = Label(root,text="You can do better ",font=("Arial Round Mt bold",20),bg="grey",fg="white",width=60).pack()
    elif score < 10 :
        good = Label(root,text="You did good ",font=("Arial Round Mt bold",20),bg="grey",fg="white",width=60).pack()
    else :
        perfect = Label(root,text="perfect you answered all the questions correctly.",font=("Arial Round Mt bold",20),bg="grey",fg="white",width=60).pack()
    creds = Label(root,text="This Quiz Program Was Created By :",font=("Castellar",25),bg="white",width=60).pack(pady=(69,0))
    ar = Label(root,text="Arpit Rai",font=("Harlow Solid Italic",30),bg="skyblue").pack()
    ap = Label(root,text="Abhishek Pagare",font=("Harlow Solid Italic",30),bg="skyblue").pack()
    av = Label(root,text="Achyut Verma",font=("Harlow Solid Italic",30),bg="skyblue").pack()
gen()
qcons(0)

root.mainloop()
