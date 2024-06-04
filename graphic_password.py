from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox

root = Tk()
root.title('Graphic password')
root.configure(bg='lightblue')

root.geometry('800x600')
root.resizable(width=False, height=False)

frame = Frame(root)
frame.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

lable1 = Label(root, text='Choose ten icons', font=20)
lable2 = Label(root, text='Find the icons you chose', font=20)
lable1.pack()

icons_num = []
count = 0


def icon_num(i):
    global count
    if i not in icons_num:
        count += 1
        icons_num.append(i)
    print(i)
    if count == 10:
        clear_frame()
        find_icon()


ch_count = 0
red_point = 0

def check_icon_num(i):
    global ch_count, list_1,red_point

    print("i is: " + str(i))
    print("list 1 :" + str(list_1))

    if i in list_1:
        ch_count += 1
        list_1.remove(i)
        if ch_count == 3:
            messagebox.showinfo("showinfo", "You have successfully logged in")
    else:
        red_point += 1
        messagebox.showwarning("showwarning", "You have just " + str(3 - red_point) + " attempt")
    if red_point == 3:
        messagebox.showerror("showerror", "Incorrect choices")
        clear_frame()
        find_icon()


def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()
    lable1.destroy()
    global click_count
    click_count = 0


icon_paths = ['icons/icons1.png', 'icons/icons2.png', 'icons/icons3.png', 'icons/icons4.png', 'icons/icons5.png',
              'icons/icons6.png', 'icons/icons7.png', 'icons/icons8.png', 'icons/icons9.png', 'icons/icons10.png',
              'icons/icons11.png', 'icons/icons12.png', 'icons/icons13.png', 'icons/icons14.png', 'icons/icons15.png',
              'icons/icons16.png', 'icons/icons17.png', 'icons/icons18.png', 'icons/icons19.png', 'icons/icons20.png',
              'icons/icons21.png', 'icons/icons22.png', 'icons/icons23.png', 'icons/icons24.png', 'icons/icons25.png',
              'icons/icons26.png', 'icons/icons27.png', 'icons/icons28.png', 'icons/icons29.png', 'icons/icons30.png',
              'icons/icons31.png', 'icons/icons32.png', 'icons/icons33.png', 'icons/icons34.png', 'icons/icons35.png']
icons = []
new_icons = []
list_1 = []
for i in range(len(icon_paths)):
    row = i // 7
    col = i % 7
    btn_photo = Image.open(icon_paths[i])
    resize_btn_photo = btn_photo.resize((80, 80))
    btn_photo = ImageTk.PhotoImage(resize_btn_photo)
    icons.append(btn_photo)
    btn = Button(frame, image=btn_photo, borderwidth=1, command=lambda i=i: icon_num(i + 1))
    btn.grid(row=row, column=col, padx=10, pady=10)


def find_icon():
    lable2.pack()

    new_list = []
    global icon_paths
    global list_1
    list_1 = [icon_paths[i - 1] for i in icons_num]
    list_2 = [icon_path for icon_path in icon_paths if icon_path not in list_1]
    list_1 = random.sample(list_1, 3)
    new_list = list_1 + random.sample(list_2, 22)
    random.shuffle(new_list)

    for i in range(len(new_list)):
        row = i // 5
        col = i % 5
        btn_photo1 = Image.open(new_list[i])
        resize_btn_photo = btn_photo1.resize((80, 80))
        btn_photo = ImageTk.PhotoImage(resize_btn_photo)
        new_icons.append(btn_photo)
        new_btn = Button(frame, image=btn_photo, borderwidth=1, command=lambda i=new_list[i]: check_icon_num(i))
        new_btn.grid(row=row, column=col, padx=30, pady=10)


root.mainloop()
