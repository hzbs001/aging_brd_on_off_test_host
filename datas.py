#!C:\Users\wanglw\AppData\Local\Programs\Python\Python36\python.exe
#coding=utf-8
import tkinter as tk
import serial,time,csv
from crc16_mb import crc16
data_len = 64
data_len2 = 36
rsens = []
for i in range(0,100):
    rsens.append(0)
def sampleDatas(ser1,ngText,chk_en,val_1,val_2,val_3,val_4,val_5,val_6,val_7,val_8,\
				val_9,val_10,val_11,val_12,val_13,val_14,val_15,val_16,\
				val_17,val_18,val_19,val_20,val_21,val_22,val_23,val_24,\
				val_25,val_26,val_27,val_28,val_29,val_30,val_31,val_32,\
                val_ad,val_cmd,val_rl,val_fs,val_ser):
    itemp = 0
    crc = crc16()
    try:
        addr = int(val_ad.get(),16)
    except ValueError:
        addr = 0x58
    cmd = int(val_cmd.get(),16)
    mb_datas = [0x00,0x00,0x00,data_len]
    mb_datas.insert(0,cmd)
    mb_datas.insert(0,addr)
    myinputL = crc.createarray(mb_datas)
    myinput = bytes(myinputL)

    ##myinput = bytes([0x58,0x03,0x00,0x00,0x00,0x01,0x88,0xC3])
    #myinput = bytes([0x58,0x03,0x00,0x00,0x00,0x20,0x48,0xDB])
    #print(myinputL)
    ser1.write(myinput)
    time.sleep(0.03)
    ser1.flush()
    count = ser1.inWaiting()
    while count<data_len :
        #self.ser1.reset_input_buffer()
        ser1.write(myinput)
        time.sleep(0.03)
        ser1.flush()
        count = ser1.inWaiting()
        if(itemp>8):
            break
        itemp = itemp+1
    try:
        RL = int(val_rl.get(),10)
        RL = RL * 1000
    except ValueError:
        RL = 470e3
    try:
        FS = int(val_fs.get(),10)
    except ValueError:
        FS = 1023

    data = ser1.read(count)
    if count>data_len:
        for i in range(1,data_len+1):
            ttt = data[2*i+1]*256+data[2*i+2]
            ttt1 = (FS/(ttt+0.01)-1)*RL/1e3
            rsens[i-1] = ttt1
            if rsens[i-1]>99999:
                rsens[i-1] = 99999
        val_ser.set('%d Datas Received'%i)

        ############Second read######################
        mb_datas2 = [0x58,cmd,0x00,64,0x00,data_len2]
        myinputL2 = crc.createarray(mb_datas)
        myinput2 = bytes(myinputL2)

        ser1.write(myinput)
        time.sleep(0.03)
        ser1.flush()
        count2 = ser1.inWaiting()

        data2 = ser1.read(count2)
        for i in range(1,data_len2+1):
            ttt2 =  data2[2*i+1]*256+data2[2*i+2]
            ttt3 = (FS/(ttt2+0.01)-1)*RL/1e3
            rsens.append(ttt3)
        filename_onoff = 'dout.aging.ng.txt'
        fp1 = open(filename_onoff,'w')
        inum = 0
        for i in range(1,data_len+data_len2):
            if rsens[i]>10000 or rsens[i]<20:
                if inum!=0 and inum%4==0:
                    ngText.insert(tk.END,'\n'+'CH'+str(i-1)+': '+'%.2f'%rsens[i]+';')
                else:
                    ngText.insert(tk.END,'CH'+str(i-1)+': '+'%.2f'%rsens[i]+';')
                inum = inum+1
                fp1.write('CH%d\t'%i)
                fp1.write('%.2f\n'%rsens[i])
        fp1.close
        ############Second read End##################

        if(chk_en.get()==1):
            mytime = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))
            fp=open('data.onoff.txt','a+')
            #fp.write(mytime+'\n')
            for i in range(0,data_len+data_len2):
                fp.write('%.2f\t'%rsens[i])
            #fp.write('\nEnd of Sample\n\n')
            fp.close()
            ######CSV output
            filename = 'dout.aging.onoff.csv'
            try:
                csvFile = open(filename,'a')
                writer = csv.writer(csvFile)
            except FileNotFoundError:
                csvFile = open(filename,'w')
                writer = csv.writer(csvFile)
                writer.writerow(['ch0','ch1','ch2','ch3','ch4','ch5','ch6','ch7','ch8','ch9',\
                    'ch10','ch11','ch12','ch13','ch14','ch15','ch16','ch17','ch18','ch19',\
                    'ch20','ch21','ch22','ch23','ch24','ch25','ch26','ch27','ch28','ch29',\
                    'ch30','ch31'])
            writer.writerow(rsens[0:data_len+data_len2-1])
    else:
        val_ser.set('No Data Received')

    if(count>data_len):
    	temp1='%.1f'%rsens[0];val_1.set(temp1)
    	temp1='%.1f'%rsens[1];val_2.set(temp1)
    	temp1='%.1f'%rsens[2];val_3.set(temp1)
    	temp1='%.1f'%rsens[3];val_4.set(temp1)
    	temp1='%.1f'%rsens[4];val_5.set(temp1)
    	temp1='%.1f'%rsens[5];val_6.set(temp1)
    	temp1='%.1f'%rsens[6];val_7.set(temp1)
    	temp1='%.1f'%rsens[7];val_8.set(temp1)
    	temp1='%.1f'%rsens[8];val_9.set(temp1)
    	temp1='%.1f'%rsens[9];val_10.set(temp1)
    	temp1='%.1f'%rsens[10];val_11.set(temp1)
    	temp1='%.1f'%rsens[11];val_12.set(temp1)
    	temp1='%.1f'%rsens[12];val_13.set(temp1)
    	temp1='%.1f'%rsens[13];val_14.set(temp1)
    	temp1='%.1f'%rsens[14];val_15.set(temp1)
    	temp1='%.1f'%rsens[15];val_16.set(temp1)
    	#val_22.set(str(data[45]*256+data[46]))
    	#val_32.set(str(data[65]*256+data[66]))
    	temp1='%.1f'%rsens[16];val_17.set(temp1)
    	temp1='%.1f'%rsens[17];val_18.set(temp1)
    	temp1='%.1f'%rsens[18];val_19.set(temp1)
    	temp1='%.1f'%rsens[19];val_20.set(temp1)
    	temp1='%.1f'%rsens[20];val_21.set(temp1)
    	temp1='%.1f'%rsens[21];val_22.set(temp1)
    	temp1='%.1f'%rsens[22];val_23.set(temp1)
    	temp1='%.1f'%rsens[23];val_24.set(temp1)
    	temp1='%.1f'%rsens[24];val_25.set(temp1)
    	temp1='%.1f'%rsens[25];val_26.set(temp1)
    	temp1='%.1f'%rsens[26];val_27.set(temp1)
    	temp1='%.1f'%rsens[27];val_28.set(temp1)
    	temp1='%.1f'%rsens[28];val_29.set(temp1)
    	temp1='%.1f'%rsens[29];val_30.set(temp1)
    	temp1='%.1f'%rsens[30];val_31.set(temp1)
    	temp1='%.1f'%rsens[31];val_32.set(temp1)

