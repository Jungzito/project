import tkinter
import tkinter.messagebox
import random

key = 0
mx = 1
my = 1
yuka = 0

root = tkinter.Tk()

def info():
    tkinter.messagebox.showinfo("정보", "이동키:화살표로 이동\n왼쪽 쉬프트:다시시작\nESC:종료")

def key_down(e):
    global key
    key = e.keysym

def key_up(e):
    global key
    key = ""

def reset():
    global mx, my, yuka
    canvas.delete("PAINT")
    mx = 1
    my = 1
    yuka = 0
    for y in range(7):
        for x in range(10):
            if maze[y][x] == 2:
                maze[y][x] = 0

def main_proc():
    global mx, my, yuka
    
    if key == "Escape":
        root.destroy()
        return ;
    if key == "Shift_L" and yuka > 1:
        reset()
    if key == "Up" and maze[my-1][mx] == 0: 
        my -= 1
    if key == "Down" and maze[my+1][mx] == 0:
        my += 1
    if key == "Left" and maze[my][mx-1] == 0:
        mx -= 1
    if key == "Right" and maze[my][mx+1] == 0:
        mx += 1    
        
    if maze[my][mx] == 0:
        maze[my][mx] = 2
        yuka += 1
        canvas.create_rectangle(mx*80, my*80, mx*80 + 79, my*80 + 79, 
                                   fill="pink", width=0, tag="PAINT")
    canvas.delete("MYCHR")
    canvas.create_image(mx*80 + 40, my*80 + 40, image=img, tag="MYCHR")
     
    if yuka == 30:
        canvas.update()
        tkinter.messagebox.showinfo("축하합니다!", "모든 바닥을 칠했습니다!")
        reset()
        
    elif 0 not in [maze[my-1][mx], maze[my+1][mx], maze[my][mx-1], maze[my][mx+1]]:
        tkinter.messagebox.showinfo("망했어요!", "클리어가 불가능합니다\n 다시 시작하세요!")
        reset()
    root.after(100, main_proc)
                            

root = tkinter.Tk()
root.title("테스트 작업")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=800, height=560, bg="white")
canvas.pack()

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            canvas.create_rectangle(x * 80, y * 80, x * 80 + 79, y * 80 + 79, fill="skyblue", width=0)

img = tkinter.PhotoImage(file="miro_y.png")
canvas.create_image(mx * 80 + 40, my * 80 + 40, image=img, tag="MYCHR")
btn = tkinter.Button(root, command=info, text="조작키와 정보")
btn.place(x=3, y=5)
main_proc()
root.mainloop()