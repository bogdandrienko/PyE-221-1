import time
from tkinter import *
import threading


def get_long_time(tim: int) -> str:
    """
    # 1 - 01 , 9 - 09, 10 - 10
    """
    if tim < 10:
        return f"0{tim}"
    return f"{tim}"


is_play = True


def start():
    hr = 0
    mn = 0
    sec = 0
    multiplay = 7
    global is_play
    while True:
        if is_play:
            print(f"{get_long_time(hr)}:{get_long_time(mn)}:{get_long_time(sec)}")
            if sec >= 59:
                if mn >= 59:
                    if hr >= 23:
                        hr = 0
                        mn = 0
                        sec = 0
                    else:
                        hr += 1 * multiplay
                        mn = 0
                        sec = 0
                else:
                    mn += 1 * multiplay
                    sec = 0
            else:
                sec += 1 * multiplay
        time.sleep(1)


def pause():
    global is_play
    is_play = not is_play


def start_thread():
    new_thread = threading.Thread(target=start)
    new_thread.start()

    # with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    #     executor.submit(start)


def create_ui():
    window = Tk()
    btn_start = Button(window, text="start", fg='blue', command=start_thread)
    btn_start.place(x=0, y=0)
    btn_pause = Button(window, text="pause", fg='green', command=pause)
    btn_pause.place(x=0, y=100)
    # lbl = Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
    # lbl.place(x=60, y=50)
    # txtfld = Entry(window, bd=5)
    # txtfld.place(x=80, y=150)
    window.title('Hello Python')
    window.geometry("1280x720+10+10")
    window.mainloop()


if __name__ == '__main__':
    create_ui()
    # start()
