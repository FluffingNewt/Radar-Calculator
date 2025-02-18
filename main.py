import tkinter
from tkinter             import ttk
from tabs.linear_tab     import Tab1
from tabs.log_tab        import Tab2
from tabs.doppler_tab    import Tab3
from tabs.unam_range_tab import Tab4

root = tkinter.Tk()
root.geometry("915x1010")
root.title("Radar Range Equation Calculator")


style = ttk.Style()
style.configure('TNotebook', background="#636363")

notebook = ttk.Notebook(root)
notebook.pack(expand=True)

tab1 = Tab1(notebook)
tab2 = Tab2(notebook)
tab3 = Tab3(notebook)
tab4 = Tab4(notebook)

notebook.add(tab1, text="Linear")
notebook.add(tab2, text="Logarithmic")
notebook.add(tab3, text="Doppler")
notebook.add(tab4, text="Unambiguous Range")

root.mainloop()