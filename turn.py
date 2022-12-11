import random


def main():
    """컴퓨터와 배틀하는 턴제게임"""

    play_again = True

    while play_again:
        winner = None
        player_health = 100
        computer_health = 100

        turn = random.randint(1,2)
        if turn == 1:
            player_turn = True
            computer_turn = False
            print("\n플레이어가 먼저.")
        else:
            player_turn = False
            computer_turn = True
            print("\n컴퓨터가 먼저.")


        print("\n플레이어 체력: ", player_health, "컴퓨터 체력: ", computer_health)

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
                    print("맞추지 못했다!")
                else:
                    if player_move in ("1", "punch"):
                        player_move = moves["Punch"]
                        print("\n당신은 펀치를 사용했다. 데미지는 ", player_move, " 이다.")
                    elif player_move in ("2", "mega punch"):
                        player_move = moves["Mega Punch"]
                        print("\n당신은 핵펀치를 사용했다. 데미지는 ", player_move, " 이다.")
                    elif player_move in ("3", "heal"):
                        heal_up = True
                        player_move = moves["Heal"]
                        print("\n당신은 체력회복을 사용했다 회복한 체력은 ", player_move, " 이다.")
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
                    print("맞추지 못했다!")
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
                    if computer_health < 0:
                        computer_health = 0
                        winner = "Player"
                        break
                else:
                    player_health -= computer_move
                    if player_health < 0:
                        player_health = 0
                        winner = "Computer"
                        break

            print("\n플레이어 체력: ", player_health, "컴퓨터 체력: ", computer_health)

            player_turn = not player_turn
            computer_turn = not computer_turn

        if winner == "Player":
            print("\n플레이어 체력: ", player_health, "컴퓨터 체력: ", computer_health)
            print("\n플레이어 승리")
        else:
            print("\n플레이어 체력: ", player_health, "컴퓨터 체력: ", computer_health)
            print("\n컴퓨터 승리.")

        print("\n다시 플레이 하시겠습니까? [y]es, [n]o")

        answer = input("> ").lower()
        if answer not in ("yes", "y"):
            play_again = False

main()