from vcScript import * 
import vcMatrix 
from vcHelpers.Robot2 import*
import time
import csv
comp = getComponent()
app=getApplication()
robot = app.findComponent("M-20iD/25")
controller = robot.findBehaviour("R-30iB")
joints = controller.Joints
dofs = [j.Dof for j in joints]
executor = robot.findBehaviour("Executor")
signal = comp.getBehaviour("Boolean Signal")
J1_RoboGuide = comp.getBehaviour("RealSignalJ1")
J2_RoboGuide = comp.getBehaviour("RealSignalJ2")
J3_RoboGuide = comp.getBehaviour("RealSignalJ3")
J4_RoboGuide = comp.getBehaviour("RealSignalJ4")
J5_RoboGuide = comp.getBehaviour("RealSignalJ5")
J6_RoboGuide = comp.getBehaviour("RealSignalJ6")
RB_Joints_SPD = comp.getBehaviour("RB_Joints_SPD")
#VC_counter = comp.getBehaviour("VC_counter")
#RB_counter = comp.getBehaviour("RB_counter")
VC_counter = comp.getProperty("Integer_VC")
RB_counter = comp.getProperty("Integer_RB")
VC_Joints_SPD = 5
RBMaxSpeedJ1 = comp.getBehaviour("RBMaxSpeedJ1")
RBMaxSpeedJ2 = comp.getBehaviour("RBMaxSpeedJ2")
RBMaxSpeedJ3 = comp.getBehaviour("RBMaxSpeedJ3")
RBMaxSpeedJ4 = comp.getBehaviour("RBMaxSpeedJ4")
RBMaxSpeedJ5 = comp.getBehaviour("RBMaxSpeedJ5")
RBMaxSpeedJ6 = comp.getBehaviour("RBMaxSpeedJ6")
Timer_pos = comp.getBehaviour("timer_pos")
#joints_speeds=[d.MaxSpeed for d in joints]
posJoints_P1 = [0, 0, 0, 10, 15, 25]
posJoints_P2 = [0, 7, -44, 3, 59, 33]
posJoints_P3 = [42, 28, -38, -43, 64, 70]
posJoints_P4 = [42, 26, 5, -73, 40, 115]
K = 0.1
def OnStart():
  joints[0].MaxSpeed = 410
  joints[1].MaxSpeed = 410
  joints[2].MaxSpeed = 520
  joints[3].MaxSpeed = 830
  joints[4].MaxSpeed = 830
  joints[5].MaxSpeed = 1430
def OnSignal(signal):
  if signal.Value==True:
    resumeRun()
  if signal.Value==False:
    suspendRun()
