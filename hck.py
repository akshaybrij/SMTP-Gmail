import pyscreenshot as ps
import webbrowser as wb
import numpy as np
import smtplib
import time
import cv2
import pyautogui as pa
wb.open('www.fb.com/profile.php')


if __name__ == "__main__" :
 time.sleep(5)
 x=ps.grab()
 xc=np.array(x)
 cv2.imwrite('D:/fb.jpg',xc)
 amt=smtplib.SMTP('smtp.gmail.com')
 amt.starttls()
 amt.login('__Username__','**Pass**')
 pa.hotkey('Ctrl','u')
 amt.sendmail('From','To','Message')
 time.sleep(7)
 x.show()
