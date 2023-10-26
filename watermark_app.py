from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont


# Create a function to add a text watermark to the image
def add_text_watermark():
    input_image_path = input_image_path_var.get()
    output_image_path = output_image_path_var.get()
    watermark_text = watermark_text_entry.get()
    watermark_font = ImageFont.truetype('arial.ttf', 36)  # Change the font and size as needed

    try:
        image = Image.open(input_image_path)
        draw = ImageDraw.Draw(image)
        draw.text((10, 10), watermark_text, fill='red', font=watermark_font)
        image.save(output_image_path)
        messagebox.showinfo(title="Watermark", message="Watermark Added Successfully.")
    except Exception as e:
        messagebox.showerror(title="Error", message=f"Error: {str(e)}")


# Create a function to add an image watermark to the image
def add_image_watermark():
    input_image_path = input_image_path_var.get()
    output_image_path = output_image_path_var.get()
    watermark_image_path = watermark_image_path_var.get()

    try:
        image = Image.open(input_image_path)
        watermark = Image.open(watermark_image_path)
        image.paste(watermark, (0, 0), watermark)
        image.save(output_image_path)
        messagebox.showinfo(title="Watermark", message="Watermark Added Successfully.")
    except Exception as e:
        messagebox.showerror(title="Error", message=f"Error: {str(e)}")


# Create the main application window
app = Tk()
app.title("Image Watermark App")
app.config(padx=100, pady=50, bg="#CDF5FD")

input_image_label = Label(app, text="Select Input Image:", bg="#CDF5FD")
input_image_label.grid(column=0, row=1)

input_image_path_var = StringVar()
input_image_path_entry = Entry(app, textvariable=input_image_path_var)
input_image_path_entry.grid(column=1, row=1)

select_input_image_button = Button(app, text="Browse", command=lambda: input_image_path_var.set(filedialog.askopenfilename()))
select_input_image_button.grid(column=2, row=1)

output_image_label = Label(app, text="Save As:", bg="#CDF5FD")
output_image_label.grid(column=0, row=2)

output_image_path_var = StringVar()
output_image_path_entry = Entry(app, textvariable=output_image_path_var)
output_image_path_entry.grid(column=1, row=2)

watermark_text_label = Label(app, text="Watermark Text:", bg="#CDF5FD")
watermark_text_label.grid(column=0, row=3)

watermark_text_var = StringVar()
watermark_text_entry = Entry(app, textvariable=watermark_text_var)
watermark_text_entry.grid(column=1, row=3)

add_text_watermark_button = Button(app, text="Add Text Watermark", command=add_text_watermark, width=17)
add_text_watermark_button.grid(column=1, row=4)

watermark_image_label = Label(app, text="Select Watermark Image:", bg="#CDF5FD")
watermark_image_label.grid(column=0, row=5)

watermark_image_path_var = StringVar()
watermark_image_path_entry = Entry(app, textvariable=watermark_image_path_var)
watermark_image_path_entry.grid(column=1, row=5)

select_watermark_image_button = Button(app, text="Browse", command=lambda: watermark_image_path_var.set(filedialog.askopenfilename()))
select_watermark_image_button.grid(column=2, row=5)

add_image_watermark_button = Button(app, text="Add Image Watermark", command=add_image_watermark, width=17)
add_image_watermark_button.grid(column=1, row=6)

app.mainloop()
