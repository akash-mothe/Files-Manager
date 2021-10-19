from tkinter import *
import tkinter
from tkinter.ttk import *
import tkinter.filedialog as tkfile
import os
import shutil
from tkinter import messagebox as msg

win = Tk()
win.geometry("800x600")
win.title("Files Arrenger")
win.configure(bg='#4B0082')
win.maxsize(width=800,height=600)
win.minsize(width=800,height=600)

dir_entry_var = StringVar()
picture_files_var = IntVar()
video_files_var = IntVar()
audio_files_var = IntVar()
document_files_var = IntVar()
software_files_var = IntVar()
mobile_apps_files_var = IntVar()
program_files_var = IntVar()
compressed_files_var = IntVar()
pgbar_var = IntVar()
pgbar_var.set(0)

picture_exten = ['jpg','jpeg','png','gif','ico','webp']
video_exten = ['webm','mpg','mp2','mpeg','mpe','mpv','ogg','mp4','3gp','m4p','m4v','avi','wmv','mov','qt','flv','swf','avchd','mkv']
audio_exten = ['mp3','wav','aif','mid','ply','aac','ac3','3ga']
document_exten = ['doc','docx','odt','pdf','xls','xlsx','ods','ppt','pptx','txt','rtf','wpd','csv','PDF']
software_exten = ['bat','exe','bin','cgi','com','gadget','jar','msi','wsf','ova','iso','whl']
mobile_apps_exten = ['apk','ipa','xap','appx']
program_exten = ['py','c','class','cpp','cs','h','java','pl','sh','swift','vb','html','js','css','xhtml','xml','php','sql','mdb']
compressed_exten = ['7z','arj','deb','pkg','rar','rpm','z','zip']


def folder_btn_func():
    path = tkfile.askdirectory()
    dir_entry_var.set(path)
    


def OnArrange():
    if dir_entry_var.get() != '':

        path = dir_entry_var.get()
        str_path = str(path)
        # os.makedirs(f"{str_path}\\Akkash")
        files = os.listdir(str_path)
        if picture_files_var.get()==0 and video_files_var.get()==0 and audio_files_var.get()==0 and document_files_var.get()==0 and software_files_var.get()==0 and mobile_apps_files_var.get()==0 and program_files_var.get()==0 and compressed_files_var.get()==0:
            msg.showinfo("Select Folder","Please select which folders do you want to create.")
        x = 0
        folder_count = 0
        try:
# ************FOR IMAGES FOLDER**********
            if picture_files_var.get() == 1:
                dst = f"{str_path}\\ImageFiles"
                os.makedirs(dst)
                for file in files:
                    filename = file.split(".")
                    # print(filename)
                    if len(filename)>=2:
                        for i in picture_exten:
                            if filename[-1]==i:
                                src = f"{str_path}\{file}"
                                shutil.move(src,dst)
                                x+=1
                                pgbar_var.set(x)
                    elif len(filename)<2:
                        folder_count+=1
# **********FOR VIDEO FOLDER**************
            if video_files_var.get() == 1:
                dst = f"{str_path}\\VideoFiles"
                os.makedirs(dst)
                for file in files:
                    filename = file.split(".")
                    # print(filename)
                    if len(filename)>=2:
                        for i in video_exten:
                            if filename[-1]==i:
                                src = f"{str_path}\{file}"
                                shutil.move(src,dst)
                                x+=1
                                pgbar_var.set(x)
                    elif len(filename)<2:
                        folder_count+=1

# **********FOR AUDIO FOLDER**************
            if audio_files_var.get() == 1:
                dst = f"{str_path}\\AudioFiles"
                os.makedirs(dst)
                for file in files:
                    filename = file.split(".")
                    # print(filename)
                    if len(filename)>=2:
                        for i in audio_exten:
                            if filename[-1]==i:
                                src = f"{str_path}\{file}"
                                shutil.move(src,dst)
                                x+=1
                                pgbar_var.set(x)
                    elif len(filename)<2:
                        folder_count+=1
# ************FOR DOCUMENT FOLDER**********
            if document_files_var.get() == 1:
                dst = f"{str_path}\\DocumentFiles"
                os.makedirs(dst)
                for file in files:
                    filename = file.split(".")
                    # print(filename)
                    if len(filename)>=2:
                        for i in document_exten:
                            if filename[-1]==i:
                                src = f"{str_path}\{file}"
                                shutil.move(src,dst)
                                x+=1
                                pgbar_var.set(x)
                    elif len(filename)<2:
                        folder_count+=1
# ************FOR SOFTWARE FOLDER**********
            if software_files_var.get() == 1:
                dst = f"{str_path}\\SoftwareFiles"
                os.makedirs(dst)
                for file in files:
                    # file1 = str(file).replace(' ',"_")
                    filename = file.split(".")
                    # print(filename)
                    if len(filename)>=2:
                        for i in software_exten:
                            if filename[-1]==i:
                                src = f"{str_path}\{file}"
                                shutil.move(src,dst)
                                x+=1
                                pgbar_var.set(x)
                    elif len(filename)<2:
                        folder_count+=1
