import math
import numpy as np
class MyCam(object):
    def __init__(self):
        self.rotationSense= None
        self.radius=None
        self.seqArray=None
        self.icorr=None
        self.currentRadius = None
        self.x = []
        self.y = []


    def set_rotationSense(self,rot):
        self.rotationSense = rot

    def set_radius(self,rad):
        self.radius = rad
        self.currentRadius=rad

    def set_SeqArray(self,array):
        self.seqArray=array
#icorr in seelf



    def execute_SHM(self,startangle, stopangle, displacement):
        k = float(self.currentRadius)
        for i in range(startangle+1,stopangle):
            deltatheta=i-startangle
            theta=startangle+deltatheta
            kdash = (displacement / 2) * (1 - (math.cos(math.radians((180 / (stopangle - startangle)) * deltatheta))))
            k = float(self.currentRadius) + kdash
            if self.rotationSense=='CW':
                self.x.append(-k*math.sin(math.radians(i)))
            if self.rotationSense=='CCW':
                self.x.append(k * math.sin(math.radians(i)))
            self.y.append( k * math.cos(math.radians(i)))
        self.currentRadius=k


    def execute_UV(self,startangle, stopangle, displacement):
        k = self.currentRadius
        for i in range(startangle+1,stopangle):
            deltatheta=i-startangle
            theta=startangle+deltatheta
            kdash = (displacement / (stopangle - startangle)) * deltatheta; #not checked
            k = self.currentRadius + kdash
            if self.rotationSense=='CW':
                self.x.append(-k*math.sin(math.radians(i)))
            if self.rotationSense=='CCW':
                self.x.append(k * math.sin(math.radians(i)))
            self.y.append( k * math.cos(math.radians(i)))
        self.currentRadius=k
        print(self.x)
        print(self.y)

    def execute_UARM(self,startangle, stopangle, displacement):
        k = self.currentRadius
        for i in range(startangle+1,stopangle):
            deltatheta=i-startangle
            theta=startangle+deltatheta
            if (deltatheta <= ((stopangle - startangle) / 2)):
                kdash = 2 * displacement * (deltatheta / (stopangle - startangle)) ^ 2   #not checked
            if (deltatheta > ((stopangle - startangle) / 2)):
                kdash = displacement - 2 * displacement * (1 - (deltatheta / (stopangle - startangle))) ^ 2   #not checked
            k = self.currentRadius + kdash
            if self.rotationSense=='CW':
                self.x.append(-k*math.sin(math.radians(i)))
            if self.rotationSense=='CCW':
                self.x.append(k * math.sin(math.radians(i)))
            self.y.append( k * math.cos(math.radians(i)))
        self.currentRadius=k
        print(self.x)
        print(self.y)

    def execute_cycloidal(self, startangle, stopangle, displacement):
        k = self.currentRadius
        for i in range(startangle + 1, stopangle):
            deltatheta = i - startangle
            theta = startangle + deltatheta
            kdash = (displacement / math.pi) * ((math.pi * i / (startangle - stopangle)) - (0.5 * math.sin(math.radians(360 * deltatheta / (startangle - stopangle)))))  #not checked
            k = self.currentRadius + kdash
            if self.rotationSense == 'CW':
                self.x.append(-k * math.sin(math.radians(i)))
            if self.rotationSense == 'CCW':
                self.x.append(k * math.sin(math.radians(i)))
            self.y.append(k * math.cos(math.radians(i)))
        self.currentRadius = k
        print(self.x)
        print(self.y)

    def execute_dwell(self, startangle, stopangle, displacement):
        k = self.currentRadius
        for i in range(startangle + 1, stopangle):
            deltatheta = i - startangle
            theta = startangle + deltatheta
            if self.rotationSense == 'CW':
                self.x.append(-k * math.sin(math.radians(i)))
            if self.rotationSense == 'CCW':
                self.x.append(k * math.sin(math.radians(i)))
            self.y.append(k * math.cos(math.radians(i)))
        self.currentRadius = k
        print(self.x)
        print(self.y)

    def master_executor(self):

        myseqarray=self.seqArray
        rows = int(myseqarray.size / 4)
        self.icorr=0
        startangle=0
        for i in range(1,rows):

            if myseqarray[i-1,0]=='Dwell':
                stopangle = startangle + int(myseqarray[i-1, 3])
                self.execute_dwell(startangle, stopangle)
                startangle = stopangle;
            else:
                if myseqarray[i-1,1]=='UV':
                    stopangle = startangle + int(myseqarray[i-1, 3])
                    if myseqarray[i-1,0]=='Rise':
                        displacement = int(myseqarray[i-1, 2])
                    if myseqarray[i-1,0]=='Fall':
                        displacement = -int(myseqarray[i-1, 2])
                    self.execute_UV(startangle, stopangle, displacement)
                    startangle = stopangle

                if myseqarray[i-1,1]=='SHM':
                    stopangle = startangle + int(myseqarray[i-1, 3])
                    if myseqarray[i-1,0]=='Rise':
                        displacement = int(myseqarray[i-1, 2])
                    if myseqarray[i-1,0]=='Fall':
                        displacement = -int(myseqarray[i-1, 2])
                    self.execute_SHM(startangle, stopangle, displacement)
                    print (self.x)
                    startangle = stopangle

                if myseqarray[i - 1, 1] == 'UARM':
                    stopangle = startangle + int(myseqarray[i-1, 3])
                    if myseqarray[i - 1, 0] == 'Rise':
                        displacement = int(myseqarray[i-1, 2])
                    if myseqarray[i - 1, 0] == 'Fall':
                        displacement = -int(myseqarray[i-1, 2])
                    self.execute_UARM(startangle, stopangle, displacement)
                    startangle = stopangle

                if myseqarray[i - 1, 1] == 'CYCLOIDAL':
                    stopangle = startangle + int(myseqarray[i-1, 3])
                    if myseqarray[i - 1, 0] == 'Rise':
                        displacement = int(myseqarray[i-1, 2])
                    if myseqarray[i - 1, 0] == 'Fall':
                        displacement = -int(myseqarray[i-1, 2])
                    self.execute_SHM(startangle, stopangle, displacement)
                    startangle = stopangle