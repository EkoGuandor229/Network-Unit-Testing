from tkinter import *
import tkinter as tk

class TestOrder:
    cbuts = []
    root = Tk()

    def create_frame(self):
        self.root.title("Define Test-Order")
        self.root.geometry('350x400')
        lbl = Label(self.root, text="Choose Tests for execution")
        lbl.grid(column=0, row=0)
        btn_all = Button(self.root, text="all", command=self.select_all)
        btn_all.grid(column=0, row=1)
        btn_none = Button(self.root, text="none", command=self.deselect_all)
        btn_none.grid(column=1, row=1)

    def create_cbuts(self, test_definitions):
        i = 0
        j = 2
        for test_definition in test_definitions.values():
            self.cbuts.append(Checkbutton(self.root, text=test_definition.get_test_id(), var=test_definition.is_executed))
            self.cbuts[i].grid(column=0, row=j)
            i += 1
            j += 1
        btn_selected = Button(self.root, text="Select", command=lambda: self.selected(test_definitions))
        btn_selected.grid(column=0, row=j)

    def select_all(self):
        for i in self.cbuts:
            i.select()

    def deselect_all(self):
        for i in self.cbuts:
            i.deselect()

    def quit(self):
        self.root.destroy()

    def selected(self, test_definitions):
        for test_definition in test_definitions.values():
            print(test_definition.get_is_executed().get())

    def define_test_order(self, test_definitions):
        self.create_frame()
        self.create_cbuts(test_definitions)
        self.root.mainloop()

