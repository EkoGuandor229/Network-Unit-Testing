from tkinter import *
from tkinter import ttk

from nuts.testhandling.GUI.ToggledFrame import ToggledFrame


class TestOrder:
    """
    The TestOrder Class creates a GUI and defines which Tests to run
    and in which order to run them in

     ...

    Attributes
    ----------
    checkbuttons
        Array to dynamically load a checkbutton for each test
    ordered_test_definitions
        Array with the specified order of the test_definitions
    root
        The root for TK inter so that every method shares the same screen
    tab1,tab2
        Tabs for the Tabview
    """

    checkbuttons = []
    ordered_test_definitions = []
    root = Tk()
    tab1 = 0
    tab2 = 0

    def create_frame(self):
        """
        Creates the basic frame structures with title and a tab view
        """
        self.root.title("Define Test-Order")
        tab_control = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(tab_control)
        self.tab2 = ttk.Frame(tab_control)
        tab_control.add(self.tab1, text="Tests")
        tab_control.add(self.tab2, text="Order")
        Label(self.tab1, text="Choose Tests for execution").grid(column=0, row=0)
        Button(self.tab1, text="all", width=10, command=self.select_all).grid(column=0, row=1, sticky=W)
        Button(self.tab1, text="none", width=10, command=self.deselect_all).grid(column=1, row=1, sticky=W)
        tab_control.grid(column=0, row=0)

    def create_checkbuttons(self, test_definitions):
        """
        Creates a checkbutton for each test and a toggledframe for each test group
        """
        groups = []
        for test_definition in test_definitions.values():
            if test_definition.get_test_group() not in groups:
                groups.append(test_definition.get_test_group())

        i = 0
        j = 2
        for group in groups:
            t = ToggledFrame(self.tab1, text=group, relief="raised", borderwidth=1)
            t.grid(column=0, row=j, sticky=W)

            for test_definition in test_definitions.values():
                if test_definition.get_test_group() == group:
                    self.checkbuttons.append(
                        Checkbutton(
                            t.sub_frame,
                            text=test_definition.get_test_id(),
                            var=test_definition.is_executed
                        )
                    )
                    self.checkbuttons[i].grid(column=0, row=j + 1, sticky=W)
                    i += 1
                    j += 1

        Button(self.tab1, text="Select", command=lambda: self.selected(test_definitions)).grid(
            column=0,
            row=j,
            sticky=W,
            pady=10
        )

    def select_all(self):
        """
        Method to select all checkbuttons
        """
        for i in self.checkbuttons:
            i.select()

    def deselect_all(self):
        """
        Method to deselect all checkbuttons
        """
        for i in self.checkbuttons:
            i.deselect()

    def move_up(self, test_definition):
        """
        Method to move a test up
        """
        for ordered_test_definition in self.ordered_test_definitions:
            if ordered_test_definition.get_test_id() == test_definition.get_test_id():
                i = self.ordered_test_definitions.index(ordered_test_definition)
                if i != 0:
                    self.ordered_test_definitions[i], self.ordered_test_definitions[i-1] = \
                        self.ordered_test_definitions[i-1], self.ordered_test_definitions[i]
        self.refresh_screen()

    def move_down(self, test_definition):
        """
        Method to move a test down
        """
        for ordered_test_definition in self.ordered_test_definitions:
            if ordered_test_definition.get_test_id() == test_definition.get_test_id():
                i = self.ordered_test_definitions.index(ordered_test_definition)
                if i != len(self.ordered_test_definitions)-1:
                    self.ordered_test_definitions[i], self.ordered_test_definitions[i+1] = \
                        self.ordered_test_definitions[i+1], self.ordered_test_definitions[i]
                    break
        self.refresh_screen()

    def quit(self):
        """
        Method to close the gui
        """
        self.root.destroy()

    def selected(self, test_definitions):
        """
        Takes every selected test and adds them in the tab2 to change the order
        """
        for test_definition in test_definitions.values():
            if test_definition not in self.ordered_test_definitions:
                if test_definition.get_is_executed().get():
                    self.ordered_test_definitions.append(test_definition)
        self.refresh_screen()

    def refresh_screen(self):
        """
        loads the selcted tests in the tab2
        """
        i = 0
        for test_definition in self.ordered_test_definitions:
            Label(self.tab2, text=test_definition.get_test_id(), width=25, anchor=W).grid(column=0, row=i)
            Button(self.tab2, text="Up", command=lambda x=test_definition: self.move_up(x)).grid(column=1, row=i)
            Button(self.tab2, text="Down", command=lambda x=test_definition: self.move_down(x)).grid(column=2, row=i)
            i += 1
        Button(self.tab2, text="Save and Quit", command=lambda: self.quit()).grid(column=0, row=i, sticky=W, pady=10)

    def define_test_order(self, test_definitions):
        """
        method to start the gui
        """
        self.create_frame()
        self.create_checkbuttons(test_definitions)
        self.root.mainloop()

