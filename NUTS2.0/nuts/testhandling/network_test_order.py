from tkinter import *
from tkinter import ttk


class TestOrder:
    cbuts = []
    ordered_test_definitions = []
    root = Tk()
    tab1 = 0
    tab2 = 0

    def create_frame(self):
        self.root.title("Define Test-Order")
        self.root.geometry('350x400')
        tab_control = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(tab_control)
        self.tab2 = ttk.Frame(tab_control)
        tab_control.add(self.tab1, text="Tests")
        tab_control.add(self.tab2, text="Order")
        Label(self.tab1, text="Choose Tests for execution").grid(column=0, row=0)
        Button(self.tab1, text="all", command=self.select_all).grid(column=0, row=1)
        Button(self.tab1, text="none", command=self.deselect_all).grid(column=1, row=1)
        tab_control.grid(column=0, row=0)

    def create_cbuts(self, test_definitions):
        i = 0
        j = 2
        for test_definition in test_definitions.values():
            self.cbuts.append(Checkbutton(self.tab1, text=test_definition.get_test_id(), var=test_definition.is_executed))
            self.cbuts[i].grid(column=0, row=j)
            i += 1
            j += 1
        btn_selected = Button(self.tab1, text="Select", command=lambda: self.selected(test_definitions))
        btn_selected.grid(column=0, row=j)

    def select_all(self):
        for i in self.cbuts:
            i.select()

    def deselect_all(self):
        for i in self.cbuts:
            i.deselect()

    def move_up(self, test_definition):
        for ordered_test_definition in self.ordered_test_definitions:
            if ordered_test_definition.get_test_id() == test_definition.get_test_id():
                i = self.ordered_test_definitions.index(ordered_test_definition)
                if i != 0:
                    self.ordered_test_definitions[i], self.ordered_test_definitions[i-1] = \
                        self.ordered_test_definitions[i-1], self.ordered_test_definitions[i]
        self.refresh_screen()

    def move_down(self, test_definition):
        for ordered_test_definition in self.ordered_test_definitions:
            if ordered_test_definition.get_test_id() == test_definition.get_test_id():
                i = self.ordered_test_definitions.index(ordered_test_definition)
                if i != len(self.ordered_test_definitions)-1:
                    self.ordered_test_definitions[i], self.ordered_test_definitions[i+1] = \
                        self.ordered_test_definitions[i+1], self.ordered_test_definitions[i]
                    break
        self.refresh_screen()

    def quit(self):
        self.root.destroy()

    def selected(self, test_definitions):
        for test_definition in test_definitions.values():
            if test_definition not  in self.ordered_test_definitions:
                if test_definition.get_is_executed().get():
                    self.ordered_test_definitions.append(test_definition)
        self.refresh_screen()

    def refresh_screen(self):
        i = 0
        for test_definition in self.ordered_test_definitions:
            Label(self.tab2, text=test_definition.get_test_id()).grid(column=0, row=i)
            Button(self.tab2, text="MoveUp", command=lambda x=test_definition: self.move_up(x)).grid(column=1, row=i)
            Button(self.tab2, text="MoveDown", command=lambda x=test_definition: self.move_down(x)).grid(column=2, row=i)
            i += 1

    def define_test_order(self, test_definitions):
        self.create_frame()
        self.create_cbuts(test_definitions)
        self.root.mainloop()

