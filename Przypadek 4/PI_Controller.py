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
#print(dofs[2].VALUE)
#print("-------------")
#print(joints[2].VALUE)
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
#joints_speeds=[d.MaxSpeed for d in joints]
posJoints_P1 = [-50, 14, -59, 54, 71, 5]
posJoints_P2 = [-50, 0, -35, 64, 58, -18]
posJoints_P3 = [-13, -27, -12, 48, 17, -17]
posJoints_P4 = [-40, -7, 15, 107, 42, -82]
posJoints_P5 = [-62, 38, 27, 104, 66, -90]
posJoints_P6 = [-62, 34, -50, 68, 72, -7]
posJoints_P7 = [-3, -7, -61, 3, 61, 28]
posJoints_P8 = [60, 38, -47, -141, 126, 55]
posJoints_P9 = [61, 29, 22, -102, 63, 145]
posJoints_P10 = [34, -19, -14, -70, 36, 95]
posJoints_P11 = [-3, -18, 18, -7, -22, 37]
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
  P1_pos = True
  P2_pos = False
  P3_pos = False
  P4_pos = False
  P5_pos = False
  P6_pos = False
  P7_pos = False
  P8_pos = False
  P9_pos = False
  P10_pos = False
  P11_pos = False
  
  P1_posRB = True
  P2_posRB = False
  P3_posRB = False
  P4_posRB = False
  P5_posRB = False
  P6_posRB = False
  P7_posRB = False
  P8_posRB = False
  P9_posRB = False
  P10_posRB = False
  P11_posRB = False
  Timer = True
  Timer_pos = False
  dT = 0
  while app.Simulation.IsRunning:
    joints_values=[d.VALUE for d in joints]
    #print(joints[5].VALUE)
    #print(joints_speeds[0])
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
        round(J5_RoboGuide.Value) == posJoints_P3[4] and round(J6_RoboGuide.Value) == posJoints_P3[5] and P3_pos==True) or (round(J1_RoboGuide.Value) == posJoints_P4[0] and  round(J2_RoboGuide.Value) == posJoints_P4[1] and  
        round(J3_RoboGuide.Value) == posJoints_P4[2] and round(J4_RoboGuide.Value) == posJoints_P4[3] and 
        round(J5_RoboGuide.Value) == posJoints_P4[4] and round(J6_RoboGuide.Value) == posJoints_P4[5] and P4_pos==True) or (round(J1_RoboGuide.Value) == posJoints_P5[0] and  round(J2_RoboGuide.Value) == posJoints_P5[1] and  
        round(J3_RoboGuide.Value) == posJoints_P5[2] and round(J4_RoboGuide.Value) == posJoints_P5[3] and 
        round(J5_RoboGuide.Value) == posJoints_P5[4] and round(J6_RoboGuide.Value) == posJoints_P5[5] and P5_pos==True) or (round(J1_RoboGuide.Value) == posJoints_P6[0] and  round(J2_RoboGuide.Value) == posJoints_P6[1] and  
        round(J3_RoboGuide.Value) == posJoints_P6[2] and round(J4_RoboGuide.Value) == posJoints_P6[3] and 
        round(J5_RoboGuide.Value) == posJoints_P6[4] and round(J6_RoboGuide.Value) == posJoints_P6[5] and P6_pos==True) or (round(J1_RoboGuide.Value) == posJoints_P7[0] and  round(J2_RoboGuide.Value) == posJoints_P7[1] and  
        round(J3_RoboGuide.Value) == posJoints_P7[2] and round(J4_RoboGuide.Value) == posJoints_P7[3] and 
        round(J5_RoboGuide.Value) == posJoints_P7[4] and round(J6_RoboGuide.Value) == posJoints_P7[5] and P7_pos==True) or (round(J1_RoboGuide.Value) == posJoints_P8[0] and  round(J2_RoboGuide.Value) == posJoints_P8[1] and  
        round(J3_RoboGuide.Value) == posJoints_P8[2] and round(J4_RoboGuide.Value) == posJoints_P8[3] and 
        round(J5_RoboGuide.Value) == posJoints_P8[4] and round(J6_RoboGuide.Value) == posJoints_P8[5] and P8_pos==True) or (round(J1_RoboGuide.Value) == posJoints_P9[0] and  round(J2_RoboGuide.Value) == posJoints_P9[1] and  
        round(J3_RoboGuide.Value) == posJoints_P9[2] and round(J4_RoboGuide.Value) == posJoints_P9[3] and 
        round(J5_RoboGuide.Value) == posJoints_P9[4] and round(J6_RoboGuide.Value) == posJoints_P9[5] and P9_pos==True) or (round(J1_RoboGuide.Value) == posJoints_P10[0] and  round(J2_RoboGuide.Value) == posJoints_P10[1] and  
        round(J3_RoboGuide.Value) == posJoints_P10[2] and round(J4_RoboGuide.Value) == posJoints_P10[3] and 
        round(J5_RoboGuide.Value) == posJoints_P10[4] and round(J6_RoboGuide.Value) == posJoints_P10[5] and P10_pos==True) or (round(J1_RoboGuide.Value) == posJoints_P11[0] and  round(J2_RoboGuide.Value) == posJoints_P11[1] and  
        round(J3_RoboGuide.Value) == posJoints_P11[2] and round(J4_RoboGuide.Value) == posJoints_P11[3] and 
        round(J5_RoboGuide.Value) == posJoints_P11[4] and round(J6_RoboGuide.Value) == posJoints_P11[5] and P11_pos==True):
      counter_RB = counter_RB+1
      RB_counter.Value = counter_RB
      Timer_pos = True
      if P1_pos == True and P2_pos == False and P3_pos == False and P4_pos == False and P5_pos == False and P6_pos == False and P7_pos == False and P8_pos == False and P9_pos == False and P10_pos == False and P11_pos == False:
        P1_pos = False
        P2_pos = True
        P3_pos = False
        P4_pos = False
        P5_pos = False
        P6_pos = False
        P7_pos = False
        P8_pos = False
        P9_pos = False
        P10_pos = False
        P11_pos = False
      elif P1_pos == False and P2_pos == True and P3_pos == False and P4_pos == False and P5_pos == False and P6_pos == False and P7_pos == False and P8_pos == False and P9_pos == False and P10_pos == False and P11_pos == False:
        P1_pos = False
        P2_pos = False
        P3_pos = True
        P4_pos = False
        P5_pos = False
        P6_pos = False
        P7_pos = False
        P8_pos = False
        P9_pos = False
        P10_pos = False
        P11_pos = False
      elif P1_pos == False and P2_pos == False and P3_pos == True and P4_pos == False and P5_pos == False and P6_pos == False and P7_pos == False and P8_pos == False and P9_pos == False and P10_pos == False and P11_pos == False:
        P1_pos = False
        P2_pos = False
        P3_pos = False
        P4_pos = True
        P5_pos = False
        P6_pos = False
        P7_pos = False
        P8_pos = False
        P9_pos = False
        P10_pos = False
        P11_pos = False
      elif P1_pos == False and P2_pos == False and P3_pos == False and P4_pos == True and P5_pos == False and P6_pos == False and P7_pos == False and P8_pos == False and P9_pos == False and P10_pos == False and P11_pos == False:
        P1_pos = False
        P2_pos = False
        P3_pos = False
        P4_pos = False
        P5_pos = True
        P6_pos = False
        P7_pos = False
        P8_pos = False
        P9_pos = False
        P10_pos = False
        P11_pos = False
      elif P1_pos == False and P2_pos == False and P3_pos == False and P4_pos == False and P5_pos == True and P6_pos == False and P7_pos == False and P8_pos == False and P9_pos == False and P10_pos == False and P11_pos == False:
        P1_pos = False
        P2_pos = False
        P3_pos = False
        P4_pos = False
        P5_pos = False
        P6_pos = True
        P7_pos = False
        P8_pos = False
        P9_pos = False
        P10_pos = False
        P11_pos = False
      elif P1_pos == False and P2_pos == False and P3_pos == False and P4_pos == False and P5_pos == False and P6_pos == True and P7_pos == False and P8_pos == False and P9_pos == False and P10_pos == False and P11_pos == False:
        P1_pos = False
        P2_pos = False
        P3_pos = False
        P4_pos = False
        P5_pos = False
        P6_pos = False
        P7_pos = True
        P8_pos = False
        P9_pos = False
        P10_pos = False
        P11_pos = False
      elif P1_pos == False and P2_pos == False and P3_pos == False and P4_pos == False and P5_pos == False and P6_pos == False and P7_pos == True and P8_pos == False and P9_pos == False and P10_pos == False and P11_pos == False:
        P1_pos = False
        P2_pos = False
        P3_pos = False
        P4_pos = False
        P5_pos = False
        P6_pos = False
        P7_pos = False
        P8_pos = True
        P9_pos = False
        P10_pos = False
        P11_pos = False
      elif P1_pos == False and P2_pos == False and P3_pos == False and P4_pos == False and P5_pos == False and P6_pos == False and P7_pos == False and P8_pos == True and P9_pos == False and P10_pos == False and P11_pos == False:
        P1_pos = False
        P2_pos = False
        P3_pos = False
        P4_pos = False
        P5_pos = False
        P6_pos = False
        P7_pos = False
        P8_pos = False
        P9_pos = True
        P10_pos = False
        P11_pos = False
      elif P1_pos == False and P2_pos == False and P3_pos == False and P4_pos == False and P5_pos == False and P6_pos == False and P7_pos == False and P8_pos == False and P9_pos == True and P10_pos == False and P11_pos == False:
        P1_pos = False
        P2_pos = False
        P3_pos = False
        P4_pos = False
        P5_pos = False
        P6_pos = False
        P7_pos = False
        P8_pos = False
        P9_pos = False
        P10_pos = True
        P11_pos = False
      elif P1_pos == False and P2_pos == False and P3_pos == False and P4_pos == False and P5_pos == False and P6_pos == False and P7_pos == False and P8_pos == False and P9_pos == False and P10_pos == True and P11_pos == False:
        P1_pos = False
        P2_pos = False
        P3_pos = False
        P4_pos = False
        P5_pos = False
        P6_pos = False
        P7_pos = False
        P8_pos = False
        P9_pos = False
        P10_pos = False
        P11_pos = True
      else:
        P1_pos = True
        P2_pos = False
        P3_pos = False
        P4_pos = False
        P5_pos = False
        P6_pos = False
        P7_pos = False
        P8_pos = False
        P9_pos = False
        P10_pos = False
        P11_pos = False
      print("Cykle RoboG: ", counter_RB)
    if (round(joints[0].VALUE) == posJoints_P2[0] and round(joints[1].VALUE) == posJoints_P2[1] and round(joints[2].VALUE) == posJoints_P2[2] and round(joints[3].VALUE) == posJoints_P2[3] and 
        round(joints[4].VALUE) == posJoints_P2[4] and round(joints[5].VALUE) == posJoints_P2[5] and P2_posRB == True) or (round(joints[0].VALUE) == posJoints_P1[0] and round(joints[1].VALUE) == posJoints_P1[1] and 
        round(joints[2].VALUE) == posJoints_P1[2] and round(joints[3].VALUE) == posJoints_P1[3] and 
        round(joints[4].VALUE) == posJoints_P1[4] and round(joints[5].VALUE) == posJoints_P1[5] and P1_posRB == True) or (round(joints[0].VALUE) == posJoints_P3[0] and round(joints[1].VALUE) == posJoints_P3[1] and 
        round(joints[2].VALUE) == posJoints_P3[2] and round(joints[3].VALUE) == posJoints_P3[3] and 
        round(joints[4].VALUE) == posJoints_P3[4] and round(joints[5].VALUE) == posJoints_P3[5] and P3_posRB == True) or (round(joints[0].VALUE) == posJoints_P4[0] and round(joints[1].VALUE) == posJoints_P4[1] and 
        round(joints[2].VALUE) == posJoints_P4[2] and round(joints[3].VALUE) == posJoints_P4[3] and 
        round(joints[4].VALUE) == posJoints_P4[4] and round(joints[5].VALUE) == posJoints_P4[5] and P4_posRB == True) or (round(joints[0].VALUE) == posJoints_P5[0] and round(joints[1].VALUE) == posJoints_P5[1] and 
        round(joints[2].VALUE) == posJoints_P5[2] and round(joints[3].VALUE) == posJoints_P5[3] and 
        round(joints[4].VALUE) == posJoints_P5[4] and round(joints[5].VALUE) == posJoints_P5[5] and P5_posRB == True) or (round(joints[0].VALUE) == posJoints_P6[0] and round(joints[1].VALUE) == posJoints_P6[1] and 
        round(joints[2].VALUE) == posJoints_P6[2] and round(joints[3].VALUE) == posJoints_P6[3] and 
        round(joints[4].VALUE) == posJoints_P6[4] and round(joints[5].VALUE) == posJoints_P6[5] and P6_posRB == True) or (round(joints[0].VALUE) == posJoints_P7[0] and round(joints[1].VALUE) == posJoints_P7[1] and 
        round(joints[2].VALUE) == posJoints_P7[2] and round(joints[3].VALUE) == posJoints_P7[3] and 
        round(joints[4].VALUE) == posJoints_P7[4] and round(joints[5].VALUE) == posJoints_P7[5] and P7_posRB == True) or (round(joints[0].VALUE) == posJoints_P8[0] and round(joints[1].VALUE) == posJoints_P8[1] and 
        round(joints[2].VALUE) == posJoints_P8[2] and round(joints[3].VALUE) == posJoints_P8[3] and 
        round(joints[4].VALUE) == posJoints_P8[4] and round(joints[5].VALUE) == posJoints_P8[5] and P8_posRB == True) or (round(joints[0].VALUE) == posJoints_P9[0] and round(joints[1].VALUE) == posJoints_P9[1] and 
        round(joints[2].VALUE) == posJoints_P9[2] and round(joints[3].VALUE) == posJoints_P9[3] and 
        round(joints[4].VALUE) == posJoints_P9[4] and round(joints[5].VALUE) == posJoints_P9[5] and P9_posRB == True) or (round(joints[0].VALUE) == posJoints_P10[0] and round(joints[1].VALUE) == posJoints_P10[1] and 
        round(joints[2].VALUE) == posJoints_P10[2] and round(joints[3].VALUE) == posJoints_P10[3] and 
        round(joints[4].VALUE) == posJoints_P10[4] and round(joints[5].VALUE) == posJoints_P10[5] and P10_posRB == True) or (round(joints[0].VALUE) == posJoints_P11[0] and round(joints[1].VALUE) == posJoints_P11[1] and 
        round(joints[2].VALUE) == posJoints_P11[2] and round(joints[3].VALUE) == posJoints_P11[3] and 
        round(joints[4].VALUE) == posJoints_P11[4] and round(joints[5].VALUE) == posJoints_P11[5] and P11_posRB == True):
      counter=counter+1
      VC_counter.Value = counter
      if P1_posRB == True and P2_posRB == False and P3_posRB == False and P4_posRB == False and P5_posRB == False and P6_posRB == False and P7_posRB == False and P8_posRB == False and P9_posRB == False and P10_posRB == False and P11_posRB == False:
        P1_posRB = False
        P2_posRB = True
        P3_posRB = False
        P4_posRB = False
        P5_posRB = False
        P6_posRB = False
        P7_posRB = False
        P8_posRB = False
        P9_posRB = False
        P10_posRB = False
        P11_posRB = False
      elif P1_posRB == False and P2_posRB == True and P3_posRB == False and P4_posRB == False and P5_posRB == False and P6_posRB == False and P7_posRB == False and P8_posRB == False and P9_posRB == False and P10_posRB == False and P11_posRB == False:
        P1_posRB = False
        P2_posRB = False
        P3_posRB = True
        P4_posRB = False
        P5_posRB = False
        P6_posRB = False
        P7_posRB = False
        P8_posRB = False
        P9_posRB = False
        P10_posRB = False
        P11_posRB = False
      elif P1_posRB == False and P2_posRB == False and P3_posRB == True and P4_posRB == False and P5_posRB == False and P6_posRB == False and P7_posRB == False and P8_posRB == False and P9_posRB == False and P10_posRB == False and P11_posRB == False:
        P1_posRB = False
        P2_posRB = False
        P3_posRB = False
        P4_posRB = True
        P5_posRB = False
        P6_posRB = False
        P7_posRB = False
        P8_posRB = False
        P9_posRB = False
        P10_posRB = False
        P11_posRB = False
      elif P1_posRB == False and P2_posRB == False and P3_posRB == False and P4_posRB == True and P5_posRB == False and P6_posRB == False and P7_posRB == False and P8_posRB == False and P9_posRB == False and P10_posRB == False and P11_posRB == False:
        P1_posRB = False
        P2_posRB = False
        P3_posRB = False
        P4_posRB = False
        P5_posRB = True
        P6_posRB = False
        P7_posRB = False
        P8_posRB = False
        P9_posRB = False
        P10_posRB = False
        P11_posRB = False
      elif P1_posRB == False and P2_posRB == False and P3_posRB == False and P4_posRB == False and P5_posRB == True and P6_posRB == False and P7_posRB == False and P8_posRB == False and P9_posRB == False and P10_posRB == False and P11_posRB == False:
        P1_posRB = False
        P2_posRB = False
        P3_posRB = False
        P4_posRB = False
        P5_posRB = False
        P6_posRB = True
        P7_posRB = False
        P8_posRB = False
        P9_posRB = False
        P10_posRB = False
        P11_posRB = False
      elif P1_posRB == False and P2_posRB == False and P3_posRB == False and P4_posRB == False and P5_posRB == False and P6_posRB == True and P7_posRB == False and P8_posRB == False and P9_posRB == False and P10_posRB == False and P11_posRB == False:
        P1_posRB = False
        P2_posRB = False
        P3_posRB = False
        P4_posRB = False
        P5_posRB = False
        P6_posRB = False
        P7_posRB = True
        P8_posRB = False
        P9_posRB = False
        P10_posRB = False
        P11_posRB = False
      elif P1_posRB == False and P2_posRB == False and P3_posRB == False and P4_posRB == False and P5_posRB == False and P6_posRB == False and P7_posRB == True and P8_posRB == False and P9_posRB == False and P10_posRB == False and P11_posRB == False:
        P1_posRB = False
        P2_posRB = False
        P3_posRB = False
        P4_posRB = False
        P5_posRB = False
        P6_posRB = False
        P7_posRB = False
        P8_posRB = True
        P9_posRB = False
        P10_posRB = False
        P11_posRB = False
      elif P1_posRB == False and P2_posRB == False and P3_posRB == False and P4_posRB == False and P5_posRB == False and P6_posRB == False and P7_posRB == False and P8_posRB == True and P9_posRB == False and P10_posRB == False and P11_posRB == False:
        P1_posRB = False
        P2_posRB = False
        P3_posRB = False
        P4_posRB = False
        P5_posRB = False
        P6_posRB = False
        P7_posRB = False
        P8_posRB = False
        P9_posRB = True
        P10_posRB = False
        P11_posRB = False
      elif P1_posRB == False and P2_posRB == False and P3_posRB == False and P4_posRB == False and P5_posRB == False and P6_posRB == False and P7_posRB == False and P8_posRB == False and P9_posRB == True and P10_posRB == False and P11_posRB == False:
        P1_posRB = False
        P2_posRB = False
        P3_posRB = False
        P4_posRB = False
        P5_posRB = False
        P6_posRB = False
        P7_posRB = False
        P8_posRB = False
        P9_posRB = False
        P10_posRB = True
        P11_posRB = False
      elif P1_posRB == False and P2_posRB == False and P3_posRB == False and P4_posRB == False and P5_posRB == False and P6_posRB == False and P7_posRB == False and P8_posRB == False and P9_posRB == False and P10_posRB == True and P11_posRB == False:
        P1_posRB = False
        P2_posRB = False
        P3_posRB = False
        P4_posRB = False
        P5_posRB = False
        P6_posRB = False
        P7_posRB = False
        P8_posRB = False
        P9_posRB = False
        P10_posRB = False
        P11_posRB = True
      else:
        P1_posRB = True
        P2_posRB = False
        P3_posRB = False
        P4_posRB = False
        P5_posRB = False
        P6_posRB = False
        P7_posRB = False
        P8_posRB = False
        P9_posRB = False
        P10_posRB = False
        P11_posRB = False
      print("Cykle VC: ", counter)
    if counter < counter_RB:
      joints[0].MaxSpeed += (K*e)
      joints[1].MaxSpeed += (K*e)
      joints[2].MaxSpeed += (K*e)
      joints[3].MaxSpeed += (K*e)
      joints[4].MaxSpeed += (K*e)
      joints[5].MaxSpeed += (K*e)
      delay(0.01)
    if counter > counter_RB:
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
    if counter == counter_RB and counter > 1:
      if Timer_pos==True:
        end = time.clock()
        #print(end-start)
        dT = end-start
        Timer_pos = False
        Timer = True
        if dT<=0.2:
          print("predkosc robotow jest rowna")
          joints[0].MaxSpeed = TargetSpeedJ1 + dT
          joints[1].MaxSpeed = TargetSpeedJ2+ dT
          joints[2].MaxSpeed = TargetSpeedJ3+ dT
          joints[3].MaxSpeed = TargetSpeedJ4+ dT
          joints[4].MaxSpeed = TargetSpeedJ5+ dT
          joints[5].MaxSpeed = TargetSpeedJ6+ dT
          delay(0.00001)
    #print(joints_values)
    #print(J1_RoboGuide.Value)
    #print(J6_RoboGuide.Value)
    #print(joints_speeds)
    #RB_test1 = J1_RoboGuide.Value
    delay(0.001)
    #RB_test2 = J1_RoboGuide.Value
    #print(abs(RB_test1-RB_test2)*10)