# ************FOR MOBILE APPS FOLDER**********
            if mobile_apps_files_var.get() == 1:
                dst = f"{str_path}\\MobileAppsFiles"
                os.makedirs(dst)
                for file in files:
                    filename = file.split(".")
                    # print(filename)
                    if len(filename)>=2:
                        for i in mobile_apps_exten:
                            if filename[-1]==i:
                                src = f"{str_path}\{file}"
                                shutil.move(src,dst)
                                x+=1
                                pgbar_var.set(x)
                    elif len(filename)<2:
                        folder_count+=1
# ************FOR PROGRAM FILES FOLDER**********
            if program_files_var.get() == 1:
                dst = f"{str_path}\\ProgramFiles"
                os.makedirs(dst)
                for file in files:
                    filename = file.split(".")
                    # print(filename)
                    if len(filename)>=2:
                        for i in program_exten:
                            if filename[-1]==i:
                                src = f"{str_path}\{file}"
                                shutil.move(src,dst)
                                x+=1
                                pgbar_var.set(x)
                    elif len(filename)<2:
                        folder_count+=1
# ************FOR COMPRESSED FILES FOLDER**********
            if compressed_files_var.get() == 1:
                dst = f"{str_path}\\CompressedFiles"
                os.makedirs(dst)
                for file in files:
                    filename = file.split(".")
                    # print(filename)
                    if len(filename)>=2:
                        for i in compressed_exten:
                            if filename[-1]==i:
                                src = f"{str_path}\{file}"
                                shutil.move(src,dst)
                                x+=1
                                pgbar_var.set(x)
                    elif len(filename)<2:
                        folder_count+=1
            pgbar = Progressbar(win,orient=HORIZONTAL,mode='determinate',maximum = (len(files)-folder_count),length=796,variable=pgbar_var)
            pgbar.place(x=2,y=580)
            if x > 0:
                msg.showinfo("Success","Files arranged successfully")


        except FileExistsError:
            msg.showerror("File Exist","Same folder is already existed. \nPlease rename old folder name.")

    else:
        msg.showwarning("Empty","Please select the path where you want to arrange your files")
    




# btn_img = PhotoImage(file="button.png")

head_lbl = tkinter.Label(win,text="Get Arrange Your Files By It's Types",font="algerian 25 bold",fg="#07EFFF",bg="#4B0082")
head_lbl.pack()
head_lbl1 = tkinter.Label(win,text="Choose your folder below",font="algerian 20 bold",fg="#FF1493",bg="#4B0082")
head_lbl1.place(x=210,y=100)

dir_entry = tkinter.Entry(win,font="corbel 13 bold",textvariable=dir_entry_var,state=DISABLED)
dir_entry.place(x=70,y=150,width=560,height=30)

folder_btn = tkinter.Button(win,text="Select Folder",bg="#8B0000",fg="white",font="corbel 13 bold",bd=3,command=folder_btn_func)
folder_btn.place(x=640,y=150,width=120,height=30)

lbl2 = tkinter.Label(win,text="Which folders do you want to create?",font="britannic 17 bold",fg="#B5F51F",bg="#4B0082")
lbl2.place(x=40,y=230)

picture_files = tkinter.Checkbutton(win,text="Picture Files",bg="#4B0082",font="britannic 12 bold",fg="white",selectcolor="black",variable=picture_files_var)
picture_files.place(x=100,y=280)

video_files = tkinter.Checkbutton(win,text="Video Files",bg="#4B0082",font="britannic 12 bold",fg="white",selectcolor="black",variable=video_files_var)
video_files.place(x=100,y=305)

audio_files = tkinter.Checkbutton(win,text="Audio Files",bg="#4B0082",font="britannic 12 bold",fg="white",selectcolor="black",variable=audio_files_var)
audio_files.place(x=100,y=330)

document_files = tkinter.Checkbutton(win,text="Document Files",bg="#4B0082",font="britannic 12 bold",fg="white",selectcolor="black",variable=document_files_var)
document_files.place(x=100,y=355)

software_files = tkinter.Checkbutton(win,text="Software Files",bg="#4B0082",font="britannic 12 bold",fg="white",selectcolor="black",variable=software_files_var)
software_files.place(x=100,y=380)

mobile_apps_files = tkinter.Checkbutton(win,text="Mobile Applications",bg="#4B0082",font="britannic 12 bold",fg="white",selectcolor="black",variable=mobile_apps_files_var)
mobile_apps_files.place(x=100,y=405)

program_files = tkinter.Checkbutton(win,text="Programm Files",bg="#4B0082",font="britannic 12 bold",fg="white",selectcolor="black",variable=program_files_var)
program_files.place(x=100,y=430)

compressed_files = tkinter.Checkbutton(win,text="Compressed Files",bg="#4B0082",font="britannic 12 bold",fg="white",selectcolor="black",variable=compressed_files_var)
compressed_files.place(x=100,y=455)

arange_btn = tkinter.Button(win,text="Arrange",bg="#FF078C",fg="white",font="century 18 bold",bd=5,command=OnArrange)
arange_btn.place(x=500,y=500,width=190,height=40)



win.mainloop()


# *****************ADDITIONAL FUNCTIONALITIES*******************
# 1)suggest the folder name to create
#         by finding first which types of files that folder contains
# 2) Progress Bar
#      ====> Added

# *****************BUGS*******************
# 1) File arraged message is showing for every file operations
#    ===> Fixed
# 2) if the filename contain more than one dot then that file is getting moved
    # =====>Fixed
# 3)if the path contains folders then progress bar is not showing completed.
    # ====> Fixed