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
#executor.OnProgramFinished = stopRecordingJointValues
signal = comp.getBehaviour("Boolean Signal")
J1_RoboGuide = comp.getBehaviour("RealSignalJ1")
J2_RoboGuide = comp.getBehaviour("RealSignalJ2")
J3_RoboGuide = comp.getBehaviour("RealSignalJ3")
J4_RoboGuide = comp.getBehaviour("RealSignalJ4")
J5_RoboGuide = comp.getBehaviour("RealSignalJ5")
J6_RoboGuide = comp.getBehaviour("RealSignalJ6")
RB_Joints_SPD = comp.getBehaviour("RB_Joints_SPD")
VC_counter = comp.getBehaviour("VC_counter")
RB_counter = comp.getBehaviour("RB_counter")
VC_Joints_SPD = 5
RBMaxSpeedJ1 = comp.getBehaviour("RBMaxSpeedJ1")
RBMaxSpeedJ2 = comp.getBehaviour("RBMaxSpeedJ2")
RBMaxSpeedJ3 = comp.getBehaviour("RBMaxSpeedJ3")
RBMaxSpeedJ4 = comp.getBehaviour("RBMaxSpeedJ4")
RBMaxSpeedJ5 = comp.getBehaviour("RBMaxSpeedJ5")
RBMaxSpeedJ6 = comp.getBehaviour("RBMaxSpeedJ6")

posJoints_P1 = [0, 0, 0, 10, 15, 20]
posJoints_P2 = [0, 26, -55, 0, 55, 0]
posJoints_P3 = [69, 28, -38, -32, 42, 25]
K = 0.5
def OnStart():
  joints[0].MaxSpeed = 210
  joints[1].MaxSpeed = 210
  joints[2].MaxSpeed = 265
  joints[3].MaxSpeed = 420
  joints[4].MaxSpeed = 420
  joints[5].MaxSpeed = 720
def OnSignal(signal):
  if signal.Value==True:
    resumeRun()
  if signal.Value==False:
    suspendRun()
