import tkinter

window = tkinter.Tk()
window.title("Login Form")
window.geometry('340x440')
window.configure(bg='#333333')

def login():
    username = "dilan"
    password = "abcd1234"
    if username_entry.get()==username and password_entry.get()==password:
        message_label = tkinter.Label(frame, text="Login successful", bg='#333333', fg="green", font=("Arial", 16))
        message_label.grid(row=4, column=0, columnspan=2, sticky="news", pady=10)
    else:
        message_label = tkinter.Label(frame, text="Invalid username or password", bg='#333333', fg="red", font=("Arial", 16))
        message_label.grid(row=4, column=0, columnspan=2, sticky="news", pady=10)

frame = tkinter.Frame(bg='#333333')

login_label = tkinter.Label(frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
username_label = tkinter.Label(frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_label = tkinter.Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
login_button = tkinter.Button(frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)



login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)


frame.pack()


window.mainloop()
