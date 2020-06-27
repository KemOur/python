import random
import curses

#initialisation de l écran
#le curses est a zero
s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
#création d'une nouvelle fênetre
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)
#position initial du snake
snk_x = sw/4
snk_y = sh/2
#création du snake
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]
#nourriture mangé par le snake, se trouvera au millieu de l'écran achaque début du jeu
food = [sh/2, sw/2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key
#condition pour la définition de la façon dont le joueur peut perdre!
    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
#création d'un nouvel snake
    new_head = [snake[0][0], snake[0][1]]
#mouvements du snake
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
#insertion du snake
    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            #création d'une nouvelle nourriture
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)