def OnRun():
  suspendRun()
  counter = 0
  counter_RB=0
  P1_pos = True
  P2_pos = False
  P3_pos = False
  P1_posRB = True
  P2_posRB = False
  P3_posRB = False
  Timer = True
  Timer_pos = False
  dT = 0
  while app.Simulation.IsRunning:
    joints_values=[d.VALUE for d in joints]
    e = abs(counter_RB-counter)
    if Timer == True and counter != counter_RB:
      start=time.clock()
      Timer = False
    if counter == 1:
      TargetSpeedJ1=RBMaxSpeedJ1.Value*RB_Joints_SPD.Value/VC_Joints_SPD
      TargetSpeedJ2=RBMaxSpeedJ2.Value*RB_Joints_SPD.Value/VC_Joints_SPD
      TargetSpeedJ3=RBMaxSpeedJ3.Value*RB_Joints_SPD.Value/VC_Joints_SPD
      TargetSpeedJ4=RBMaxSpeedJ4.Value*RB_Joints_SPD.Value/VC_Joints_SPD
      TargetSpeedJ5=RBMaxSpeedJ5.Value*RB_Joints_SPD.Value/VC_Joints_SPD
      TargetSpeedJ6=RBMaxSpeedJ6.Value*RB_Joints_SPD.Value/VC_Joints_SPD
    if (round(J1_RoboGuide.Value) == posJoints_P2[0] and  round(J2_RoboGuide.Value) == posJoints_P2[1] and  round(J3_RoboGuide.Value) == posJoints_P2[2] and round(J4_RoboGuide.Value) == posJoints_P2[3] and 
        round(J5_RoboGuide.Value) == posJoints_P2[4] and round(J6_RoboGuide.Value) == posJoints_P2[5] and P2_pos==True) or (round(J1_RoboGuide.Value) == posJoints_P1[0] and  round(J2_RoboGuide.Value) == posJoints_P1[1] and  
        round(J3_RoboGuide.Value) == posJoints_P1[2] and round(J4_RoboGuide.Value) == posJoints_P1[3] and 
        round(J5_RoboGuide.Value) == posJoints_P1[4] and round(J6_RoboGuide.Value) == posJoints_P1[5] and P1_pos==True) or (round(J1_RoboGuide.Value) == posJoints_P3[0] and  round(J2_RoboGuide.Value) == posJoints_P3[1] and  
        round(J3_RoboGuide.Value) == posJoints_P3[2] and round(J4_RoboGuide.Value) == posJoints_P3[3] and 
        round(J5_RoboGuide.Value) == posJoints_P3[4] and round(J6_RoboGuide.Value) == posJoints_P3[5] and P3_pos==True):
      counter_RB = counter_RB+1
      RB_counter.Value = counter_RB
      Timer_pos = True
      if P1_pos == True and P2_pos == False and P3_pos == False:
        P1_pos = False
        P2_pos = True
        P3_pos = False
      elif P1_pos == False and P2_pos == True and P3_pos == False:
        P1_pos = False
        P2_pos = False
        P3_pos = True
      else:
        P1_pos = True
        P2_pos = False
        P3_pos = False
    if (round(joints[0].VALUE) == posJoints_P2[0] and round(joints[1].VALUE) == posJoints_P2[1] and round(joints[2].VALUE) == posJoints_P2[2] and round(joints[3].VALUE) == posJoints_P2[3] and 
        round(joints[4].VALUE) == posJoints_P2[4] and round(joints[5].VALUE) == posJoints_P2[5] and P2_posRB == True) or (round(joints[0].VALUE) == posJoints_P1[0] and round(joints[1].VALUE) == posJoints_P1[1] and 
        round(joints[2].VALUE) == posJoints_P1[2] and round(joints[3].VALUE) == posJoints_P1[3] and 
        round(joints[4].VALUE) == posJoints_P1[4] and round(joints[5].VALUE) == posJoints_P1[5] and P1_posRB == True) or (round(joints[0].VALUE) == posJoints_P3[0] and round(joints[1].VALUE) == posJoints_P3[1] and 
        round(joints[2].VALUE) == posJoints_P3[2] and round(joints[3].VALUE) == posJoints_P3[3] and 
        round(joints[4].VALUE) == posJoints_P3[4] and round(joints[5].VALUE) == posJoints_P3[5] and P3_posRB == True):
      counter=counter+1
      VC_counter.Value = counter
      if P1_posRB == True and P2_posRB == False and P3_posRB == False:
        P1_posRB = False
        P2_posRB = True
        P3_posRB = False
      elif P1_posRB == False and P2_posRB == True and P3_posRB == False:
        P1_posRB = False
        P2_posRB = False
        P3_posRB = True
      else:
        P1_posRB = True
        P2_posRB = False
        P3_posRB = False
    if counter < counter_RB:
      delay(0.01)
    if counter > counter_RB:
      if joints[0].MaxSpeed >= 210 and joints[1].MaxSpeed >= 210 and joints[2].MaxSpeed >=265 and joints[3].MaxSpeed >= 420 and joints[4].MaxSpeed >= 420 and joints[5].MaxSpeed >=720:
        delay(0.01)
      else:
        joints[0].MaxSpeed = joints[0].MaxSpeed
        joints[1].MaxSpeed = joints[1].MaxSpeed
        joints[2].MaxSpeed = joints[2].MaxSpeed
        joints[3].MaxSpeed = joints[3].MaxSpeed
        joints[4].MaxSpeed = joints[4].MaxSpeed
        joints[5].MaxSpeed = joints[5].MaxSpeed
    if counter == counter_RB and counter > 1:
      if Timer_pos==True:
        end = time.clock()
        dT = end-start
        Timer_pos = False
        Timer = True
        if dT<=0.2:
          delay(0.00001)
    delay(0.001)
