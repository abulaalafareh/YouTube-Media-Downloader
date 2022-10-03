# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 20:14:29 2022

@author: TOSHIBA
"""

from tkinter import *
import subprocess





window=Tk()


window.title('Scrapper')
window.geometry("1250x670")
window.configure(bg='#455D6F')

window.attributes('-alpha', 0.96)





lbl=Label(window, text="YouTube", fg='#D1F0BD', bg='#455D6F', font=("Calibiri", 32))
lbl.place(x=550, y=78, anchor='s')
lbl=Label(window, text="Scrapper", fg='White', bg='#455D6F', font=("Calibiri", 32))
lbl.place(x=750, y=78, anchor='s')
# lbl=Label(window, text="YouTube", fg='White', bg='#455D6F', font=("Calibiri", 24))
# lbl.place(x=570, y=130, anchor='s')
# lbl=Label(window, text="Scrapper", fg='#D1F0BD', bg='#455D6F', font=("Calibiri", 24))
# lbl.place(x=710, y=130, anchor='s')



# def complete_audio_video_download():
#     id = txtfld_url.get()
#     subprocess.run(['youtube-dl', id])
#     messagebox.showinfo("showinfo", "Video+Audio Downloaded")


def complete_audio_download():
     id = txtfld_url.get()
     print(id)
     print('Audio downloading...........')
     subprocess.run(['youtube-dl' ,'--extract-audio' ,'--audio-format' ,'mp3' ,'--output', '"%(uploader)s%(title)s.%(ext)s"' ,id] )
     print('Downloaded')

def complete_video_download():
     id = txtfld_url.get()
     print(id)
     print('video downloading...........')
     subprocess.run(['youtube-dl', '-f','bestvideo', id] )
     print('Downloaded')



def cut_audio_download():
    
    id = txtfld_url.get()
    print(id)
    
    out = subprocess.run(['youtube-dl','-g',id], capture_output=True) 
    
    st = out.stdout.splitlines()
    
    
    
    
    start_time = txtfld_st.get() #input("Enter the start time in format M:SS")
    end_time = txtfld_end.get() #input('Enter the stop time in format M:SS')

    print('cut Audio downloading...........')
    subprocess.run(['ffmpeg','-ss',start_time,'-to',end_time,'-i' ,st[1], '-c', 'copy', 'out9.mkv'])
    print('Downloaded')
    #messagebox.showinfo("showinfo", "cut Audio Downloaded")



def cut_video_download():
    
    id = txtfld_url.get()
    
    
    out = subprocess.run(['youtube-dl','-g',id], capture_output=True) 
    
    st = out.stdout.splitlines()
    
    
    
    
    start_time = txtfld_st.get() #input("Enter the start time in format M:SS")
    end_time = txtfld_end.get() #input('Enter the stop time in format M:SS')

    print('cut Video downloading.................')
    subprocess.run(['ffmpeg','-ss',start_time,'-to',end_time,'-i' ,st[0], '-c', 'copy','ouyoyo.mp4'])
    print('downloaded')
    #messagebox.showinfo("showinfo", "cut video Downloaded")
    
    

       
    
    
        
    
    

#uncut download
can = Canvas(window, width=1500, height = 33, bg='#D8E4ED')
can.place(x=0,y=105)
can2 = Canvas(window, width=330, height = 400, bg='#D8E4ED')
can2.place(x=10,y=180)
can3 = Canvas(window, width=330, height = 400, bg='#D8E4ED')
can3.place(x=430,y=180)
can4 = Canvas(window, width=330, height = 400, bg='#D8E4ED')
can4.place(x=850,y=180)

lbl_id=Label(window, text="Full Audio and Video download", fg='#455D6F',bg='#D8E4ED',font=("Calibiri", 12))
lbl_id.place(x=20, y=230)

# txtfld_api=Entry(window, text="ID", bd=5, width=30)
# txtfld_api.place(x=120, y=70)

lbl_url=Label(window, text="video url", fg='#455D6F',bg='#D8E4ED', width=10)
lbl_url.place(x=20, y=330)

txtfld_url=Entry(window, text="URL", bd=5, width=30)
txtfld_url.place(x=120, y=330)

btn_aud=Button(window, text="Download Audio", fg='#D1F0BD',bg='#455D6F' , bd=2, width=15, command=complete_audio_download)
btn_aud.place(x=70, y=430)
btn_vid=Button(window, text="Download Video", fg='#D1F0BD',bg='#455D6F' ,bd=2, width=15, command=complete_video_download)
btn_vid.place(x=200, y=430)
# btn_avid=Button(window, text="Download Audio + Video", fg='white',bg='grey' ,bd=2, width=20, command = complete_audio_video_download)
# btn_avid.place(x=330, y=180)



#cut download
lbl_id=Label(window, text="Cut Audio and Video download", fg='#455D6F',bg='#D8E4ED', font=("Calibiri", 12))
lbl_id.place(x=440, y=230)

lbl_st=Label(window, text="Start Time", fg='#455D6F',bg='#D8E4ED',width=10)
lbl_st.place(x=440, y=300)

txtfld_st=Entry(window, text="start time", bd=5, width=30)
txtfld_st.place(x=540, y=300)

lbl_end=Label(window, text="Stop Time", fg='#455D6F',bg='#D8E4ED', width=10)
lbl_end.place(x=440, y=380)

txtfld_end=Entry(window, text="stop time", bd=5, width=30)
txtfld_end.place(x=540, y=380)

btn_caud=Button(window, text="Download Audio(C)", fg='#D1F0BD',bg='#455D6F',bd=2, width=15, command=cut_audio_download)
btn_caud.place(x=490, y=470)
btn_cvid=Button(window, text="Download Video(C)", fg='#D1F0BD',bg='#455D6F',bd=2, width=15, command=cut_video_download)
btn_cvid.place(x=620, y=470)


#Scrapper Download






window.mainloop()




