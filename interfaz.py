import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from analizador import *
import json


class ScrollText(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = tk.Text(
            self,
            bg="#f8f9fa",
            foreground="#343a40",
            insertbackground="#3b5bdb",
            selectbackground="blue",
            width=120,
            height=30,
            font=("Courier New", 13),
        )

        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)

        self.numberLines = TextLineNumbers(self, width=40, bg="#dee2e6")
        self.numberLines.attach(self.text)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.numberLines.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.text.bind("<Key>", self.onPressDelay)
        self.text.bind("<Button-1>", self.numberLines.redraw)
        self.scrollbar.bind("<Button-1>", self.onScrollPress)
        self.text.bind("<MouseWheel>", self.onPressDelay)

    def onScrollPress(self, *args):
        self.scrollbar.bind("<B1-Motion>", self.numberLines.redraw)

    def onScrollRelease(self, *args):
        self.scrollbar.unbind("<B1-Motion>", self.numberLines.redraw)

    def onPressDelay(self, *args):
        self.after(2, self.numberLines.redraw)

    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)

    def insert(self, *args, **kwargs):
        return self.text.insert(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.text.delete(*args, **kwargs)

    def index(self, *args, **kwargs):
        return self.text.index(*args, **kwargs)

    def redraw(self):
        self.numberLines.redraw()



class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs, highlightthickness=0)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        """redraw line numbers"""
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True:
            dline = self.textwidget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(
                2,
                y,
                anchor="nw",
                text=linenum,
                fill="#868e96",
                font=("Courier New", 13, "bold"),
            )
            i = self.textwidget.index("%s+1line" % i)


class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proyecto 1")
        self.geometry("1000x650")
        self.scroll = ScrollText(self)
        self.scroll.pack()
        self.after(200, self.scroll.redraw())

        self.menu = Menu(self)
        self.config(menu=self.menu)
        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label="ARCHIVO", menu=self.filemenu)
        self.filemenu.add_command(label="Guardar",command=self.guardar_mismo_nombre)
        self.filemenu.add_command(label="Abrir", command=self.open_file)
        self.filemenu.add_command(label="Guardar como", command=self.guardar_archivo)
        self.filemenu.configure(background="blue",foreground="white")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quit)
       

        btnanalizar = Button(self, text="Analizar", command=self.analizar_texto, bg="blue", fg="white", font=(15))
        btnanalizar.place(x=365,y=610)

        btnreporte = Button(self, text="Reporte", command=self.mostrar_reporte, bg="blue", fg="white", font=(15))
        btnreporte.place(x=440,y=610)

        btnerrores = Button(self, text="Errores", command=self.mostrarerrores, bg="blue", fg="white", font=(15))
        btnerrores.place(x=515,y=610)



    def guardar_archivo(self):
        filepath = asksaveasfilename(
            defaultextension="json",
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = self.scroll.get(1.0, tk.END)
            output_file.write(text)
        self.title(f"Proyecto 1 - {filepath}")




    def guardar_mismo_nombre(self):
        nombre = "archivo_entrada.json"
        ruta = filedialog.asksaveasfilename(defaultextension=".json",initialfile=nombre)
        if ruta:
            with open(ruta,"w") as output_file:
                text = self.scroll.get(1.0,tk.END)
                output_file.write(text)




    def analizar_texto(self):
       
        text = self.scroll.get(1.0, tk.END) 
        diagrama = analizar(text)
        for i in tokens:
            cont = 0
            print(cont+1,":",i)

    def mostrar_reporte(self):
        text = self.scroll.get(1.0, tk.END) 
        diagrama = reportar(text)
        print(diagrama.dot.source)
        diagrama.dot.view()


    def open_file(self):
        filepath = askopenfilename(
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        
        self.scroll.delete(1.0,tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            self.scroll.insert(tk.END, text)
        self.title(f"Proyecto 1 - {filepath}")


    def mostrarerrores(self):
        ventana_emergente = tk.Toplevel(root)
        ventana_emergente.title("Errores")   
        
        errores_serializados = [error.to_json() for error in errores]

        errores_json = json.dumps(errores_serializados,indent=4)

        texto = tk.Text(ventana_emergente, wrap=tk.WORD)
        texto.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(ventana_emergente, command=texto.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        texto.config(yscrollcommand=scrollbar.set)
        texto.insert(tk.END, errores_json)


root = Interfaz()
root.mainloop()