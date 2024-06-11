import tkinter
from tkinter import ttk
from tabs.linear_graphs import Tab1
from tabs.logarithmic_graphs import Tab2
# from tab3 import Tab3

root = tkinter.Tk()
root.geometry("915x1010")
root.title("Radar Range Equation Calculator")

# Create a style object
style = ttk.Style()

# Configure the style of the notebook
style.configure('TNotebook', background="#636363")

# Create a Notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(expand=True)

tab1 = Tab1(notebook)
tab2 = Tab2(notebook)
# tab3 = Tab3(notebook)

notebook.add(tab1, text="Linear")
notebook.add(tab2, text="Logarithmic")
# notebook.add(tab3, text='')

# Run the application
root.mainloop()