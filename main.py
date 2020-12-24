from tkinter import *
from tkinter import filedialog
import re

#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# ATTENTION!!! THIS IS STILL A WORK IN PROGRESS!!!
#
#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
#
root = Tk()
root.title('SUBTITRON')
root.geometry("500x300")

#Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=10)

#MENU
my_menu = Menu(root)
root.config(menu = my_menu)

#File Menu
file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label = "File",menu = file_menu)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save as")
file_menu.add_separator()
file_menu.add_command(label="Exit")


#Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label = "File",menu = edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")



def subtitles():
    sub = open_file()
    my_list = sub.readlines()
    print("ORIGINAL" + str(my_list))

    result = [letter.replace('ã', 'a') and letter.replace('º','s') for letter in my_list]
    converted_result = ''.join([str(element) for element in result])
    print("RESULT!! : " + str(converted_result))
    save_file(converted_result)
    #return str(converted_result)

def open_file():

   subtitle_file = filedialog.askopenfilename(initialdir = "C:/Users",title="Open File", filetypes=(("Subtitle Files","*.srt"),))
   subtitle_file = open(subtitle_file, 'r')
   return subtitle_file

def save_file(file):
    # SAVING RESULT ON THE FILE
    subtitle_file2 = filedialog.askopenfilename(initialdir="C:/Users", title="Save File", filetypes=(("Subtitle Files", "*.srt"),))
    subtitle_file2 = open(subtitle_file2, 'w')
    subtitle_file2.write(str(file))



open_btn = Button(root, text="Open File", command = subtitles)
open_btn.pack(pady=20)

save_btn = Button(root, text="Save File", command = save_file)
save_btn.pack(pady=40)

root.mainloop()