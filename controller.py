from __future__ import division
import time
import pyautogui as pyg 

class control:
    def __init__(self):
        self.des_roll=0.0
        self.des_pitch=0.0
        self.des_yaw=0.0
        self.des_xd=0.0
        self.des_yd=0.0
        self.des_zd=0.0
        self.des_rate=0.02
        self.dt=0.1
        self.prevrate=0
        self.starttime=time.time()
        self.dty=0.1
        self.prevratey=0
        self.starttimey=time.time()
        
    def calcerror(self, act_roll, act_pitch, act_yaw, act_xd, act_yd, act_zd, act_rate):
        self.error_roll= self.des_roll-act_roll
        self.error_pitch=self.des_pitch-act_pitch
        self.error_yaw=self.des_yaw-act_yaw
        self.error_xd=self.des_xd-act_xd
        self.error_yd=self.des_yd-act_yd
        self.error_zd=self.des_xd-act_zd
        self.error_rate=self.des_rate-act_rate
        return(self.error_roll,self.error_pitch,self.error_yaw,self.error_xd,self.error_yd,self.error_zd,self.error_rate)

    def rateupdater(Incbtn,Decbtn,rate):
        if(rate<0.05 and rate >-0.05):
            pass
        elif(rate>0.05):
            pyg.click(Incbtn)
        elif(rate<-0.05):
            pyg.click(Decbtn)

    def rateupdaterZ(Incbtn,Decbtn,rate):
        if(rate<0.2 and rate >-0.2):
            pass
        elif(rate<0.2):
            pyg.click(Incbtn)
        elif(rate>-0.2):
            pyg.click(Decbtn)

    def rateupdaterY(Incbtn,Decbtn,ratey):
        if(ratey<0.1 and ratey >-0.1):
            pass
        elif(ratey>0.1):
            pyg.click(Incbtn)
        elif(ratey<-0.1):
            pyg.click(Decbtn)

    def rateupdaterX(Incbtn,Decbtn,rate) :
        if(rate<0.05 and rate >-0.05):
            pass
        elif(rate>0.05):
            pyg.click(Incbtn)
        elif(rate<-0.05):
            pyg.click(Decbtn)

    def pitchcontrol( self, rate, pitchUpbtn, pitchDownbtn): 
        control.rateupdater(pitchUpbtn,pitchDownbtn,rate)
        if(self.error_pitch < 0 and abs(rate)<= 0.2):
            pyg.click(pitchDownbtn)        
        elif (self.error_pitch > 0) and (abs(rate) <= 0.2):
            pyg.click(pitchUpbtn)
        elif (self.error_pitch==0):
            pass

    def rollcontrol(self, rate, rollLeftbtn, rollRightbtn): 
        control.rateupdater(rollLeftbtn,rollRightbtn,rate)
        if(self.error_roll > 0 and abs(rate)<= 0.2):
            pyg.click(rollLeftbtn)        
        elif (self.error_roll < 0) and (abs(rate) <= 0.2):
            pyg.click(rollRightbtn)
        elif (self.error_roll==0):
            pass

    def yawcontrol(self, rate, yawLeftbtn, yawRightbtn): 
        control.rateupdater(yawLeftbtn,yawRightbtn,rate)
        if(self.error_yaw > 0 and abs(rate)<= 0.2):
            pyg.click(yawLeftbtn)        
        elif (self.error_yaw < 0) and (abs(rate) <= 0.2):
            pyg.click(yawRightbtn)
        elif (self.error_yaw==0):
            pass

    
    def xdcontrol(self, rate, translateForwardbtn, translateBackbtn): 
        control.rateupdaterX(translateForwardbtn,translateBackbtn,rate)
        if(self.error_xd < 0 and abs(rate)<= 0.1):
            pyg.click(translateForwardbtn)        
        elif (self.error_xd > 0) and (abs(rate) <= 0.03):
            pyg.click(translateBackbtn)
        elif (self.error_xd==0):
            pass

    def ydcontrol(self,translateLeftbtn, translateRightbtn): 
        self.dty=(time.time()-self.starttimey)
        ratey=(self.error_yd-self.prevratey)/self.dty
        print("Yrate: ",ratey)
        self.prevratey=self.error_yd
        self.starttimey=time.time()
        control.rateupdaterX(translateLeftbtn,translateRightbtn,ratey)
        if(self.error_yd < 0 and abs(ratey)<= 0.1):
            pyg.click(translateLeftbtn)        
        elif (self.error_yd > 0) and (abs(ratey) <= 0.1):
            pyg.click(translateRightbtn)
        elif (self.error_yd==0):
            pass

    def zdcontrol(self,translateUpbtn, translateDownbtn): 
        #ratex=Kp*(self.error_zd)+Kd*(self.error_zd)/self.dt 
        self.dt=(time.time()-self.starttime)
        rate=(self.error_zd-self.prevrate)/self.dt
        #print(rate)
        self.prevrate=self.error_zd
        self.starttime=time.time()
        control.rateupdaterZ(translateDownbtn,translateUpbtn,rate)
        if(self.error_zd < 0 and abs(rate)<= 0.2):
            pyg.click(translateDownbtn)        
        elif (self.error_zd > 0) and (abs(rate) <= 0.2):
            pyg.click(translateUpbtn)
        elif (self.error_zd==0):
            pass
    
