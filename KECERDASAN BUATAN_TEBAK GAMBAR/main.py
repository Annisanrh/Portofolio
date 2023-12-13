# Import library tkinter digunakan untuk membuka canvas seperti paint
# Import numpy 
# Import AI
# Import library pillow
import tkinter as tk
import AI
import numpy as np
from PIL import Image, ImageTk, ImageDraw

model = AI.load_ai()

# Membuat canvas seperti paint
# Menampilkan library pemrosesan gambar, agar dapat menggambar pada window 
# ImageDraw = modul menggambar
# ImageTk = modul untuk mengubah gambar agar bisa dipakai tkinter
# Canvas yang dibuat memakai mode 1(black & white), size (500,500),color = 0(hitam) 
window = tk.Tk()

img = Image.new(mode="1", size=(500, 500), color=0)
tkimage = ImageTk.PhotoImage(img)
canvas = tk.Label(window, image=tkimage)
canvas.pack()

# Membuat kuas untuk menggambar
draw = ImageDraw.Draw(img)
last_point = (0, 0)
prediction = tk.StringVar()
label = tk.Label(window, textvariable=prediction)

def draw_image(event):
    global last_point, tkimage, prediction
    current_point = (event.x, event.y)
    draw.line([last_point, current_point], fill=255, width=30)
    last_point = current_point
    tkimage = ImageTk.PhotoImage(img)
    canvas['image'] = tkimage
    canvas.pack() 
    # Menampilkan text hasil prediksi AI
    img_temp = img.resize((28, 28))
    img_temp = np.array(img_temp)
    img_temp = img_temp.flatten()
    output = model.predict([img_temp])
    if(output[0] == 0):
        prediction.set("kotak")
    elif(output[0] == 1):
        prediction.set("lingkaran")
    else:
        prediction.set("segitiga")
    label.pack()

# Membuat titik awal dan titik akhir dari sebuah gambar
def start_draw(event):
    global last_point
    last_point = (event.x, event.y)

# Membuat tombol reset canvas agar bisa digunakan untuk menggambar gambar baru
def reset_canvas(event):
    global tkimage, img, draw
    img = Image.new(mode="1", size=(500, 500), color=0)
    draw = ImageDraw.Draw(img)
    tkimage = ImageTk.PhotoImage(img)
    canvas['image'] = tkimage
    canvas.pack()

# Membuat char save atau huruf untuk menyimpan masing masing sample yang dibuat 
# k = kotak, l = lingkaran, dan s = segitiga
# Membuat data sample masing masing bentuk sebanyak 10
kotak = 0
lingkaran = 0
segitiga = 0

def save_image(event):
    global kotak, lingkaran, segitiga
    img_temp = img.resize((28, 28))
    if(event.char == "k"):
        img_temp.save(f"kotak/{kotak}.png")
        kotak += 1
    elif(event.char == "l"):
        img_temp.save(f"lingkaran/{lingkaran}.png")
        lingkaran += 1
    elif(event.char == "s"):
        img_temp.save(f"segitiga/{segitiga}.png")
        segitiga += 1

window.bind("<B1-Motion>", draw_image)
window.bind("<ButtonPress-1>", start_draw)
window.bind("<ButtonPress-3>", reset_canvas)
window.bind("<Key>", save_image)

label.pack()

window.mainloop()