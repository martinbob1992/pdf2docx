from pdf2docx import Converter
import os
import uuid
from threading import Thread
import tkinter as tk
from tkinter import filedialog


def pdf_to_word():
    pdf_path = select_pdf_path.get()
    out_path = select_out_path.get()
    if len(pdf_path) > 0 and len(out_path) > 0:
        thread = Thread(target=thread_command, args=(pdf_path, out_path))
        btn.config(text='转码中,请稍等...', state=tk.DISABLED)
        thread.start()


def thread_command(pdf_path, out_path):
    try:
        cv = Converter(pdf_path)
        cv.convert(out_path, kwargs={'debug': True})
        cv.close()
    except BaseException as e:
        print("error!")
        print(e)
    else:
        print("success!")
    btn.config(text='转换文件', state=tk.NORMAL)


def select_pdf():
    path = tk.filedialog.askopenfilename(filetypes=[("pdf", "*.pdf")])
    select_pdf_path.set(path)
    active_btn()


def select_out_dir():
    path = tk.filedialog.askdirectory()
    pdf_name = os.path.basename(select_pdf_path.get())
    if len(pdf_name) == 0:
        pdf_name = str(uuid.uuid1()).replace("-", "")
    else:
        index = pdf_name.rfind(".")
        if index >= 0:
            pdf_name = pdf_name[0:index]
    select_out_path.set(path + os.path.sep + pdf_name + ".docx")
    active_btn()


def active_btn():
    pdf_path = select_pdf_path.get()
    out_path = select_out_path.get()
    if len(pdf_path) > 0 and len(out_path) > 0:
        btn.config(state=tk.NORMAL)
    else:
        btn.config(state=tk.DISABLED)


if __name__ == '__main__':
    app = tk.Tk()
    app.title('pdf转docx')
    app.geometry('380x130')
    app.resizable(0, 0)
    # app.attributes("-toolwindow", 2)
    app.iconphoto(False, tk.PhotoImage(file='pdf.png'))

    select_pdf_path = tk.StringVar()
    select_out_path = tk.StringVar()

    tk.Label(app, text='pdf文件:', width=10, height=2).grid(column=0, row=0)
    tk.Entry(app, textvariable=select_pdf_path, width=30).grid(column=1, row=0)
    tk.Button(app, text='选择pdf文件', command=select_pdf, width=10).grid(column=2, row=0)

    tk.Label(app, text='输出路径:', width=10, height=2).grid(column=0, row=1)
    tk.Entry(app, textvariable=select_out_path, width=30).grid(column=1, row=1)
    tk.Button(app, text='选择输出路径', command=select_out_dir, width=10).grid(column=2, row=1)

    btn = tk.Button(app, text="转换文件", command=pdf_to_word)
    btn.grid(column=1, row=2)
    active_btn()
    # 进入消息循环
    app.mainloop()
