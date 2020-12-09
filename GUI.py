import tkinter
import EDmain as ed
import BranchAndBound
import DivideAndConquer
import Dynamic

root= tkinter.Tk()

l1 = tkinter.Label(root, text="Input String S1")
l1.pack(anchor=tkinter.W)
e1 = tkinter.Entry(root, bd =5)
df= "dsghdsf"
e1.pack(anchor= tkinter.W)
s1= e1.get()
print (e1)
l1 = tkinter.Label(root, text="Input String S2")
l1.pack(anchor= tkinter.W)
e2 = tkinter.Entry(root, bd =5)
dsg= "efsdgfg"
e2.pack(anchor= tkinter.W)
s2=e2.get()
print (e2)


def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
var = tkinter.IntVar()
R1 = tkinter.Radiobutton(root, text="Branch and Bound Algorithm.", variable=var, value=1,
                  command=sel)
R1.pack(anchor= tkinter.W)

R2 = tkinter.Radiobutton(root, text="Divide And Conquer Algorithm.", variable=var, value=2,
                  command=sel)
R2.pack(anchor= tkinter.W)

R3 = tkinter.Radiobutton(root, text="Dynamic Algorithm.", variable=var, value=3,
                  command=sel)
R3.pack(anchor= tkinter.W)

L5 = tkinter.Label(root, text="Cost for Branch and Bound")
L5.pack(anchor= tkinter.W)
E5 = tkinter.Spinbox(root, from_=0 , to= 20, bd =5)
E5.pack(anchor=tkinter.W)

def selt():
   selection = "Value = " + str(var.get())
   label.config(text = selection)

var2 = tkinter.StringVar()
label = tkinter.Message( root, textvariable=var2, width=300 )


label.pack()
var3 = tkinter.StringVar()
label = tkinter.Message( root, textvariable=var3, width=300 )
   

def callback():
    if var.get()==1:
       
        result = BranchAndBound.branchAndBound(e1, e2,0,max(len(e1),len(e2)))
        var2.set("RUNNING TIME :%s seconds" % (result[0]))
        var3.set("{} {}".format("MINIMUM EDIT DISTANCE :", result[1]))
        var4.set(result[2])
        var5.set(result[3])
        var6.set(result[4])

    if var.get()==2:
    
        result1= DivideAndConquer.Hb(e1,e2)
        
        var4.set(result1[0])
        var5.set(result1[1])
        var6.set(result1[2])
        
    if var.get()==3:
        result = Dynamic.editDistDp(e1,e2)
        var2.set("RUNNING TIME :%s seconds" % result[0])
        var3.set("{} {}".format("MINIMUM EDIT DISTANCE :", result[1]))
        
B = tkinter.Button(root, text ="Compute.", command = callback)
B.pack()


label = tkinter.Label(root)
label.pack()
root.mainloop()