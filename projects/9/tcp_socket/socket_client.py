import socket
import json
import tkinter
import threading


def client_connection():
    with open("config.json", 'rb') as f:
        config = json.load(f)  # config = json.loads(f.read())

    host = config["host"]  # "192.168.0.127"
    port = config["port"]  # 8000
    print(host, port)

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((host, port))
    while True:
        global _get_text
        message = _get_text()

        if len(message) > 0:
            my_socket.send(message.encode("ascii"))

            data = my_socket.recv(1024)

            global _set_text
            print(data)
            _set_text(data.decode(encoding="utf8"))
            continue
        break
    my_socket.close()


def frontend_client() -> None:

    tk_windows = tkinter.Tk()
    tk_windows.title("our client")
    tk_windows.geometry("640x480")

    ##############################################################################
    # TODO текст, который нужно отправить на сервер

    tk_entry = tkinter.Entry(tk_windows)
    tk_entry.grid(row=0, column=0)
    tk_entry.insert(0, "_")

    def __get_text() -> str:
        return tk_entry.get()

    global _get_text
    _get_text = __get_text

    ##############################################################################

    ##############################################################################
    # TODO текст, который нужно получить от сервера

    tk_label = tkinter.Label(tk_windows, text="")
    tk_label.grid(row=0, column=1)

    def __set_text(__text: str) -> None:
        tk_label.config(text=__text)

    global _set_text
    _set_text = __set_text

    ##############################################################################

    tk_button = tkinter.Button(tk_windows, text="connect",
                               command=lambda: threading.Thread(target=client_connection).start())
    tk_button.grid(row=1, column=0)

    tk_windows.mainloop()


if __name__ == '__main__':

    def _get_text() -> str:
        pass

    get_text = _get_text

    def _set_text(message: str) -> None:
        pass

    set_text = _set_text

    frontend_client()
