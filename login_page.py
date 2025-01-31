from tkinter import *
from PIL import ImageTk, Image

class NextPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(10, 10)
        
        self.window.title('Next Page')

        self.bg_frame = Frame(self.window, bg='#040405', width=1500, height=1000)
        self.bg_frame.place(x=500, y=200)

        self.heading = Label(self.bg_frame, text="DETAILS OF INVENTORY MANAGEMNET SYSTEM", font=('yu gothic ui', 25, "bold"), bg="#040405", fg='white')
        self.heading.pack(pady=20)

        # Name
        self.name_label = Label(self.bg_frame, text="Asset NO", font=('yu gothic ui', 13, "bold"), bg="#040405", fg='white')
        self.name_label.pack(pady=10)
        self.name_entry = Entry(self.bg_frame, font=('yu gothic ui', 13), bg='#6b6a69', fg='white')
        self.name_entry.pack(pady=10)

        # USN
        self.usn_label = Label(self.bg_frame, text="Asset Name", font=('yu gothic ui', 13, "bold"), bg="#040405", fg='white')
        self.usn_label.pack(pady=10)
        self.usn_entry = Entry(self.bg_frame, font=('yu gothic ui', 13), bg='#6b6a69', fg='white')
        self.usn_entry.pack(pady=10)

        # Phone Number
        self.phone_label = Label(self.bg_frame, text="Type of Device", font=('yu gothic ui', 13, "bold"), bg="#040405", fg='white')
        self.phone_label.pack(pady=10)
        self.phone_entry = Entry(self.bg_frame, font=('yu gothic ui', 13), bg='#6b6a69', fg='white')
        self.phone_entry.pack(pady=10)

        # Email
        self.email_label = Label(self.bg_frame, text="Mac", font=('yu gothic ui', 13, "bold"), bg="#040405", fg='white')
        self.email_label.pack(pady=10)
        self.email_entry = Entry(self.bg_frame, font=('yu gothic ui', 13), bg='#6b6a69', fg='white')
        self.email_entry.pack(pady=10)

        # Submit Button
        self.submit_button = Button(self.bg_frame, text="Submit", font=('yu gothic ui', 13, "bold"), bg='#3047ff', fg='white', cursor='hand2', command=self.submit_details)
        self.submit_button.pack(pady=20)

    def submit_details(self):
        name = self.name_entry.get()
        usn = self.usn_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        # For now, we just print the details to the console
        print(f"Name: {name}, USN: {usn}, Phone: {phone}, Email: {email}")
        # Add your logic to handle the form data here

         # Clear the frame
        for widget in self.bg_frame.winfo_children():
            widget.destroy()

        # Display Thank You message
        self.thank_you_label = Label(self.bg_frame, text="Thank You!", font=('yu gothic ui', 50, "bold"), bg="#040405", fg='white')
        self.thank_you_label.pack(pady=20)

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Login Page')

        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        self.txt = "WELCOME TO ISBG"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white', bd=5, relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)

        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)

        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)

        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.open_next_page)
        self.login.place(x=20, y=10)

        self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?",
                                    font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                    activebackground="#040405", borderwidth=0, background="#040405", cursor="hand2")
        self.forgot_button.place(x=630, y=510)

        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=550, y=560)

        self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405")
        self.signup_button_label.place(x=670, y=555, width=111, height=35)

        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)

        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)

        self.show_image = ImageTk.PhotoImage(file='images\\show.png')
        self.hide_image = ImageTk.PhotoImage(file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')

    def open_next_page(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        NextPage(self.window)

def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()

if __name__ == '__main__':
    page()
