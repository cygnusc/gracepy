#!/usr/bin/env python3
from tkinter import *
from tkinter.filedialog import askopenfilename
import shutil

class LabeledEntry(object):
    def getVal(self):
        return self.e.get()

    def __init__(self, name, window, r, c = 1):
        #global position 
        self.label = Label(window, text=name).grid(row = r)
        self.e = Entry(window)
        self.e.insert(0, "0")
        self.e.grid(row=r, column=c)

class Simulation(object):
    def saveVals(self):
        global sims
        self.Data["totalTime"] = self.totalTime.getVal()
        self.Data["dt"] = self.dt.getVal()
        self.Data["Interval"] = self.Interval.getVal()
        self.Data["runID"] = self.runID.getVal()
        self.Data["algorithm"] = self.var.get()
        print ("Data = \n", self.Data)
        print ('appending to sims')
        sims.append(self)

    def __init__ (self, window, currPos = 0):
        self.pos = currPos
        self.window = window
        self.runID = LabeledEntry("simulation name", self.window, self.pos)
        self.totalTime = LabeledEntry("totalTime (ns)", self.window, self.pos + 1)
        self.dt = LabeledEntry("dt (ns)", self.window, self.pos + 2)
        self.Interval = LabeledEntry("output Interval / dt", self.window, self.pos + 3)
        self.dx = LabeledEntry("dx (nm)", self.window, self.pos + 4)
        self.dy = LabeledEntry("dy (nm)", self.window, self.pos + 5)
        self.dz = LabeledEntry("dz (nm)", self.window, self.pos + 6)
        Label(self.window, text="Choose an algorithm:").grid(row=self.pos + 7)
        self.var = StringVar(self.window)
        self.var.set('Euler')
        lst = ['Euler', 'Heun', 'RK4']
        self.algorithm = OptionMenu(self.window, self.var, *lst)
        self.algorithm.grid(row=self.pos + 7, column=1)
        self.Data = {}

class Rectangle(object):
    #def __init__(self, window, currPos):
    def saveVals(self):
        global rects
        self.Data["x0"] = self.x0.getVal()
        self.Data["y0"] = self.y0.getVal()
        self.Data["z0"] = self.z0.getVal()
        self.Data["x1"] = self.x1.getVal()
        self.Data["y1"] = self.y1.getVal()
        self.Data["z1"] = self.z1.getVal()
        self.Data["Mx0"] = self.Mx0.getVal()
        self.Data["My0"] = self.My0.getVal()
        self.Data["Mz0"] = self.Mz0.getVal()
        self.Data["alpha"] = self.alpha.getVal()
        self.Data["exch"] = self.exch.getVal()
        self.Data["H_anisX"] = self.H_anisX.getVal()
        self.Data["H_anisY"] = self.H_anisY.getVal()
        self.Data["H_anisZ"] = self.H_anisZ.getVal()
        rects.append(self)
        print ("1 Rect saved, curr No. of Rect(s):", len(rects))
        print ("Rect = \n", self.Data)

    def __init__(self, currPos):
        self.window = Tk()
        #self.window.geometry("300x500")
        self.window.title("Add a new Rectangle")
        self.pos = currPos
        rectGroup = LabelFrame(self.window, text="Rect Params", padx=5, pady=5)
        rectGroup.grid(row=0, column=1, padx=50, pady=50)
        self.x0 = LabeledEntry("x0 (nm)", rectGroup, self.pos)
        self.y0 = LabeledEntry("y0 (nm)", rectGroup, self.pos + 1)
        self.z0 = LabeledEntry("z0 (nm)", rectGroup, self.pos + 2)
        self.x1 = LabeledEntry("x1 (nm)", rectGroup, self.pos + 3)
        self.y1 = LabeledEntry("x1 (nm)", rectGroup, self.pos + 4)
        self.z1 = LabeledEntry("x1 (nm)", rectGroup, self.pos + 5)
        self.Mx0 = LabeledEntry("Mx0 (kA/m)", rectGroup, self.pos + 6)
        self.My0 = LabeledEntry("My0 (kA/m)", rectGroup, self.pos + 7)
        self.Mz0 = LabeledEntry("Mz0 (kA/m)", rectGroup, self.pos + 8)
        self.alpha = LabeledEntry("alpha", rectGroup, self.pos + 9)
        self.exch = LabeledEntry("exch (J/m)", rectGroup, self.pos + 10)
        self.H_anisX = LabeledEntry("H_anisX (kA/m)", rectGroup, self.pos + 11)
        self.H_anisY = LabeledEntry("H_anisY (kA/m)", rectGroup, self.pos + 12)
        self.H_anisZ = LabeledEntry("H_anisZ (kA/m)", rectGroup, self.pos + 13)
        self.Data = {}

        saveGroup = LabelFrame(self.window, text="", padx=5, pady=5)
        saveGroup.grid(row=self.pos + 14, column = 1, padx=50, pady=50)
        Button(saveGroup, text='Save & Return', command=self.closewindow).grid()
        Button(saveGroup, text='Cancel', command=self.window.withdraw).grid()
    def closewindow(self):
        self.saveVals()
        self.window.destroy()

