import sys
from pathlib import Path

from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar ) 
import numpy as np
# Define log
import logging as log 
log.basicConfig(format='[%(levelname)s]: %(message)s', level=log.INFO)

# Import the modules of my directory
from gui.fkgui_qt import *
from gui.mplwidget import MplWidget
from src.geolib import *

class application(Ui_MainWindow):
    def __init__(self, window):
        log.info("Initialization ")
        self.setupUi(window)

        self.initState()
        self.draw()
        self.labels1.setText("Joint 1 : "+str(self.hslider1.value())+u'\N{DEGREE SIGN}')
        self.labels2.setText("Joint 2 : "+str(self.hslider2.value())+u'\N{DEGREE SIGN}')
        self.labels3.setText("Joint 3 : "+str(self.hslider3.value())+u'\N{DEGREE SIGN}') 
        self.labels4.setText("Joint 4 : "+str(self.hslider4.value())+u'\N{DEGREE SIGN}') 
        self.labels5.setText("Joint 5 : "+str(self.hslider5.value())+u'\N{DEGREE SIGN}')
        self.labels6.setText("Joint 6 : "+str(self.hslider6.value())+u'\N{DEGREE SIGN}') 

        #process
        self.pushButton_reset.clicked.connect(self.initState)
        self.pushButton1.clicked.connect(self.clickMe)
        self.pushButton2.clicked.connect(self.clickMe)
        self.hslider1.valueChanged.connect(self.s1label)
        self.hslider2.valueChanged.connect(self.s2label)
        self.hslider3.valueChanged.connect(self.s3label)
        self.hslider4.valueChanged.connect(self.s4label)
        self.hslider5.valueChanged.connect(self.s5label)
        self.hslider6.valueChanged.connect(self.s6label)

    def initState(self):
        j1 = 0
        j2 = 0
        j3 = 0
        j4 = 0
        j5 = 0
        j6 = 0
        self.hslider1.setProperty("value", j1)
        self.hslider2.setProperty("value", j2)
        self.hslider3.setProperty("value", j3)
        self.hslider4.setProperty("value", j4)
        self.hslider5.setProperty("value", j5)
        self.hslider6.setProperty("value", j6)
        self.MplWidget.canvas.axes.view_init(20, -120)
        self.draw()

    def clickMe(self):
        print("hellow dunia")

    def showName1(self):
        self.label1.setText("indra agustian")

    def showName2(self):
        self.label1.setText("apa kabar??")

    def s1label(self):
        self.labels1.setText("Joint 1: "+str(self.hslider1.value())+u'\N{DEGREE SIGN}')
        self.draw()

    def s2label(self):
        self.labels2.setText("Joint 2: "+str(self.hslider2.value())+u'\N{DEGREE SIGN}')
        self.draw()

    def s3label(self):
        self.labels3.setText("Joint 3: "+str(self.hslider3.value())+u'\N{DEGREE SIGN}')
        self.draw()

    def s4label(self):
        self.labels4.setText("Joint 4: "+str(self.hslider4.value())+u'\N{DEGREE SIGN}')
        self.draw()

    def s5label(self):
        self.labels5.setText("Joint 5: "+str(self.hslider5.value())+u'\N{DEGREE SIGN}')
        self.draw()

    def s6label(self):
        self.labels6.setText("Joint 6: "+str(self.hslider6.value())+u'\N{DEGREE SIGN}')
        self.draw()

    def draw(self): 
        j1=self.hslider1.value()
        j2=self.hslider2.value()
        j3=self.hslider3.value()
        j4=self.hslider4.value()
        j5=self.hslider5.value()
        j6=self.hslider6.value()

        j= dh_parse(j1,j2,j3,j4,j5,j6)
        m = kinematics(j)
        Q = xyz_pos(m)
        
        X0, Y0, Z0 = Q[0, 0:3], Q[1, 0:3], Q[2, 0:3]
        X1, Y1, Z1 = Q[0, 1:4], Q[1, 1:4], Q[2, 1:4]
        X2, Y2, Z2 = Q[0, 2:4], Q[1, 2:4], Q[2, 2:4]
        X3, Y3, Z3 = Q[0, 3:5], Q[1, 3:5], Q[2, 3:5]
        X4, Y4, Z4 = Q[0, 4:6], Q[1, 4:6], Q[2, 4:6]
        X5, Y5, Z5 = Q[0, 5:6], Q[1, 5:6], Q[2, 5:6]
        X6, Y6, Z6 = Q[0, 6:6], Q[1, 6:6], Q[2, 6:6]

        self.MplWidget.canvas.axes.clear() 
        self.MplWidget.canvas.axes.plot (X1,Y1,Z1, color='green', marker='o', linestyle='solid', linewidth=5, markersize=10)
        self.MplWidget.canvas.axes.plot (X2,Y2,Z2, color='red', marker='o', linestyle='solid', linewidth=5, markersize=10)
        self.MplWidget.canvas.axes.plot (X3,Y3,Z3, color='blue', marker='o', linestyle='solid', linewidth=5, markersize=10)
        self.MplWidget.canvas.axes.plot (X4,Y4,Z4, color='goldenrod', marker='o', linestyle='solid', linewidth=5, markersize=10)
        self.MplWidget.canvas.axes.plot (X5,Y5,Z5, color='blue', marker='o', linestyle='solid', linewidth=5, markersize=10)
        self.MplWidget.canvas.axes.plot (X6,Y6,Z6, color='goldenrod', marker='o', linestyle='solid', linewidth=5, markersize=10)
        x5=X5[0]
        y5=Y5[0]
        z5=Z5[0]
        self.MplWidget.canvas.axes.text(x5, y5, z5,'({:.2f}, {:.2f}, {:.2f})'.format(x5,y5,z5), weight='bold', fontsize=12)
        
        self.MplWidget.canvas.axes.set_xlabel('x')
        self.MplWidget.canvas.axes.set_ylabel('y')
        self.MplWidget.canvas.axes.set_zlabel('z')
        
        self.MplWidget.canvas.axes.set_xlim([-3, 3])
        self.MplWidget.canvas.axes.set_ylim([-3, 3])
        self.MplWidget.canvas.axes.set_zlim([0, 2])
        
        self.MplWidget.canvas.draw() 


