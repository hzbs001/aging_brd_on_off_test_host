#!C:\Users\wanglw\AppData\Local\Programs\Python\Python36\python.exe
import serial,time
import tkinter as tk
import tkinter.font as tkFont

from datas import sampleDatas
#from crc16_mb import crc16

#vref = 3.3
#FS = 4095
#RL = 200e3
class App(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        
        chk_en = tk.IntVar()
        val_ad = tk.StringVar()
        val_cmd = tk.StringVar()
        val_op1 = tk.StringVar()
        val_op2 = tk.StringVar()

        val_1 = tk.StringVar()
        val_2 = tk.StringVar()
        val_3 = tk.StringVar()
        val_4 = tk.StringVar()
        val_5 = tk.StringVar()
        val_6 = tk.StringVar()
        val_7 = tk.StringVar()
        val_8 = tk.StringVar()

        val_9 = tk.StringVar()
        val_10 = tk.StringVar()
        val_11 = tk.StringVar()
        val_12 = tk.StringVar()
        val_13 = tk.StringVar()
        val_14 = tk.StringVar()
        val_15 = tk.StringVar()
        val_16 = tk.StringVar()

        val_17 = tk.StringVar()
        val_18 = tk.StringVar()
        val_19 = tk.StringVar()
        val_20 = tk.StringVar()
        val_21 = tk.StringVar()
        val_22 = tk.StringVar()
        val_23 = tk.StringVar()
        val_24 = tk.StringVar()

        val_25 = tk.StringVar()
        val_26 = tk.StringVar()
        val_27 = tk.StringVar()
        val_28 = tk.StringVar()
        val_29 = tk.StringVar()
        val_30 = tk.StringVar()
        val_31 = tk.StringVar()
        val_32 = tk.StringVar()

        val_rl = tk.StringVar()
        val_fs = tk.StringVar()
        vpc = tk.StringVar()
        vp = tk.StringVar()

        val_ser = tk.StringVar()
        v1 = tk.StringVar()
        v2 = tk.StringVar()
        v3 = tk.StringVar()
        def openMyPort(v1,v2,v3):
            sport = v1.get();
            sportn = int(v2.get())
            try:
                self.ser1 = serial.Serial(sport,sportn)
                v3.set('Open'+' '+sport+' '+'Sucess')
                #print('Open {} Sucess!'.format(sport))
                #print(self.ser1)
            except serial.serialutil.SerialException:
                v3.set('Cannot open'+' '+sport)
                #print('Cannot open {}'.format(sport))

        def closeMyPort(v3):
            try:
                self.ser1.close()
                sport = v1.get()
                v3.set(sport+' '+'Closed')
            except:
                v3.set('Port Not Open') 


        helv24 = tkFont.Font(family='Helvetica',size=24,weight='bold')
        helv16 = tkFont.Font(family='Helvetica',size=16,weight='bold')

        self.addrLabel = tk.Label(self,fg='#00f',bg='#0f0',width=64,font=helv16,\
                text='100 CH On Off Test System')
        self.addrLabel.grid(row=0,column=0,columnspan=64)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='MBAddr:')
        self.addrLabel.grid(row=1,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_ad,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=1,column=8,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CMD:')
        self.addrLabel.grid(row=1,column=16,columnspan=8)
        #self.addrEntry = tk.Entry(self,textvariable=val_cmd,bg='white',fg='blue',width=8,font=helv24)
        #self.addrEntry.grid(row=1,column=24,columnspan=8)
        optionListcmd = ('03','10')
        val_cmd.set(optionListcmd[0])
        self.addroption = tk.OptionMenu(self,val_cmd,*optionListcmd)
        self.addroption.grid(row=1,column=24,columnspan=8)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='PORT:')
        self.addrLabel.grid(row=1,column=32,columnspan=8)

        optionListc = ('COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9','COM10',\
				'COM11','COM12','COM13','COM14','COM15','COM16','COM17','COM18','COM19','COM20')
        vpc.set(optionListc[8])
        self.addoption = tk.OptionMenu(self,vpc,*optionListc)
        self.addoption.grid(row=1,column=40,columnspan=8)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='BautRate:')
        self.addrLabel.grid(row=1,column=48,columnspan=8)
        #self.OptionMenu(row=1,column=56,columnspan=8)

        optionList = ('4800','9600','19200','38400','57600','115200','230400')
        vp.set(optionList[5])
        self.addoption = tk.OptionMenu(self,vp,*optionList)
        self.addoption.grid(row=1,column=56,columnspan=8)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH0(K):')
        self.addrLabel.grid(row=2,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_1,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=2,column=8,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH8(K):')
        self.addrLabel.grid(row=2,column=16,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_9,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=2,column=24,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH16(K):')
        self.addrLabel.grid(row=2,column=32,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_17,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=2,column=40,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH24(K):')
        self.addrLabel.grid(row=2,column=48,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_25,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=2,column=56,columnspan=8)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH1(K):')
        self.addrLabel.grid(row=3,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_2,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=3,column=8,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH9(K):')
        self.addrLabel.grid(row=3,column=16,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_10,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=3,column=24,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH17(K):')
        self.addrLabel.grid(row=3,column=32,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_18,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=3,column=40,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH25(K):')
        self.addrLabel.grid(row=3,column=48,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_26,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=3,column=56,columnspan=8)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH2(K):')
        self.addrLabel.grid(row=4,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_3,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=4,column=8,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH10(K):')
        self.addrLabel.grid(row=4,column=16,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_11,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=4,column=24,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH18(K):')
        self.addrLabel.grid(row=4,column=32,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_19,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=4,column=40,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH26(K):')
        self.addrLabel.grid(row=4,column=48,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_27,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=4,column=56,columnspan=8)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH3(K):')
        self.addrLabel.grid(row=5,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_4,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=5,column=8,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH11(K):')
        self.addrLabel.grid(row=5,column=16,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_12,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=5,column=24,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH19(K):')
        self.addrLabel.grid(row=5,column=32,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_20,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=5,column=40,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH27(K):')
        self.addrLabel.grid(row=5,column=48,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_28,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=5,column=56,columnspan=8)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH4(K):')
        self.addrLabel.grid(row=6,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_5,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=6,column=8,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH12(K):')
        self.addrLabel.grid(row=6,column=16,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_13,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=6,column=24,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH20(K):')
        self.addrLabel.grid(row=6,column=32,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_21,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=6,column=40,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH28(K):')
        self.addrLabel.grid(row=6,column=48,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_29,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=6,column=56,columnspan=8)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH5(K):')
        self.addrLabel.grid(row=7,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_6,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=7,column=8,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH13(K):')
        self.addrLabel.grid(row=7,column=16,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_14,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=7,column=24,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH21(K):')
        self.addrLabel.grid(row=7,column=32,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_22,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=7,column=40,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH29(K):')
        self.addrLabel.grid(row=7,column=48,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_30,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=7,column=56,columnspan=8)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH6(K):')
        self.addrLabel.grid(row=8,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_7,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=8,column=8,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH14(K):')
        self.addrLabel.grid(row=8,column=16,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_15,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=8,column=24,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH22(K):')
        self.addrLabel.grid(row=8,column=32,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_23,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=8,column=40,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH30(K):')
        self.addrLabel.grid(row=8,column=48,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_31,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=8,column=56,columnspan=8)

        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH7(K):')
        self.addrLabel.grid(row=9,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_8,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=9,column=8,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH15(K):')
        self.addrLabel.grid(row=9,column=16,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_16,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=9,column=24,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH23(K):')
        self.addrLabel.grid(row=9,column=32,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_24,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=9,column=40,columnspan=8)
        self.addrLabel = tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='CH31(K):')
        self.addrLabel.grid(row=9,column=48,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_32,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=9,column=56,columnspan=8)

        self.addrLabel=tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='RL(kOhm):')
        self.addrLabel.grid(row=10,column=0,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_rl,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=10,column=8,columnspan=8)
        self.addrLabel=tk.Label(self,fg='#eee',bg='#aaa',width=8,font=helv16,text='FS:')
        self.addrLabel.grid(row=10,column=16,columnspan=8)
        self.addrEntry = tk.Entry(self,textvariable=val_fs,bg='white',fg='blue',width=8,font=helv24)
        self.addrEntry.grid(row=10,column=24,columnspan=8)

        self.NGLabel=tk.Label(self,fg='cyan',bg='#aaa',width=8,font=helv16,text='NG:')
        self.NGLabel.grid(row=15,column=0,columnspan=8)
        self.NGText = tk.Text(self,bg='white',fg='red',height=6,width=56,font=helv24)
        self.NGText.grid(row=15,column=8,columnspan=56)

        self.genButton = tk.Button(self,text='Sample',font=helv24,width=8,command=lambda \
                                   :sampleDatas(self.ser1,self.NGText,chk_en,\
                                   val_1,val_2,val_3,val_4,val_5,val_6,val_7,val_8,\
				                   val_9,val_10,val_11,val_12,val_13,val_14,val_15,val_16,\
				                   val_17,val_18,val_19,val_20,val_21,val_22,val_23,val_24,\
				                   val_25,val_26,val_27,val_28,val_29,val_30,val_31,val_32,\
                                   val_ad,val_cmd,val_rl,val_fs,val_ser))
        self.genButton.grid(row=16,column=0)

        self.addcheck = tk.Checkbutton(self,onvalue=1,offvalue=0,text='WrToFile',variable=chk_en)
        self.addcheck.grid(row=16,column=8,columnspan=8)

        self.genButton = tk.Button(self,text='OpenPort',font=helv24,width=8,command=lambda \
                                   :openMyPort(vpc,vp,val_ser))
        self.genButton.grid(row=16,column=32)
        self.genButton = tk.Button(self,text='ClosePort',font=helv24,width=8,command=lambda \
                                   :closeMyPort(val_ser))
        self.genButton.grid(row=16,column=16)
        self.addrEntry = tk.Entry(self,textvariable=val_ser,bg='white',fg='blue',width=24,font=helv24)
        self.addrEntry.grid(row=16,column=40,columnspan=24)


app1 = App()
app1.master.title('MBDisp_20190405')
app1.mainloop()