class Field(object):
    #def __init__(self, window, currPos):
    def saveVals(self):
        global fields
        self.Data["Hx"] = self.Hx.getVal()
        self.Data["Hy"] = self.Hy.getVal()
        self.Data["Hz"] = self.Hz.getVal()
        self.Data["start"] = self.start.getVal()
        self.Data["peak"] = self.peak.getVal()
        self.Data["decay"] = self.decay.getVal()
        self.Data["end"] = self.end.getVal()
        fields.append(self)
        print ("1 Field saved, curr No. of Field(s):", len(fields))
        print ("Field = \n", self.Data)

    def __init__(self, currPos):
        self.window = Tk()
        #self.window.geometry("250x300")
        self.window.title("Add a new Field")
        self.pos = currPos
        fieldGroup = LabelFrame(self.window, text="Field Params", padx=5, pady=5)
        fieldGroup.grid(row=0, column=1, padx=50, pady=50)
        self.Hx = LabeledEntry("Hx", fieldGroup, self.pos + 1)
        self.Hy = LabeledEntry("Hy", fieldGroup, self.pos + 2)
        self.Hz = LabeledEntry("Hz", fieldGroup, self.pos + 3)
        self.start = LabeledEntry("startTime", fieldGroup, self.pos + 4)
        self.peak = LabeledEntry("peakTime", fieldGroup, self.pos + 5)
        self.decay = LabeledEntry("decayTime", fieldGroup, self.pos + 6)
        self.end = LabeledEntry("endTime", fieldGroup, self.pos + 7)
        self.Data = {}

        saveGroup = LabelFrame(self.window, text="", padx=5, pady=5)
        saveGroup.grid(row=self.pos+8, column=1, padx=50, pady=50)
        Button(saveGroup, text='Save & Return', command=self.closewindow).grid()
        Button(saveGroup, text='Cancel', command=self.window.withdraw).grid()
    def closewindow(self):
        self.saveVals()
        self.window.destroy()


def loadFileAndSave():
    fname = askopenfilename()
    print (fname)
    if fname == '':
        return
    shutil.copy2(fname, 'test.txt')

def createScriptAndSave():
    global sims
    newScriptWindow = Tk()
    #newScriptWindow.geometry("300x400")
    newScriptWindow.title("New Simulation")
    simGroup = LabelFrame(newScriptWindow, text="sim Params", padx=5, pady=5)
    simGroup.grid(row=0, column=0, padx=50, pady=50)
    sim = Simulation(simGroup)
    sims.append(sim)
    geoGroup = LabelFrame(newScriptWindow, text="Add Geometry", padx=5, pady=5)
    geoGroup.grid(row=10, column=0, padx=50, pady=50)
    Button(geoGroup, text='addRect', command=add_Rectangle).pack()
    Button(geoGroup, text='addField', command=add_Field).pack()
    saveGroup = LabelFrame(newScriptWindow, text="", padx=5, pady=5)
    saveGroup.grid(row=12, column=0, padx=50, pady=50)
    Button(saveGroup, text='Save & Run', command=save2File).pack()
    Button(saveGroup, text='Save & Quit', command=save2FileAndDeleteTest).pack()
    Button(saveGroup, text='Cancel', command=exit).pack()

rects = []
def add_Rectangle():
    r = Rectangle(2)

fields = []
def add_Field():
    f = Field(2)    

def save2File():
    global sims
    global rects
    global fields
    print ('in save2File()')
    print ('size of', len(sims))
    sims[0].saveVals()
    target=open("test.txt", 'w')
    target.write("***Simulation***\n")
    for key in sims[0].Data.keys(): # there should be only one sim instance
        print(key, sims[0].Data[key])
        target.write(key + " = " + sims[0].Data[key] + "\n")
    target.write("\n")

    for r in rects:
        target.write("***Rectangle***\n")
        for key in r.Data.keys():
            target.write(key + " = " + r.Data[key] + "\n")
        target.write("\n")

    for f in fields:
        target.write("***Field***\n")
        for key in f.Data.keys():
            target.write(key + " = " + f.Data[key] + "\n")
        target.write("\n")

    target.close()
    scriptName = sims[0].Data["runID"] + '.txt'
    shutil.copy2('test.txt', scriptName)
    exit()

def save2FileAndDeleteTest():
    save2File()
    open('test.txt','w')
    exit()
    
sims = []
welcome = Tk()
#welcome.geometry("400x200")
welcome.title("Grace")
group = LabelFrame(welcome, text="Choose an option", padx=5, pady=5)
group.pack(padx=50, pady=50)
Button(group, text='Run Existing Script', command=loadFileAndSave).pack()#.grid(row=1, column=1)
Button(group, text='Create New Script', command=createScriptAndSave).pack()#.grid(row=1, column=2)
mainloop()
