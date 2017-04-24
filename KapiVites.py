#!/usr/bin/python3
import sys, os
import errno

counter = 1

while counter < 100:

 def inputget():


  print (" ")

 LD = str(input("Left Dashboard switch (1/0)?"))
 print ("L.D. Swich = " + LD)
 print (" ")

 RD = str(input("Right Dashboard switch (1/0)?"))
 print ("R.D. Swich = " + RD)
 print (" ")


 CL = str(input("Child Lock switch (1/0)?"))
 print ("C.L. Swich = " + CL)
 print (" ")


 ML = str(input("Master Unlock switch (1/0)?"))
 print ("M.L. Swich = " + ML)
 print (" ")


 LI = str(input("Left Inside switch (1/0)?"))
 print ("L.I. Swich = " + LI)
 print (" ")

 LO = str(input("Left Outside switch (1/0)?"))
 print ("L.O. Swich = " + LO)
 print (" ")


 RI = str(input("Right Inside switch (1/0)?"))
 print ("R.I. Swich = " + RI)
 print (" ")


 RO = str(input("Right Outside switch (1/0)?"))
 print ("R.O. Swich = " + RO)
 print (" ")

  
 GS = input("Gear swift Position (P,N,D,1,2,3, or R)?")
 print ("G.S. Swich = " + GS)
 print (" ")

#############################

 def doorCheck(LD, RD, CL, ML, LI, LO, RI, RO, GS):
    """
    This funciton accepts nine arguments and verifyies
    the conditions that are needed for the doors to
    open or remian closed.

    It also provides some error correction for the
    GS variable to ensure that only a valid gearshift
    option exists.
    """
    print("Left dashboard switch (0 or 1): ", LD)
    print("Right dashboard switch (0 or 1): ", RD)
    print("Child lock switch (0 or 1): ", CL)
    print("Master unlock switch (0 or 1): ", ML)
    print("Left inside handle (0 or 1): ", LI)
    print("Left outside handle (0 or 1): ", LO)
    print("Right inside handle (0 or 1): ", RI)
    print("Right outside handle (0 or 1): ", RO)
    print("Gear shift position (0 or 1): ", GS)
    print()

##################################



 if GS not in {'P', 'p', 'N', 'n', 'D', 'd', '1', '2', '3', 'R'}:
  
      print("INVALID RECORD: ALL DOORS STAY CLOSED.")
      print(" ")
  

 if GS == 'R' or GS == 'D' or GS == 'N' or GS == 'r' or GS == 'd' or GS == 'n' or GS == '1' or GS == '2' or GS == '3' :

       print ("BOTH DOORS STAY CLOSED")
       print

 if LO == '1' and ML == '1' and GS == 'P' or GS == 'p' and RO == '1' and RD == '1' and LD == '1' and RI == '1' and LI == '1' and CL == '1' :

       print ("ALL DOORS ARE OPEN")
       print ("------------------ ")

 if ML == '0' and GS == 'P' or GS == 'p' and LD == '0' and RD == '0' and LI == '0' and RI == '0' and LO == '0' and RO == '0' and CL == '0' :

       print ("BOTH DOORS CLOSE")
       print


 if LD == '1' and ML == '1' and GS == 'P' or GS == 'p' and RD == '0' and LI == '0' and RI == '0' and LO == '0' and RO == '0' and CL == '0' :

      print ("LEFT SIDE DOOR IS OPEN ")
      print

 if RD == '1' and ML == '1' and GS == 'P' or GS == 'p' and LD == '0' and LI == '0' and RI == '0' and LO == '0' and RO == '0' and CL == '0' :

      print ("RIGHT SIDE DOOR IS OPEN ")
      print

 if LI == '1' and ML == '1' and GS == 'P' or GS == 'p' and RI == '0' and RD == '0' and LD == '0' and LO == '0' and RO == '0' and CL == '0' :

      print ("LEFT SIDE DOOR IS OPEN ")
      print

 if RI == '1' and ML == '1' and GS == 'P' or GS == 'p' and LI == '0' and RD == '0' and LD == '0' and LO == '0' and RO == '0' and CL == '0' :

      print ("RIGHT SIDE DOOR IS OPEN ")
      print

 if RO == '1' and ML == '1' and GS == 'P' or GS == 'p' and LO == '0' and RD == '0' and LD == '0' and RI == '0' and LI == '0' and CL == '0' :

      print ("RIGHT SIDE DOOR IS OPEN ")
      print

 if LO == '1' and ML == '1' and GS == 'P' or GS == 'p' and RO == '0' and RD == '0' and LD == '0' and RI == '0' and LI == '0' and CL == '0' :

      print ("LEFT SIDE DOOR IS OPEN ")
      print

  

 print ("..................................................")

 counter += 1

 print ("Reading record # '",counter,"'(Use Keyboard Interrupt to Stop the Program):")

 print (" ")

def main():
  inputGet()
  doorCheck(LD, RD, CL, ML, LI, LO, RI, RO, GS) 

if __name__ == '__main__':
  main()
