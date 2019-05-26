from tkinter import Tk, Frame, messagebox
from tkinter import Entry, Label, Button
from solver import draw_solution


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        # T
        self.T_label = Label(self, text='T')
        self.T_label.grid(row=0, column=0)

        self.T_entry = Entry(self)
        self.T_entry.grid(row=0, column=1)
        self.T_entry.insert(0, '25')

        # l
        self.l_label = Label(self, text='l')
        self.l_label.grid(row=0, column=2)

        self.l_entry = Entry(self)
        self.l_entry.grid(row=0, column=3)
        self.l_entry.insert(0, '40')

        # a
        self.a_label = Label(self, text='a')
        self.a_label.grid(row=0, column=4)

        self.a_entry = Entry(self)
        self.a_entry.grid(row=0, column=5)
        self.a_entry.insert(0, '1')

        # h
        self.h_label = Label(self, text='h')
        self.h_label.grid(row=0, column=6)

        self.h_entry = Entry(self)
        self.h_entry.grid(row=0, column=7)
        self.h_entry.insert(0, '1')

        # tau
        self.tau_label = Label(self, text='tau')
        self.tau_label.grid(row=0, column=8)

        self.tau_entry = Entry(self)
        self.tau_entry.grid(row=0, column=9)
        self.tau_entry.insert(0, '1')

        # fi
        self.fi_label = Label(self, text='fi =')
        self.fi_label.grid(row=1, column=0)

        self.fi0_entry = Entry(self)
        self.fi0_entry.grid(row=1, column=1)
        self.fi0_entry.insert(0, '0.025')

        self.fi0_label = Label(self, text='+')
        self.fi0_label.grid(row=1, column=2)

        self.fi1_entry = Entry(self)
        self.fi1_entry.grid(row=1, column=3)
        self.fi1_entry.insert(0, '0')

        self.fi1_label = Label(self, text='cos(pi*x/l) +')
        self.fi1_label.grid(row=1, column=4)

        self.fi2_entry = Entry(self)
        self.fi2_entry.grid(row=1, column=5)
        self.fi2_entry.insert(0, '0')

        self.fi2_label = Label(self, text='cos(2pi*x/l)')
        self.fi2_label.grid(row=1, column=6)

        #b
        self.b_label = Label(self, text='b =')
        self.b_label.grid(row=2, column=0)

        self.b0_entry = Entry(self)
        self.b0_entry.grid(row=2, column=1)
        self.b0_entry.insert(0, '0')

        self.b0_label = Label(self, text='+')
        self.b0_label.grid(row=2, column=2)

        self.b1_entry = Entry(self)
        self.b1_entry.grid(row=2, column=3)
        self.b1_entry.insert(0, '0.25')

        self.b1_label = Label(self, text='cos(pi*x/l) +')
        self.b1_label.grid(row=2, column=4)

        self.b2_entry = Entry(self)
        self.b2_entry.grid(row=2, column=5)
        self.b2_entry.insert(0, '-0.25')

        self.b2_label = Label(self, text='sin(pi*x/l) +')
        self.b2_label.grid(row=2, column=6)

        self.b3_entry = Entry(self)
        self.b3_entry.grid(row=2, column=7)
        self.b3_entry.insert(0, '0')

        self.b3_label = Label(self, text='cos(2pi*x/l) +')
        self.b3_label.grid(row=2, column=8)

        self.b4_entry = Entry(self)
        self.b4_entry.grid(row=2, column=9)
        self.b4_entry.insert(0, '-0.5')

        self.b4_label = Label(self, text='sin(2pi*x/l)')
        self.b4_label.grid(row=2, column=10)

        # solve button
        self.solve_button = Button(self, text='Solve', command=self.solve)
        self.solve_button.grid(row=4, column=0)
    
    def solve(self):
        try:
            draw_solution(
                int(self.T_entry.get()),
                int(self.l_entry.get()),
                float(self.a_entry.get()),
                float(self.h_entry.get()),
                float(self.tau_entry.get()),
                [float(self.fi0_entry.get()), float(self.fi1_entry.get()), float(self.fi2_entry.get())],
                [float(self.b0_entry.get()), float(self.b1_entry.get()), float(self.b2_entry.get()),
                float(self.b3_entry.get()), float(self.b4_entry.get())]
            )
        except ValueError as error:
            messagebox.showerror(title='Error', message=str(error))


def main():
    root = Tk()
    root.title("Differential Equations")
    root.geometry("1000x300")
    app = Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()
