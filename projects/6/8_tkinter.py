import time
# from tkinter import *  # коллизия имён!!!
import tkinter
import threading


def get_long_time(tim: int) -> str:
    """
    # 1 - 01 , 9 - 09, 10 - 10
    """
    if tim < 10:
        return f"0{tim}"
    return f"{tim}"


is_play = True
slider_widget = None
label_widget = None

hr = 0
mn = 0
sec = 0


def start():
    global hr
    global mn
    global sec

    global is_play
    is_play = True
    while True:
        multiplay = 1
        global slider_widget
        if slider_widget is not None:
            multiplay = slider_widget.get()

        if is_play:
            if sec >= 59:
                if mn >= 59:
                    if hr >= 23:
                        hr = 0
                        mn = 0
                        sec = 0
                    else:
                        hr += 1
                        mn = 0
                        sec = 0
                else:
                    mn += 1
                    sec = 0
            else:
                sec += 1 * multiplay

            str1 = f"{get_long_time(hr)}:{get_long_time(mn)}:{get_long_time(sec)}"
            print(str1)
            label_widget.config(text=str1)

        time.sleep(1)


def pause():
    global is_play
    is_play = not is_play


def reset():
    global hr
    hr = 0
    global mn
    mn = 0
    global sec
    sec = 0
    label_widget.config(text="00:00:00")



def start_thread():
    new_thread = threading.Thread(target=start)
    new_thread.start()

    # with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    #     executor.submit(start)


def create_ui():
    tkinter_ui_window = tkinter.Tk()
    label_time = tkinter.Label(tkinter_ui_window, text="Hello Python", fg="#eee", bg="#333")
    label_time.place(x=0, y=0)
    btn_start = tkinter.Button(tkinter_ui_window, text="start", fg='blue', command=start_thread)
    btn_start.place(x=0, y=50)
    btn_reset = tkinter.Button(tkinter_ui_window, text="reset", fg='yellow', command=reset)
    btn_reset.place(x=0, y=100)
    btn_pause = tkinter.Button(tkinter_ui_window, text="pause", fg='green', command=pause)
    btn_pause.place(x=0, y=150)
    slider = tkinter.Scale(tkinter_ui_window, from_=1, to=59, orient=tkinter.HORIZONTAL)
    slider.place(x=0, y=200)

    global slider_widget
    slider_widget = slider

    global label_widget
    label_widget = label_time

    print(slider.get())

    # lbl = Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
    # lbl.place(x=60, y=50)
    # txtfld = Entry(window, bd=5)
    # txtfld.place(x=80, y=150)
    tkinter_ui_window.title('Hello Python')
    tkinter_ui_window.geometry("640x480+10+10")
    tkinter_ui_window.mainloop()


if __name__ == '__main__':
    create_ui()
    # start()
