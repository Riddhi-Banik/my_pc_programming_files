import tkinter as tk


def _repeat_code(code:str, parameters:list, target_change:str):
    """code: pass the actual code to mass execute
    parameters: pass a list of parameters to add parameters in the list everytime it gets executed
    target_change: pass a variable that will be located in the 'code's parameter area

    this function can significantly reduce repetition in a program"""

    _str = ""
    for x in parameters:
        _str += code.replace(target_change, str(x)) + "\n"
    return _str


  #https://www.youtube.com/watch?v=yAGqzyaotAQ&list=PL105eZx4YyKzHf0QPaHPuOWfe2MxX8bhn


class _Nid_GUI:

    def __init__(self):
        self._font = ('Arial', 24)
        self._main = tk.Tk()
        self._main.geometry("1000x700")
        self._main.title("Nid Management System")

        self._heading = tk.Label(self._main, text="NID Management System", font=('Arial', 40))
        self._heading.pack(padx=10, pady=10)

        self._segment = tk.Frame(self._main)
        self._segment.columnconfigure(0, weight=1)

        self._view_display = tk.Frame(self._segment)
        self._view_display.columnconfigure(0, weight=1)



        self.view_box = tk.Frame(self._segment, background="gray")


        self.view_box.columnconfigure(0, weight=1)
        self.view_box.columnconfigure(1, weight=1)
        self.view_box.columnconfigure(2, weight=1)
        self.view_box.columnconfigure(3, weight=1)

        self._label_nid_view_input_label = tk.Label(self.view_box, text="NID: ", font=self._font, background="gray")
        self._label_nid_view_input_label.grid(row=0, column=0)

        self._label_name_view_input_label = tk.Label(self.view_box, text="Name: ", font=self._font, background="gray")
        self._label_name_view_input_label.grid(row=1, column=0)

        self._label_birth_view_input_label = tk.Label(self.view_box, text="Date of Birth: ", font=self._font, background="gray")
        self._label_birth_view_input_label.grid(row=2, column=0)

        self._label_district_view_input_label = tk.Label(self.view_box, text="District: ", font=self._font, background="gray")
        self._label_district_view_input_label.grid(row=3, column=0)


        self._input_name_view_input = tk.Entry(self.view_box, font=self._font)
        self._input_name_view_input.grid(row=0, column=1)

        self._input_nid_view_input = tk.Entry(self.view_box, font=self._font)
        self._input_nid_view_input.grid(row=1, column=1)

        self._input_birth_view_input = tk.Entry(self.view_box, font=self._font)
        self._input_birth_view_input.grid(row=2, column=1)

        self._input_district_view_input = tk.Entry(self.view_box, font=self._font)
        self._input_district_view_input.grid(row=3, column=1)


        self.view_box.grid(row=0, column=0)
        self._view_display.grid(row=0, column=1)

        self._segment.pack(pady=20)
        self._main.mainloop()





_Nid_GUI()