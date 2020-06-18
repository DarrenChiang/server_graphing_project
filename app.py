from utils import *
from make_graph import *
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.graphs = list()
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.add_button = tk.Button(self, text='Add Graph', command=self.add_graph)
        self.add_button.pack(side='top')
        self.add_graph()

    def add_graph(self):
        graph = GraphFrame(self)
        self.graphs.append(graph)

class GraphFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.specs = list()
        self['highlightbackground'] = 'black'
        self['highlightthickness'] = 1
        self.pack(side='left')
        self.create_widgets()

    def create_widgets(self):
        self.spec_frame = tk.Frame(self)
        self.spec_frame.pack(side='top')

        self.add_spec()

        row = tk.Frame(self)
        row.pack(side='top')

        self.add_button = tk.Button(row, text='Add', command=self.add_spec)
        self.add_button.pack(side='left')
        self.graph_button = tk.Button(row, text='Graph', command=self.graph)
        self.graph_button.pack(side='right')

        self.graph_frame = tk.Frame(self)
        self.graph_frame.pack(side='top')

        self.del_button = tk.Button(self, text='Delete Graph', command=self.delete)
        self.del_button.pack(side='top')

    def graph(self):
        plots = list()

        for spec in self.specs:
            try:
                plots.append(spec.to_dict())
            except Exception as e:
                print(e)

        if len(plots) > 0:
            figure = plt.Figure(figsize=(6,5), dpi=100)
            ax = figure.add_subplot(111)

            for plot in plots:
                x, y = get_data(plot)
                ax.plot(x, y, label=plot['tool'] + ', ' + plot['chamber'])

            canvas = FigureCanvasTkAgg(figure, self.graph_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side='top')

    def add_spec(self):
        spec = Spec(self.spec_frame)
        self.specs.append(spec)

    def delete(self):
        if len(self.master.graphs) > 1:
            self.master.graphs.remove(self)
            self.destroy()

class Spec(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(side = 'left')
        self.create_widgets()

    def create_widgets(self):
        self.del_button = tk.Button(self, text='Delete Specs', command=self.delete)
        self.del_button.pack(side='top')

        _, _, self.tool = self.create_entry_row('Tool: ')
        _, _, self.chamber = self.create_entry_row('Chamber: ')
        _, _, self.date = self.create_entry_row('Date: ')

    def delete(self):
        if len(self.master.master.specs) > 1:
            self.master.master.specs.remove(self)
            self.destroy()

    def create_entry_row(self, prompt):
        row = tk.Frame(self)
        label = tk.Label(row, width=15, text=prompt)
        entry = tk.Entry(row)
        row.pack(side='top')
        label.pack(side='left')
        entry.pack(side='right')
        return row, label, entry

    def to_dict(self):
        d = {'tool': self.tool.get(), 'chamber': self.chamber.get()}
        d.update(parse_date(self.date.get()))
        return d

if __name__ == '__main__':
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
