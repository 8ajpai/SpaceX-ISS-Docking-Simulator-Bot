'''
SpaceX Crew Dragon Simulator (ISS Docking) Autopilot Bot
@author=Utkarsh Bajpai
'''
# -*- coding: utf-8 -*-
from selenium import webdriver
import pyautogui as pyg 
import time
import controller
from lxml import html 

############################################################################################################################################
## Define pixel values of various buttons

#rpy                                                
rollLeftbtn = (1598,553)       #roll Left
rollRightbtn = (1788,550)       #roll Right
pitchDownbtn = (1694,961)      #pitch Down
pitchUpbtn = (1693,674)      #pitch Up
yawLeftbtn = (1541,806)        #yaw Left
yawRightbtn = (1848,816)        #yaw Right
#xyz
translateUpbtn = (220,667)      #translate Up
translateDownbtn = (224,959)      #translate Down
translateLeftbtn = (69,807)      #translateLeft
translateRightbtn = (378,807)       #translateRight
translateForwardbtn = (318,556)     #translateForward
translateBackbtn = (130,556)        #translateBack
#precision
translationp = (224,806)   #Translation Precision
rotationp = (1694,806)      #Rotation Precision

#############################################################################################################################################


class sim:      

    #functions
    def getstate(driver):
        source = driver.page_source
        tree = html.fromstring(source)
#pitch
        for i in tree.xpath('//*[@id="pitch"]/div[1]'):
            #pitchangle = i.text
            pitchangle=float(i.text.rstrip('°'))
            #print("Pitch Angle : ", pitchangle)
        for i in tree.xpath('//*[@id="pitch"]/div[2]'):
            pitchrate=float(i.text.rstrip('°/s'))
            #print("Pitch Rate : ", pitchrate)
#roll
        for i in tree.xpath('//*[@id="roll"]/div[1]'):
            rollangle=float(i.text.rstrip('°'))
            #print("Roll Angle : ",rollangle)
        for i in tree.xpath('//*[@id="roll"]/div[2]'):
            rollrate=float(i.text.rstrip('°/s'))
            #print("Roll Rate : ",rollrate)
#yaw
        for i in tree.xpath('//*[@id="yaw"]/div[1]'):
            yawangle=float(i.text.rstrip('°'))
            #print("Yaw Angle : ", yawangle)
        for i in tree.xpath('//*[@id="yaw"]/div[2]'):
            yawrate=float(i.text.rstrip('°/s'))
            #print("Yaw Rate : ", yawrate)
#X
        for i in tree.xpath('//*[@id="x-range"]/div'):
            #xdist=i.text
            xdist=float(i.text.rstrip(' m'))
            #print("X-Range : ",xdist)
#Y
        for i in tree.xpath('//*[@id="y-range"]/div'):
            #ydist=i.text
            ydist=float(i.text.rstrip(' m'))
            #print("Y-Range : ", ydist)
#Z
        for i in tree.xpath('//*[@id="z-range"]/div'):
            #zdist=i.text
            zdist=float(i.text.rstrip(' m'))
            #print("Z-Range : ",zdist)
#Rate
        for i in tree.xpath('//*[@id="rate"]/div[2]'):
            rate=float(i.text.rstrip(' m/s'))
            #print("Rate : ",rate)

    #    print("Pitch Angle :",pitchangle, "    Roll Angle :",rollangle, "   Yaw Angle :",yawangle, "   X-Range :",xdist, "   Y-Range :",ydist, "   Z-Range :",zdist, "   Rate :",rate )
        return(rollangle,rollrate,pitchangle,pitchrate,yawangle,yawrate,xdist,ydist,zdist,rate)
##############################################################################################################################################


def openpage():
    #Selenium
    url= ('https://iss-sim.spacex.com/')
    driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe") 
    driver.maximize_window()
    driver.get(url)

    #wait for page to load          
    time.sleep(17)
    begin=(961,665) #begin button
    pyg.click(begin)

    #wait for game to start
    time.sleep(10)
    return(driver)




def Main():
    print('SpaceX Crew Dragon Simulator (ISS Docking) Autopilot Bot')
    driver=openpage()
    c= controller.control() 
    while True:
        state=sim.getstate(driver)
        curr_roll=float(state[0])
        curr_rollrate=float(state[1])
        curr_pitch=float(state[2])
        curr_pitchrate=float(state[3])
        curr_yaw=float(state[4])
        curr_yawrate=float(state[5])
        curr_xd=float(state[6])
        curr_yd=float(state[7])
        curr_zd=float(state[8])
        curr_rate=float(state[9])
        
        
        c.calcerror(curr_roll,curr_pitch,curr_yaw,curr_xd,curr_yd,curr_zd,curr_rate)
        #controller.control.rollcontrol()
        c.pitchcontrol(curr_pitchrate,pitchUpbtn,pitchDownbtn)
        c.rollcontrol(curr_rollrate,rollLeftbtn,rollRightbtn)
        c.yawcontrol(curr_yawrate,yawLeftbtn,yawRightbtn)
        c.xdcontrol(curr_rate,translateForwardbtn,translateBackbtn)
        c.ydcontrol(translateLeftbtn,translateRightbtn)
        c.zdcontrol(translateUpbtn,translateDownbtn)

        #print("P :",curr_pitch , "      R :",curr_roll, "       Y :", curr_yaw )

    
Main()