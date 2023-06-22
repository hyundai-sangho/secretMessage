from tkinter import *
from tkinter import messagebox
import base64
import os


def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("암호화")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END)
        decode_message = message.encode("utf8")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("utf8")

        Label(screen2, text="복호화", font="arial", fg="white", bg="#00bd56").place(
            x=10, y=0
        )
        text2 = Text(
            screen2, font="Rpbote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0
        )
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt)

    elif password == "":
        messagebox.showerror("암호화", "비밀번호를 입력해주세요.")
    elif password != "1234":
        messagebox.showerror("암호화", "유효하지 않는 비밀번호입니다.")


def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("암호화")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        encode_message = message.encode("utf8")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("utf8")

        Label(screen1, text="암호화", font="arial", fg="white", bg="#ed3833").place(
            x=10, y=0
        )
        text2 = Text(
            screen1, font="Rpbote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0
        )
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt)

    elif password == "":
        messagebox.showerror("암호화", "비밀번호를 입력해주세요.")
    elif password != "1234":
        messagebox.showerror("암호화", "유효하지 않는 비밀번호입니다.")


def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("378x398")

    # icon
    image_icon = PhotoImage(file="keys.png")
    screen.iconphoto(False, image_icon)
    screen.title("PctApp")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="암호화 및 복호화할 텍스트를 입력하십시오.", fg="black", font=("calbri", 10)).place(
        x=10, y=10
    )

    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(
        text="암호화 및 복호화에 사용할 Secret 키를 입력하십시오", fg="black", font=("calbri", 10)
    ).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(
        x=10, y=200
    )

    Button(
        text="암호화", width=23, height=2, bg="#ed3833", fg="white", bd=0, command=encrypt
    ).place(x=10, y=250)

    Button(
        text="복호화", width=23, height=2, bg="#00bd56", fg="white", bd=0, command=decrypt
    ).place(x=200, y=250)

    Button(
        text="초기화", width=50, height=2, bg="#1089ff", fg="white", bd=0, command=reset
    ).place(x=10, y=300)

    screen.mainloop()


main_screen()
