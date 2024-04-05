import tkinter as tk
from tkinter import *



def num_filter(number):
    number = str(number)
    _num = ["0","1","2","3","4","5","6","7","8","9"]
    res = ""
    for x in number:
        if x in _num:
            res += x
    res = str(res)
    return res


def _find_modified(_list, _obj, _counts):
    _counts = int(_counts)
    _res = -1
    for x in _list:
        _res += 1
        if x == _obj:
            _counts -= 1
            if _counts == 0:
                return _res
    if _res == -1:
        return _res


_str_file = ""


class Form_gui:

    def __init__(self):


        self._main = tk.Tk()
        self._main.geometry("800x800")
        self._scroll = Scrollbar(self._main, orient=VERTICAL)
        self._scroll.pack(side= RIGHT, fill=Y)




        self._head = tk.Label(self._main, text="STUDENT FORM", font=("Arial", 25))
        self._head.pack()

        self._box_create_form = tk.Frame(self._main, borderwidth=1, relief="solid")
        self._box_create_form.columnconfigure(0, weight=0)
        self._box_create_form.columnconfigure(1, weight=0)
        self._box_create_form.columnconfigure(2, weight=0)
        self._box_create_form.columnconfigure(3, weight=0)
        self._box_create_form.columnconfigure(4, weight=0)

        self._box_label1 = tk.Label(self._box_create_form, text="Name:", font=("Arial", 22))
        self._box_label1.grid(row=0, column=0)

        self._box_label2 = tk.Label(self._box_create_form, text="Roll:", font=("Arial", 22))
        self._box_label2.grid(row=1, column=0)

        self._box_label3 = tk.Label(self._box_create_form, text="Section:", font=("Arial", 22))
        self._box_label3.grid(row=2, column=0)

        self._box_label4 = tk.Label(self._box_create_form, text="Class:", font=("Arial", 22))
        self._box_label4.grid(row=3, column=0)

        self._box_label5 = tk.Label(self._box_create_form, text="Gender:", font=("Arial", 22))
        self._box_label5.grid(row=4, column=0)


        self._name = tk.StringVar()
        self._roll = tk.StringVar()
        self._section = tk.StringVar()
        self._class = tk.StringVar()
        self._genter_bool = tk.StringVar()
        self._id_find = tk.StringVar()
        self._id_write = tk.StringVar()

        self._input1 = tk.Entry(self._box_create_form, font=("Arial", 22), background="lightblue", textvariable=self._name)
        self._input1.grid(row=0,column=1)

        self._input2 = tk.Entry(self._box_create_form, font=("Arial", 22), background="lightcyan", textvariable=self._roll)
        self._input2.grid(row=1, column=1)

        self._input3 = tk.Entry(self._box_create_form, font=("Arial", 22), background="lightblue", textvariable=self._section)
        self._input3.grid(row=2, column=1)

        self._input4 = tk.Entry(self._box_create_form, font=("Arial", 22), background="lightcyan", textvariable=self._class)
        self._input4.grid(row=3, column=1)

        self._input5 = tk.Radiobutton(self._box_create_form, font=("Arial", 22), text="Male", variable=self._genter_bool, value="Male")
        self._input5.grid(row=4, column=1)

        self._input6 = tk.Radiobutton(self._box_create_form, font=("Arial", 22), text="Female", variable=self._genter_bool, value="Female")
        self._input6.grid(row=4, column=2)

        self._submit_btn = tk.Button(self._main, text="SUBMIT", font=("Arial", 22), background="cyan", command=self.submit)
        self._box_create_form.pack(pady=6)

        self._submit_btn.pack()

        self._text1 = tk.Label(self._main, font=("Arial", 22), text="a")
        self._text1.pack()
        ###################################################################################################


        self._text2 = tk.Label(self._main, font=("Arial", 22), text="Insert your id No. to read the students profile:")
        self._text2.pack()

        self._input_id = tk.Entry(self._main, font=("Arial", 22), background="lightcyan", textvariable=self._id_find)
        self._input_id.pack()

        self._read_btn = tk.Button(self._main, text="Read", font=("Arial", 22), background="cyan", command=self.read)
        self._read_btn.pack(pady=5)

        self._box_read_form = tk.Frame(self._main, borderwidth=1, relief="solid")
        self._box_read_form.columnconfigure(0, weight=0)
        self._box_read_form.columnconfigure(1, weight=0)
        self._box_read_form.columnconfigure(2, weight=0)
        self._box_read_form.columnconfigure(3, weight=0)
        self._box_read_form.columnconfigure(4, weight=0)

        self._box_label1_read = tk.Label(self._box_read_form, text="Name:", font=("Arial", 22))
        self._box_label1_read.grid(row=0, column=0)

        self._box_label2_read = tk.Label(self._box_read_form, text="Roll:", font=("Arial", 22))
        self._box_label2_read.grid(row=1, column=0)

        self._box_label3_read = tk.Label(self._box_read_form, text="Section:", font=("Arial", 22))
        self._box_label3_read.grid(row=2, column=0)

        self._box_label4_read = tk.Label(self._box_read_form, text="Class:", font=("Arial", 22))
        self._box_label4_read.grid(row=3, column=0)

        self._box_label5_read = tk.Label(self._box_read_form, text="Gender:", font=("Arial", 22))
        self._box_label5_read.grid(row=4, column=0)


        self._box_label1_show = tk.Label(self._box_read_form, text="     ", font=("Arial", 22), background="lightblue", borderwidth=1, relief="solid")
        self._box_label1_show.grid(row=0, column=1)

        self._box_label2_show = tk.Label(self._box_read_form, text="     ", font=("Arial", 22), background="lightcyan", borderwidth=1, relief="solid")
        self._box_label2_show.grid(row=1, column=1)

        self._box_label3_show = tk.Label(self._box_read_form, text="     ", font=("Arial", 22), background="lightblue", borderwidth=1, relief="solid")
        self._box_label3_show.grid(row=2, column=1)

        self._box_label4_show = tk.Label(self._box_read_form, text="     ", font=("Arial", 22), background="lightcyan", borderwidth=1, relief="solid")
        self._box_label4_show.grid(row=3, column=1)

        self._box_label5_show = tk.Label(self._box_read_form, text="     ", font=("Arial", 22), background="lightblue", borderwidth=1, relief="solid")
        self._box_label5_show.grid(row=4, column=1)

        self._box_read_form.pack()

        ###############################################################################
        self.label3 = tk.Label(text="Insert the student id and re-write the info on the create form section:", font=("Arial", 22))
        self.label3.pack(pady=8)

        self._input_id2 = tk.Entry(self._main, font=("Arial", 22), background="lightcyan", textvariable=self._id_write)
        self._input_id2.pack()

        self._write_btn = tk.Button(self._main, text="Write", font=("Arial", 22), background="cyan", command=self.write)
        self._write_btn.pack()


        self._main.mainloop()

        self._input6.deselect()

    def read(self):
        global _str_file
        self._server_read = open("server_students.txt", "r")
        self._server_read = self._server_read.read()
        self._server_read = str(self._server_read)
        self._server_read = self._server_read + "*"
        self._stu_id = int(num_filter(self._input_id.get()))
        self._res_str = self._server_read[_find_modified(self._server_read, "*", self._stu_id) : _find_modified(self._server_read, "*", (self._stu_id + 1))]
        _str_file = self._res_str
        ans = File_read(_str_file)
        ans = str(ans)
        ans = ans.split(",")
        if "\n" in ans[4][4:]:
            ans[4] = ans[4][:-1]
        _name = ans[0].split(":")
        _name = _name[2]
        _roll = ans[1].split(":")
        _roll = _roll[1]
        _section = ans[2].split(":")
        _section = _section[1]
        _class = ans[3].split(":")
        _class = _class[1]
        _gender = ans[4].split(":")
        _gender = str(_gender[1])
        self._box_label1_show.config(text= f"{_name}")
        self._box_label2_show.config(text=f"{_roll}")
        self._box_label3_show.config(text=f"{_section}")
        self._box_label4_show.config(text=f"{_class}")
        self._box_label5_show.config(text=f"{_gender}")

    def write(self):
        _id = self._id_write.get()
        _name = self._input1.get()
        _roll = self._input2.get()
        _section = self._input3.get()
        _class = self._input4.get()
        _gender = self._genter_bool.get()
        if _name.strip() == "" or _roll.strip() == "" or _section.strip() == "" or _class.strip() == "":
            pass
        else:
            _output = f'*{_id}: Name: {self._input1.get().capitalize()}, Roll: {self._input2.get()}, Section: {self._input3.get().upper()}, Class: {self._input4.get()}, Gender: {self._genter_bool.get()}'

        _server_write = open("server_students.txt", "a")
        _server_read = open("server_students.txt", "r")
        _server_str = _server_read.read()



    def submit(self):

        _server_write = open("server_students.txt", "a")
        _server_read = open("server_students.txt", "r")
        _server_str = _server_read.read()

        _id = 1
        _id += _server_str.count("*")

        _name = self._input1.get()
        _roll = self._input2.get()
        _section = self._input3.get()
        _class = self._input4.get()
        _gender = self._genter_bool.get()

        if _name.strip() == "" or _roll.strip() == "" or _section.strip() == "" or _class.strip() == "":
            pass
        else:
            _output = f'*{_id}: Name: {self._input1.get().capitalize()}, Roll: {self._input2.get()}, Section: {self._input3.get().upper()}, Class: {self._input4.get()}, Gender: {self._genter_bool.get()}'
            self._text1.config(text=f"Submitted successfully! The students id is: {_id}")
            _server_write.write("\n" + _output)
            _server_write.close()
            print(_output)
class File_read:
    def __init__(self, _str_f):
        self._str_f = _str_f
    def __str__(self):
        return f"{self._str_f}"
Form_gui()

