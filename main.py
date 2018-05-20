import keyboard
import math
import time
from random import randint
import gestures
from graphics import *

# 0 = tie, 1 = loss, 2 = tie
#                 r , p , s  
result_table = [ [0 , 1 , 2], # r
                 [2 , 0 , 1], # p
                 [1 , 2 , 0] ]# s

choices = ['r', 'p', 's']

def start(win):
    start_text = Text(Point(300, 100), "Pick a mode")
    start_text.setSize(36)
    normal_mode = Text(Point(150, 250), "Normal")
    normal_mode.setSize(30)
    normal_rect = Rectangle(Point(80,230),Point(230,270))
    impossible_mode = Text(Point(400, 250), "Impossible")
    impossible_mode.setSize(30)
    impossible_rect = Rectangle(Point(300,230),Point(500,270))

    start_text.draw(win)
    normal_mode.draw(win)
    normal_rect.draw(win)
    impossible_mode.draw(win)
    impossible_rect.draw(win)

    while True:
        clickPoint = win.getMouse()
        print(clickPoint)
        if (clickPoint.getX() > 80 and clickPoint.getX() < 230 and
        clickPoint.getY() > 230 and clickPoint.getY() < 270):
            win.delete('all')
            return 'normal'
            break
        if (clickPoint.getX() > 300 and clickPoint.getX() < 500 and
        clickPoint.getY() > 230 and clickPoint.getY() < 270):
            win.delete('all')
            return 'impossible'
            break


def player_move():
    while True:
        log = open("hand_log.txt", 'r')
        choice = log.read()
        if choice in choices:
            return choice 
        else:
            None

def computer_move():
    return randint(0,2)

def result(p, c):
    return result_table[choices.index(p)][c]

def again(win):
    drawAgain = Text(Point(200, 300), "Play Again?")
    drawAgain.setSize(30)
    drawAgain.draw(win)
    
    yes = Text(Point(400,300), "Yes")
    yes.setSize(30)
    yes.draw(win)

    yesBox = Rectangle(Point(350,280), Point(450,320))
    yesBox.draw(win)

    no = Text(Point(500, 300), "No")
    no.setSize(30)
    no.draw(win)

    noBox = Rectangle(Point(450, 280), Point(550, 320))
    noBox.draw(win)

    while True:
        clickPoint = win.getMouse()
        print(clickPoint)
        if (clickPoint.getX() > 350 and clickPoint.getX() < 450 and
        clickPoint.getY() > 280 and clickPoint.getY() < 320):
            win.delete('all')
            return True
            break
        if (clickPoint.getX() > 450 and clickPoint.getX() < 550 and
        clickPoint.getY() > 280 and clickPoint.getY() < 320):
            win.delete('all')
            return False
            break

def normal(win):
    score = [0,0]

    while True:
        win.delete('all')
        time.sleep(2)
        comp = computer_move()

        three = Text(Point(300,75), 'Rock')
        three.setSize(36)
        three.draw(win)
        print("Rock!")
        time.sleep(.75)

        two = Text(Point(300,150), 'Paper')
        two.setSize(36)
        two.draw(win)
        print("Paper!")
        time.sleep(.75)

        one = Text(Point(300,225), 'Scissors')
        one.setSize(36)
        one.draw(win)
        print("Scissors!")
        time.sleep(.75)

        shoot = Text(Point(300,300), 'Shoot!')
        shoot.setSize(36)
        shoot.draw(win) 
        print("Shoot!")
        print()

        time.sleep(2)


        if comp == 0:
            print('rock')
            c = 'rock'
            gestures.rock()
        elif comp == 1:
            print('paper')
            c = 'paper'
            gestures.paper()
        elif comp == 2:
            print('scissors')
            c = 'scissors'
            gestures.scissors()

        player = player_move()
        if player == 'r':
            print('rock')
            p = 'rock'
        elif player == 'p':
            print('paper')
            p = 'paper'
        elif player == 's':
            print('scissors')
            p = 'scissors'

        win.delete('all')

        res = result(player, comp)

        #display results

        p_throw = Text(Point(200,100), "Player: " + p)
        p_throw.setSize(30)
        p_throw.draw(win)

        comp_throw = Text(Point(200, 200), "Computer: " + c)
        comp_throw.setSize(30)
        comp_throw.draw(win)
        
        time.sleep(2)

        print()
        if res == 0:
            disp_res = Text(Point(300, 300), "You Tied!")
            disp_res.setSize(36)
            disp_res.draw(win)
            print("You Tied!")
        elif res == 1:
            disp_res = Text(Point(300, 300), "You Lost!")
            disp_res.setSize(36)
            disp_res.draw(win)
            print("You Lost!")
            score[1] += 1
        else:
            disp_res = Text(Point(300, 300), "You Won!")
            disp_res.setSize(36)
            disp_res.draw(win)
            print("You Won!")
            score[0] += 1
        
        time.sleep(1)
        win.delete('all')
        
        print()
        print("Score")
        drawScore = Text(Point(300, 50), "Score")
        drawScore.setSize(36)
        drawScore.draw(win)
        print("Player: " + str(score[0]))
        drawPscore = Text(Point(300, 150), "Player: " + str(score[0]))
        drawPscore.setSize(30)
        drawPscore.draw(win)
        print("Computer: " + str(score[1]))
        drawCscore = Text(Point(300, 225), "Computer: " + str(score[1]))
        drawCscore.setSize(30)
        drawCscore.draw(win)
        print()

        if not again(win):
            print("Thanks for playing!")
            break
        else:
            None

