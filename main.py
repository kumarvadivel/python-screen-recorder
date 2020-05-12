import cv2
import numpy as np
import pyautogui
import selenium


print("welcome to python screen recorder")
inp=input()
print("python screen recorder is recording your file",inp,".avi\n please minimize the python window and carry on your recording \n to quit the recording please press CTRL+C")
si=input()

SCREEN_SIZE =(1366,768)


fourcc=cv2.VideoWriter_fourcc(*"XVID")

out=cv2.VideoWriter(inp+".avi",fourcc,20.0,(SCREEN_SIZE))




while True:
   
    img = pyautogui.screenshot()
  
    frame = np.array(img)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
 
    out.write(frame)
 
    cv2.imshow("screenshot", frame)
 
    if cv2.waitKey(1) == ord(si):
        break
qi=input()
if qi=='q':

    cv2.destroyAllWindows()
    out.release()