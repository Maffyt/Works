from tkinter import messagebox
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
import cProfile
def main():
    window = Tk()
    window.title('Авторизация')
    window.geometry('450x230')
    window.resizable(False, False)
    font_header = ('TimesNewRoman', 15)
    font_entry = ('TimesNewRoman', 12)
    label_font = ('TimesNewRoman', 11)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}
    def clicked(username_entry='name', password_entry=544):
        username = username_entry.get()
        password = password_entry.get()
        messagebox.showinfo('Заголовок, {username}, {password}'.format(username=username,
                                                         password=password))

        main_label = Label(window, text='Авторизация', font=font_header, **header_padding)
        main_label.pack()
        username_label = Label(window, text='Имя пользователя', font=label_font,
                               **base_padding)
        username_label.pack()
        username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
        username_entry.pack()
        password_label = Label(window, text='Пароль', font=label_font,
                               **base_padding)
        password_label.pack()
        password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
        password_entry.pack()
        send_btn = Button(window, text='Войти', command=clicked)
        send_btn.pack(**base_padding)
        window.mainloop()

if __name__ == '__main__':
    main()
