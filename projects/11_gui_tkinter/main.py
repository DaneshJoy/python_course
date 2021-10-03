import tkinter as tk
from image_lab import ImageLab
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    filepath = askopenfilename(
        filetypes=[("PNG Files", "*.png"),
                   ("Jpeg Files", "*.jpg"),
                   ("All Files", "*.*")]
        )
    ent_imgpath.delete(0, tk.END)
    ent_imgpath.insert(0, filepath)

def process_image():
    _path = ent_imgpath.get()
    img_lab = ImageLab(_path)
    img_lab.load_image()
    _op = ent_op.get()
    _factor = float(ent_factor.get())
    img_lab.enhance_image(_op, _factor)
    img_lab.show_image(img_lab.result)

app = tk.Tk()
app.title('Image Processing Lab')
app.resizable(False, False)

frm_main = tk.Frame(padx=20, pady=20)
frm_2 = tk.Frame(padx=20, pady=20)

lbl_imgpath = tk.Label(master=frm_main, text="Image path:>")
ent_imgpath = tk.Entry(master=frm_main, width=100)
btn_open = tk.Button(master=frm_main,
                     text="Open...",
                     width=15,
                     command=open_file)
btn_process = tk.Button(master=frm_main,
                        text="Process",
                        width=15,
                        command=process_image)

lbl_imgpath.grid(row=0, column=0)
ent_imgpath.grid(row=0, column=1)
btn_open.grid(row=0, column=2, padx=15, pady=15)
btn_process.grid(row=0, column=3, padx=15, pady=15)

lbl_op = tk.Label(master=frm_2, text="Operation:")
ent_op = tk.Entry(master=frm_2, width=50)
lbl_factor = tk.Label(master=frm_2, text="Factor:")
ent_factor = tk.Entry(master=frm_2, width=50)

lbl_op.grid(row=0, column=0)
ent_op.grid(row=0, column=1)
lbl_factor.grid(row=0, column=2)
ent_factor.grid(row=0, column=3)

frm_main.grid(row=0, column=0, sticky="w")
frm_2.grid(row=1, column=0, sticky="w")

app.mainloop()