def OnRun():
  suspendRun()
  counter = 0
  counter_RB=0
  VC_counter.Value = counter
  RB_counter.Value = counter_RB
  P1_pos = True
  P2_pos = False
  P3_pos = False
  P4_pos = False
  P1_posRB = True
  P2_posRB = False
  P3_posRB = False
  P4_posRB = False
  Timer = True
  Timer_pos = comp.getBehaviour("timer_pos")
  Timer_pos.Value = False
  dT = 0
  while app.Simulation.IsRunning:
    joints_values=[d.VALUE for d in joints]
    #print(joints[5].VALUE)
    #print(joints_speeds[0])
    #print("skrypt 1", RB_counter.Value,VC_counter.Value)
    e = abs(RB_counter.Value-VC_counter.Value)
    print(VC_counter.Value,RB_counter.Value)
    if Timer == True and VC_counter.Value != RB_counter.Value:
      start=time.clock()
      Timer = False
    if VC_counter.Value == 1:
      TargetSpeedJ1=RBMaxSpeedJ1.Value*RB_Joints_SPD.Value/VC_Joints_SPD
      TargetSpeedJ2=RBMaxSpeedJ2.Value*RB_Joints_SPD.Value/VC_Joints_SPD
      TargetSpeedJ3=RBMaxSpeedJ3.Value*RB_Joints_SPD.Value/VC_Joints_SPD
      TargetSpeedJ4=RBMaxSpeedJ4.Value*RB_Joints_SPD.Value/VC_Joints_SPD
      TargetSpeedJ5=RBMaxSpeedJ5.Value*RB_Joints_SPD.Value/VC_Joints_SPD
      TargetSpeedJ6=RBMaxSpeedJ6.Value*RB_Joints_SPD.Value/VC_Joints_SPD
      #print(TargetSpeedJ1,TargetSpeedJ2,TargetSpeedJ3,TargetSpeedJ4,TargetSpeedJ5,TargetSpeedJ6)
    '''if (round(J1_RoboGuide.Value) == posJoints_P2[0] and  round(J2_RoboGuide.Value) == posJoints_P2[1] and  round(J3_RoboGuide.Value) == posJoints_P2[2] and round(J4_RoboGuide.Value) == posJoints_P2[3] and 
        round(J5_RoboGuide.Value) == posJoints_P2[4] and round(J6_RoboGuide.Value) == posJoints_P2[5] and P2_pos==True) or (round(J1_RoboGuide.Value) == posJoints_P1[0] and  round(J2_RoboGuide.Value) == posJoints_P1[1] and  
        round(J3_RoboGuide.Value) == posJoints_P1[2] and round(J4_RoboGuide.Value) == posJoints_P1[3] and 
        round(J5_RoboGuide.Value) == posJoints_P1[4] and round(J6_RoboGuide.Value) == posJoints_P1[5] and P1_pos==True) or (round(J1_RoboGuide.Value) == posJoints_P3[0] and  round(J2_RoboGuide.Value) == posJoints_P3[1] and  
        round(J3_RoboGuide.Value) == posJoints_P3[2] and round(J4_RoboGuide.Value) == posJoints_P3[3] and 
        round(J5_RoboGuide.Value) == posJoints_P3[4] and round(J6_RoboGuide.Value) == posJoints_P3[5] and P3_pos==True) or (round(J1_RoboGuide.Value) == posJoints_P4[0] and  round(J2_RoboGuide.Value) == posJoints_P4[1] and  
        round(J3_RoboGuide.Value) == posJoints_P4[2] and round(J4_RoboGuide.Value) == posJoints_P4[3] and 
        round(J5_RoboGuide.Value) == posJoints_P4[4] and round(J6_RoboGuide.Value) == posJoints_P4[5] and P4_pos==True):
      counter_RB = counter_RB+1
      RB_counter.Value = counter_RB
      Timer_pos = True
      if P1_pos == True and P2_pos == False and P3_pos == False and P4_pos == False:
        P1_pos = False
        P2_pos = True
        P3_pos = False
        P4_pos = False
      elif P1_pos == False and P2_pos == True and P3_pos == False and P4_pos == False:
        P1_pos = False
        P2_pos = False
        P3_pos = True
        P4_pos = False
      elif P1_pos == False and P2_pos == False and P3_pos == True and P4_pos == False:
        P1_pos = False
        P2_pos = False
        P3_pos = False
        P4_pos = True
      else:
        P1_pos = True
        P2_pos = False
        P3_pos = False
        P4_pos = False
      #print("Cykle RoboG: ", counter_RB)
    if (round(joints[0].VALUE) == posJoints_P2[0] and round(joints[1].VALUE) == posJoints_P2[1] and round(joints[2].VALUE) == posJoints_P2[2] and round(joints[3].VALUE) == posJoints_P2[3] and 
        round(joints[4].VALUE) == posJoints_P2[4] and round(joints[5].VALUE) == posJoints_P2[5] and P2_posRB == True) or (round(joints[0].VALUE) == posJoints_P1[0] and round(joints[1].VALUE) == posJoints_P1[1] and 
        round(joints[2].VALUE) == posJoints_P1[2] and round(joints[3].VALUE) == posJoints_P1[3] and 
        round(joints[4].VALUE) == posJoints_P1[4] and round(joints[5].VALUE) == posJoints_P1[5] and P1_posRB == True) or (round(joints[0].VALUE) == posJoints_P3[0] and round(joints[1].VALUE) == posJoints_P3[1] and 
        round(joints[2].VALUE) == posJoints_P3[2] and round(joints[3].VALUE) == posJoints_P3[3] and 
        round(joints[4].VALUE) == posJoints_P3[4] and round(joints[5].VALUE) == posJoints_P3[5] and P3_posRB == True) or (round(joints[0].VALUE) == posJoints_P4[0] and round(joints[1].VALUE) == posJoints_P4[1] and 
        round(joints[2].VALUE) == posJoints_P4[2] and round(joints[3].VALUE) == posJoints_P4[3] and 
        round(joints[4].VALUE) == posJoints_P4[4] and round(joints[5].VALUE) == posJoints_P4[5] and P4_posRB == True):
      counter=counter+1
      VC_counter.Value = counter
      Timer_pos = True
      if P1_posRB == True and P2_posRB == False and P3_posRB == False and P4_posRB == False:
        P1_posRB = False
        P2_posRB = True
        P3_posRB = False
        P4_posRB = False
      elif P1_posRB == False and P2_posRB == True and P3_posRB == False and P4_posRB == False:
        P1_posRB = False
        P2_posRB = False
        P3_posRB = True
        P4_posRB = False
      elif P1_posRB == False and P2_posRB == False and P3_posRB == True and P4_posRB == False:
        P1_posRB = False
        P2_posRB = False
        P3_posRB = False
        P4_posRB = True
      else:
        P1_posRB = True
        P2_posRB = False
        P3_posRB = False
        P4_posRB = False
      print("Cykle VC: ", counter)'''
    if VC_counter.Value < RB_counter.Value:
      joints[0].MaxSpeed += (K*e)
      joints[1].MaxSpeed += (K*e)
      joints[2].MaxSpeed += (K*e)
      joints[3].MaxSpeed += (K*e)
      joints[4].MaxSpeed += (K*e)
      joints[5].MaxSpeed += (K*e)
      delay(0.01)
    if VC_counter.Value > RB_counter.Value:
      if joints[0].MaxSpeed >= 210 and joints[1].MaxSpeed >= 210 and joints[2].MaxSpeed >=265 and joints[3].MaxSpeed >= 420 and joints[4].MaxSpeed >= 420 and joints[5].MaxSpeed >=720:
        joints[0].MaxSpeed -= (K*e)
        joints[1].MaxSpeed -= (K*e)
        joints[2].MaxSpeed -= (K*e)
        joints[3].MaxSpeed -= (K*e)
        joints[4].MaxSpeed -= (K*e)
        joints[5].MaxSpeed -= (K*e)
        delay(0.01)
      else:
        joints[0].MaxSpeed = joints[0].MaxSpeed
        joints[1].MaxSpeed = joints[1].MaxSpeed
        joints[2].MaxSpeed = joints[2].MaxSpeed
        joints[3].MaxSpeed = joints[3].MaxSpeed
        joints[4].MaxSpeed = joints[4].MaxSpeed
        joints[5].MaxSpeed = joints[5].MaxSpeed
    if VC_counter.Value == RB_counter.Value and VC_counter.Value > 1:
      if Timer_pos==True:
        end = time.clock()
        #print(end-start)
        dT = end-start
        Timer_pos = False
        Timer = True
        if dT<=1.8:
          #print("predkosc robotow jest rowna")
          joints[0].MaxSpeed = TargetSpeedJ1 + dT/10
          joints[1].MaxSpeed = TargetSpeedJ2+ dT/10
          joints[2].MaxSpeed = TargetSpeedJ3+ dT/10
          joints[3].MaxSpeed = TargetSpeedJ4+ dT/10
          joints[4].MaxSpeed = TargetSpeedJ5+ dT/10
          joints[5].MaxSpeed = TargetSpeedJ6+ dT/10
          delay(0.00001)
    #print(joints_values)
    #print(J1_RoboGuide.Value)
    #print(J6_RoboGuide.Value)
    #print(joints_speeds)
    #RB_test1 = J1_RoboGuide.Value
    delay(0.001)
    #RB_test2 = J1_RoboGuide.Value
    #print(abs(RB_test1-RB_test2)*10)

