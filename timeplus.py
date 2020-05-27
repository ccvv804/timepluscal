import sys # sys 모듈 가져오기
import binascii # binascii 모듈 가져오기
import os
import tkinter
import time
import datetime

iamtime = datetime.timedelta()
clickc = 0

def kbn_plus(r1,r2,r3):
    global iamtime, clickc 
    if r1 == '' :
        r1 = '0' 
    if r2 == '' :
        r2 = '0'
    if r3 == '' :
        r3 = '0'
    iamtime = datetime.timedelta(hours=int(r1), minutes=int(r2), seconds=int(r3)) + iamtime
    print(str(iamtime))
    return str(iamtime)
    
def kbn_minus(r1,r2,r3):    
    global iamtime, clickc
    if r1 == '' :
        r1 = '0' 
    if r2 == '' :
        r2 = '0'
    if r3 == '' :
        r3 = '0'
    iamtime = iamtime - datetime.timedelta(hours=int(r1), minutes=int(r2), seconds=int(r3))
    print(str(iamtime))
    return str(iamtime)
    
def kbn_reset():    
    
    pritn(r1)    
    
def guirun():
    global clickc
    r11 = e1.get()
    r22 = e2.get()
    r33 = e3.get()
    iamtext = kbn_plus(r11,r22,r33)
    clickc = clickc + 1
    clickt = str(clickc)
    label2.config(text='총 시간은 '+iamtext)
    label5.config(text='클릭 카운터 '+clickt)
    return None

def guirun_minus():
    global clickc
    r11 = e1.get()
    r22 = e2.get()
    r33 = e3.get()
    iamtext = kbn_minus(r11,r22,r33)
    clickc = clickc - 1
    clickt = str(clickc)
    label2.config(text='총 시간은 '+iamtext)
    label5.config(text='클릭 카운터 '+clickt)
    return None
    
def guirun_reset():
    global iamtime, clickc
    iamtime = datetime.timedelta()
    iamtext = str(iamtime) 
    clickc = 0
    clickt = str(clickc)
    label2.config(text='총 시간은 '+iamtext)
    label5.config(text='클릭 카운터 '+clickt)
    return None    

window=tkinter.Tk()
window.title("time")
window.geometry("200x300+0+0")
window.resizable(False, False)



#rtx = sys.argv[1]
#hanaripper(rtx)

if __name__ == '__main__': # UI 시작
    label = tkinter.Label(window, text="시간")
    label1 = tkinter.Label(window, text="분")
    label4 = tkinter.Label(window, text="초")
    button = tkinter.Button(window, text="더하기", overrelief="solid", width=10, command=guirun)
    button1 = tkinter.Button(window, text="빼기", overrelief="solid", width=10, command=guirun_minus)
    button2 = tkinter.Button(window, text="리셋", overrelief="solid", width=10, command=guirun_reset)
    e1 = tkinter.Entry(window)
    e2 = tkinter.Entry(window)    
    e3 = tkinter.Entry(window)    
    label2=tkinter.Label(window, text="시간 계산 결과값은 여기")
    label3=tkinter.Label(window, text="영상 시간 더하기 계산기")
    label5=tkinter.Label(window, text="시간 계산 카운터는 여기")
    label.pack()
    e1.pack()
    label1.pack()
    e2.pack()
    label4.pack()
    e3.pack()
    button.pack()  
    button1.pack()
    button2.pack()    
    label2.pack()
    label5.pack()
    label3.pack(side="bottom")
    window.mainloop()