import tkinter
import tkinter.messagebox
import random
from tkinter import *

root = tkinter.Tk()
root.title("종합게임팩")
root.geometry("1280x720")

mx = 1
my = 1
yuka = 0
key = 0

def fri():

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
            canvas.create_rectangle(mx*80, my*80, mx*80 + 79, my*80 + 79, fill="pink", width=0, tag="PAINT")
            canvas.delete("MYCHR")
            canvas.create_image(mx*80 + 40, my*80 + 40, image=img, tag="MYCHR")
    
        if yuka == 30:
            canvas.update()
            tkinter.messagebox.showinfo("축하합니다!", "모든 바닥을 칠했습니다!")
            reset()
        
        elif 0 not in [maze[my-1][mx], maze[my+1][mx], maze[my][mx-1], maze[my][mx+1]]:
            tkinter.messagebox.showinfo("망했어요!", "클리어가 불가능합니다\n 다시 시작합니다")
            reset()
        root.after(100, main_proc)
                            
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
    btn.place(x=5, y=5)
    main_proc()

def sec():
      
    def main():
        """컴퓨터와 배틀하는 턴제게임"""

        name=input("플레이어의 이름을 입력하세요:")

        play_again = True

        while play_again:
            winner = None
            player_health = 100
            computer_health = 100

            turn = random.randint(1,2)
            if turn == 1:
                player_turn = True
                computer_turn = False
                print(name ,"가 먼저.")
            else:
                player_turn = False
                computer_turn = True
                print("\n컴퓨터가 먼저.")

            print(name ,"의 체력: ", player_health, "컴퓨터 체력: ", computer_health)

            while (player_health != 0 or computer_health != 0):

                heal_up = False
                miss = False

                moves = {"Punch": random.randint(18, 25),
                        "Mega Punch": random.randint(10, 35),
                        "Heal": random.randint(20, 25)}

                if player_turn:
                    print("\n명령을 입력하시오:\n1. 펀치 (데미지는 18-25)\n2. 핵펀치 (데미지는 10-35)\n3. 힐 (체력 회복은 20-25 )\n")

                    player_move = input("> ").lower()

                    move_miss = random.randint(1,5)
                    if move_miss == 1:
                        miss = True
                    else:
                        miss = False

                    if miss:
                        player_move = 0
                        print("\n실수했다!")
                    else:
                        if player_move in ("1", "punch"):
                            player_move = moves["Punch"]
                            print(name, "이(가) 펀치를 사용했다. 데미지는 ", player_move, " 이다.")
                        elif player_move in ("2", "mega punch"):
                            player_move = moves["Mega Punch"]
                            print(name, "이(가) 핵펀치를 사용했다. 데미지는 ", player_move, " 이다.")
                        elif player_move in ("3", "heal"):
                            heal_up = True
                            player_move = moves["Heal"]
                            print(name, "이(가) 체력회복을 사용했다 회복한 체력은 ", player_move, " 이다.")
                        else:
                            print("\n잘못된 값 다시 입력.")
                            continue
                else:
                    move_miss = random.randint(1,5)
                    if move_miss == 1:
                        miss = True

                    else:
                        miss = False

                    if miss:
                        computer_move = 0
                        print("\n실수했다!")

                    else:
                        if computer_health > 30: 
                            if player_health > 75:
                                computer_move = moves["Punch"]
                                print("\n컴퓨터는 펀치를 사용했다. 데미지는 ", computer_move, " 이다.")
                            elif player_health > 35 and player_health <= 75:
                                imoves = ["Punch", "Mega Punch"]
                                imoves = random.choice(imoves)
                                computer_move = moves[imoves]
                                print("\n컴퓨터는 ", imoves, "를 사용했다 데미지는 ", computer_move, " 이다.")
                            elif player_health <= 35:
                                computer_move = moves["Mega Punch"]
                                print("\n컴퓨터는 핵펀치를 사용했다. 데미지는 ", computer_move, " 이다..")                       
                        else:
                            heal_or_fight = random.randint(1,2) 
                            if heal_or_fight == 1:
                                heal_up = True
                                computer_move = moves["Heal"]
                                print("\n컴퓨터는 체력회복을 사용했다. 회복한 체력은 ", computer_move, " 이다.")
                            else:
                                if player_health > 75:
                                    computer_move = moves["Punch"]
                                    print("\n컴퓨터는 펀치를 사용했다. 데미지는 ", computer_move, " 이다.")
                                elif player_health > 35 and player_health <= 75:
                                    imoves = ["Punch", "Mega Punch"]
                                    imoves = random.choice(imoves)
                                    computer_move = moves[imoves]
                                    print("\n컴퓨터는 ", imoves, "를 사용했다 데미지는 ", computer_move, " 이다.")
                                elif player_health <= 35:
                                    computer_move = moves["Mega Punch"]
                                    print("\n컴퓨터는 핵펀치를 사용했다. 데미지는 ", computer_move, " 이다.")

                if heal_up:
                    if player_turn:
                        player_health += player_move
                        if player_health > 100:
                            player_health = 100
                    else:
                        computer_health += computer_move
                        if computer_health > 100:
                            computer_health = 100
                else:
                    if player_turn:
                        computer_health -= player_move
                        if computer_health <= 0:
                            computer_health = 0
                            winner = "Player"
                            break
                    else:
                        player_health -= computer_move
                        if player_health <= 0:
                            player_health = 0
                            winner = "Computer"
                            break

                print(name, "의 체력: ", player_health, "컴퓨터 체력: ", computer_health)

                player_turn = not player_turn
                computer_turn = not computer_turn

            if winner == "Player":
                print(name, "의 체력: ", player_health, "컴퓨터 체력: ", computer_health)
                print(name, "승리")
            else:
                print(name, "의 체력: ", player_health, "컴퓨터 체력: ", computer_health)
                print("\n컴퓨터 승리.")

            print("\n다시 플레이 하시겠습니까? [y]es, [n]o")

            answer = input("> ").lower()
            if answer not in ("yes", "y"):
                play_again = False
            if answer in ("yes", "y"):
                play_again = True
    main()

def info():
    tkinter.messagebox.showinfo("정보","미로는 새로운 창에서 실행됩니다.\n턴제게임은 터미널에서 실행됩니다.\n미로게임의 조작키는 미로창 왼쪽 상단을 참고하시오.")
 
photo = PhotoImage(file="miro.png")
btn = Button(root, command=fri, image=photo)
btn.place(x=75, y=100) 

photo2 = PhotoImage(file="aii.png")
btn2 = Button(root, command=sec, image=photo2)
btn2.place(x=875, y=100)

photo3 = PhotoImage(file="info.png")
btn3 = Button(root, command=info, image=photo3)
btn3.place(x=575, y=500)

root.mainloop()