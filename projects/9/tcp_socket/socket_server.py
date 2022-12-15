import socket
import tkinter
import threading
import _thread
import json


def new_connection(__connection: any) -> None:
    print("connection start...")

    while True:
        data = __connection.recv(1024)

        res = f"[request]: {data} {type(data)}"

        # с2 = None
        # с2("12")

        global _set_text
        _set_text(res)  # tk_label.config(text="")
        print(res)

        if not data:
            __connection.send(b"[response]: MOT_ANY_DATA 400")
            break
        else:
            __connection.send(b"[response]: OK 200")

    __connection.close()
    pass


# TODO сервер, listener "слушатель" -> ip:port (порт занят и открыт)
def backend_server() -> None:  # 192.168.0.127:8000

    global _set_text
    _set_text("server started")

    with open("config.json", 'rb') as f:
        config = json.load(f)  # config = json.loads(f.read())

    host = config["host"]  # "192.168.0.127"
    port = config["port"]  # 8000
    print(host, port)

    print_lock = threading.Lock()
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind((host, port))
    my_socket.listen(5)

    while True:
        connection, address = my_socket.accept()
        print_lock.acquire()

        _thread.start_new_thread(new_connection, (connection,))
    my_socket.close()


def start_server():
    threading.Thread(target=backend_server).start()


def frontend_server() -> None:
    tk_windows = tkinter.Tk()
    tk_windows.title("our server")
    tk_windows.geometry("300x100")

    tk_label = tkinter.Label(tk_windows, text="server ready to start")
    tk_label.grid(row=0, column=0)

    def __set_text(__text: str) -> None:
        tk_label.config(text=__text)

    global _set_text
    _set_text = __set_text

    tk_button = tkinter.Button(tk_windows, text="start server", command=start_server)
    tk_button.grid(row=1, column=0)

    tk_windows.mainloop()


if __name__ == '__main__':
    # заглушка, чтобы код не ругался на тип данных
    def _set_text_ph(__text: str) -> None:
        pass

    _set_text = _set_text_ph  # промежуточная глобальная переменная для будущего хранения функции для установки
    # текста в поле

    frontend_server()

# области видимости


# a1 = 12  # глобальные
# print(a1)
#
#
# def set1():
#     global a1
#     a1 = 15  # локальная для set1
#     print(a1)
#     # def set2():
#     #     a1 = 17
#
#
# set1()
# print(a1)


# b1 = 12
# print(b1)
#
#
# def set4(val1: int) -> int:
#     return val1 ** 2
#
#
# b1 = set4(9)
# print(b1)  # 81
#
# b1 = set4
# print(b1)  # <function set4 at 0x0000012D307C60E0>
# b2 = b1(9)
# print(b2)  # 81
