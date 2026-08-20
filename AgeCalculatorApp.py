from tkinter import * 

# import Pillow to control the exact dimensions of the photo
from PIL import Image, ImageTk

from tkinter import messagebox,Button


# create the main app window
age_app = Tk()


# set the title of the app window
age_app.title("Maryem Age calculator app")


# change the background color of the window
age_app.configure(background="pink") 


# open the image file and resize it to 200x150 pixels
pil_image = Image.open(r"c:\Users\user\Downloads\unnamed (1).png")
pil_image = pil_image.resize((200, 150))



# add a text label to the window
Label1 = Label(age_app, text="Age App Calculator")
Label1.pack()



# convert the Pillow image into a tkinter-compatible image
image = ImageTk.PhotoImage(pil_image)


# wrap the image in a Label widget so it can be displayed
image_label = Label(age_app, image=image)



# keep a reference so Python doesn't garbage-collect the image
image_label.image = image 


# display the image label in the window
image_label.pack()


#age variables
age = StringVar()

#set a default value for age 
age.set("00")


#display an input 
Label_input = Entry(age_app,width=2,background="white",font=('Arial',30),textvariable=age)
Label_input.pack()


#calculating the age 
# age_in_months = age * 12
# age_in_days = age * 365 
# age_in_weeks = age_in_months * 4

def calc(): 
    the_age_value = age.get()

    age_in_months = int(the_age_value) * 12
    age_in_days = int(the_age_value) * 365 
    age_in_weeks = age_in_days // 7

    line1 = f"your age in months is {age_in_months}"
    line2 = f"your age in days is {age_in_days}"
    line3 = f"your age in weeks is {age_in_weeks}"

    messagebox.showinfo("Age Results", '\n'.join([line1, line2, line3]))


#create the button 

btn = Button(age_app, text="calculate age", background='Green',command=calc,width=20,height=2,borderwidth=0)
btn.pack()



# start the app's event loop (keeps the window open and responsive)
age_app.mainloop()