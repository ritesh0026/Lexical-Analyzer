
#*****importing modules*****

import os
import re
import sys
from Tkinter import *
from PIL import ImageTk, Image

stack=[]
st={}
l=[]

#*****creating node*****

class node(object):
    def __init__(self):
        self.data_type=None
    def add(self,d):
        self.data_type=d
        
#*****creating symbol table*****
        
class symbol_table:
    def add1(self,x,v):    
        n=node()
        n.add(x)
        st[v]=n
        l.append(v)
    
    def display(self):
        j=len(l)
        for m in range(0,j):
            k=l[m]
            ob=st[k]
            print "Identifier: %s\t\t\tType: %s"%(k,ob.data_type)
            

    def lookup(self,ln):
            if len(stack)==0:
                return
            else:
                e1.error_invalid(ln)

#*****lexeme errors*****
                
class error:
    def error_multiple(self,ln):
        print "Error: Multiple declaration\tline no.: %d"%ln
        getch=raw_input()
        sys.exit(0)
    def error_invalid(self,ln):
        print "Error: Can't use keyword as identifier\tline no.: %d"%ln
        getch=raw_input()
        sys.exit(0)
    def error_declaration(self,ln):
        print "Error: Invalid declaration\tLine no.: %d"%ln
        getch=raw_input()
        sys.exit(0)


#*****File dialog*****

import tkFileDialog
def openfile():
    file_path=tkFileDialog.askopenfilename()
    if os.path.exists(file_path):
        f=open(file_path,'r')
        content=f.read()
        app.text.insert(0.0,content)

s1=symbol_table()
e1=error()
            
def lexical():
    pattern=re.compile("(#(.)*)|(\d{1,3})|(\d+(\w)+)|(\w*_*\w+)|(\"(.*)\")|op|(//(.)*)|(.)|(\s+)|((/\*)+(.)*)")
    scan=pattern.scanner(app.text.get(0.0,END))
    
    keywords=('auto','break','case','char','const','continue','default','do','double','else','enum','extern',
          'float','for','goto','if','int','long','register','return','short','signed','sizeof','static',
          'struct','switch','typedef','union','unsigned','void','volatile','while')
    data=('char','double','float','int','short','void')
    op=('+','-','*','/','%','++','--','?:')
    logical=('&&','||','!','&','|','^')
    rel=('==','!=','>','<','>=','<=')
    assi=('+=','=','-=','*=','/=','%=','&=','|=','^=')
    line=1
    flag=0
    
    i=0
    p=0

    temp=None

    while 1:
        m=scan.match()
        if not m:
            break
        lexeme=m.group(m.lastindex)
        if lexeme=='\n':
            line=line+1
            del stack[:]
            if i==1:
                e1.error_invalid(line)
                i=0;
            
        if m.lastindex==1:
            print lexeme + "\t\t//Header files"

    #*****operators*****
    
        elif m.lastindex==11:
            for word in op:
                if word==lexeme:
                    print lexeme + "\t\t//operator"
                    break
            for word in logical:
                if word==lexeme:
                    print lexeme + "\t\t//Logical operator"
                    break
            for word in rel:
                if word==lexeme:
                    print lexeme + "\t\t//Relational operator"
                    break
            for word in assi:
                if word==lexeme:
                    print lexeme + "\t\t//Assignment operator"
                    break
            if lexeme==';':
                i=0
                p=0
                temp=None
                del stack[:]
            if lexeme==',':
                if temp!=None:
                    i=1

    #*****Keyword/Identifiers*****    

        elif m.lastindex==6:
            for word in keywords:
                if word==lexeme:
                    s1.lookup(line)
                    for xyz in data:
                        if xyz==lexeme:
                            temp=lexeme
                        #i=1 when the comiler sees a data type
                            i=1
                            stack.append(lexeme)
                            break
                    flag=1
                    break
                elif i==1:
                    s1.add1(temp,lexeme)
                    i=0
                    p=0
            if flag:
                print lexeme + "\t\t//keyword"
                flag=0
            else:
                print lexeme + "\t\t//identifier"

    #*****numbers*****

        elif m.lastindex==3:
            print lexeme + "\t\t//number"

    #*****Literals*****

        elif m.lastindex==7:
            print lexeme + "\t\t//Literals"

    #*****Comments*****
        
        elif m.lastindex==7:
            print lexeme + "\t\t//comment"

        elif m.lastindex==3:
            e1.error_declaration(line)

#*****Total lines*****
    
    print "\n\nTotal lines: %d"%line

#*****Displaying symbol table*****

    print "\n\n\n*****Symbol table*****\n"
    print s1.display()
                
def close():
    exit()

class application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.widget()
    def widget(self):
        self.label=Label(self,text="Lexical Analyser" ,fg="white",bg="black",font=("@Adobe Fan Heiti Std B", 44))
        self.label.grid(row=0)
        self.text=Text(self,width=70,height=25,bg="seashell")
        self.text.grid(row=1)
        self.text.grid(padx=70,pady=20)
        self.button=Button(self,text="Analyse",command=lexical,fg="red",bg="lavender")
        self.button.grid(row=2,pady=5)
        self.label=Label(self,text="Team members :-\n\t\t\t\tRitesh Kumar Singh\n\t\t\t\tPrateek Vashist\n\t\t\t\tRahul Malhotra",fg="white", bg="black",font=("Courier", 8))
        self.label.grid(row=3)
#Creating Window
        
root=Tk()

#Modifying Window

root.title("Lexical analyser")
root.geometry("700x630")
root.configure(background='black')

#putting image in root window
#path = "secure.jpg"
#img = ImageTk.PhotoImage(Image.open(path))
#panel =Label(root, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")

menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="open",command=openfile)
filemenu.add_command(label="close",command=close)

menubar.add_cascade(label="File",menu=filemenu)

helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="About")
helpmenu.add_command(label="Developers")

menubar.add_cascade(label="Help",menu=helpmenu)
root.config(menu=menubar)


#Creating Frame
app=application(root)
app.configure(background="black",height=600)

root.mainloop()