def impossible(win):
    score = [0,0]

    while True:
        win.delete('all')
        time.sleep(2)

        three = Text(Point(300,75), 'Rock')
        three.setSize(36)
        three.draw(win)
        print("Rock!")
        time.sleep(.5)

        two = Text(Point(300,150), 'Paper')
        two.setSize(36)
        two.draw(win)
        print("Paper!")
        time.sleep(.5)

        one = Text(Point(300,225), 'Scissors')
        one.setSize(36)
        one.draw(win)
        print("Scissors!")
        time.sleep(.5)

        shoot = Text(Point(300,300), 'Shoot!')
        shoot.setSize(36)
        shoot.draw(win) 
        print("Shoot!")
        print()
        for i in range(8):
            time.sleep(.25)

            player = player_move()
            if player == 'r':
                print('rock')
                p = 'rock'
                gestures.paper()
                comp = 1
                c = 'paper'
            elif player == 'p':
                print('paper')
                p = 'paper'
                gestures.scissors()
                comp = 2
                c = 'scissors'
            elif player == 's':
                print('scissors')
                p = 'scissors'
                gestures.rock()
                comp = 0
                c = 'rock'

        time.sleep(2)
        win.delete('all')

        res = result(player, comp)

        #display results

        p_throw = Text(Point(200,100), "Player: " + p)
        p_throw.setSize(30)
        p_throw.draw(win)

        comp_throw = Text(Point(200, 200), "Computer: " + c)
        comp_throw.setSize(30)
        comp_throw.draw(win)
        
        time.sleep(2)

        print()
        if res == 0:
            disp_res = Text(Point(300, 300), "You Tied!")
            disp_res.setSize(36)
            disp_res.draw(win)
            print("You Tied!")
        elif res == 1:
            disp_res = Text(Point(300, 300), "You Lost!")
            disp_res.setSize(36)
            disp_res.draw(win)
            print("You Lost!")
            score[1] += 1
        else:
            disp_res = Text(Point(300, 300), "You Won!")
            disp_res.setSize(36)
            disp_res.draw(win)
            print("You Won!")
            score[0] += 1
        
        time.sleep(1)
        win.delete('all')
        
        print()
        print("Score")
        drawScore = Text(Point(300, 50), "Score")
        drawScore.setSize(36)
        drawScore.draw(win)
        print("Player: " + str(score[0]))
        drawPscore = Text(Point(300, 150), "Player: " + str(score[0]))
        drawPscore.setSize(30)
        drawPscore.draw(win)
        print("Computer: " + str(score[1]))
        drawCscore = Text(Point(300, 225), "Computer: " + str(score[1]))
        drawCscore.setSize(30)
        drawCscore.draw(win)
        print()

        time.sleep(1)

        if not again(win):
            print("Thanks for playing!")
            break
        else:
            None


def main():
    win = GraphWin("Rock Paper Scissors", 600, 400)
    while True:
        level = start(win)
        if level == "normal":
            normal(win)
            break
        elif level == "impossible":
            impossible(win)

    


    
if __name__ == "__main__":
    main()



