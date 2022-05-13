# 1366x768
# FOOTYFIT
# ENJOY THE GAME !!!!

from time import sleep
from tkinter import Button, Entry, PhotoImage, StringVar, \
    Tk, Canvas, Widget, font, messagebox, filedialog
from random import randint
from tkinter.constants import ALL, BOTH, CENTER, END, HIDDEN, NW, TRUE


# Defining user control
def leftKey(event):
    global direction
    direction = "left"


def rightKey(event):
    global direction
    direction = "right"


def upKey(event):
    global direction
    direction = "up"


def downKey(event):
    global direction
    direction = "down"


def quit_game(event):
    global window
    window.destroy()


def pause(event):
    global run, pause_text, wc, hc, btn9
    if run is False:
        run = True
        canvas.delete(pause_text)
        Button.destroy(btn9)
        canvas.after(speed*3 + 70, p1_move)
        canvas.after(speed, movebot)
    else:
        run = False
        pause_text = canvas.create_text(wc/2, hc/2,
                                        font='Times 20 italic bold',
                                        text="Press 'P' to resume",
                                        fill='white')
        btn9 = Button(window, text="Save Game", font=("Arial", 15),
                      command=lambda: savefile(), background="#ffff4d",
                      activeforeground="red")
        btn9.place(x=wc/2 - 60, y=hc/2 + 20)


def bosskey(event):
    global bimage, wc, hc, run, bkey_display
    if run is False:
        run = True
        canvas.delete(bkey_display)
        canvas.after(speed*3 + 70, p1_move)
        canvas.after(speed, movebot)
    else:
        run = False
        bkey_display = canvas.create_image(0, 0, anchor='nw', image=bimage)


def player_switch_r(event):
    global image_switch, p1, messi
    messi = False
    canvas.itemconfigure(p1, image=image_switch)
    window.update()


def player_switch_m(event):
    global img, p1, messi
    messi = True
    canvas.itemconfigure(p1, image=img)
    window.update()


def speed_bot_fast(event):
    global speed_bot
    if speed_bot < 8:
        speed_bot += 1
    window.update()


def speed_bot_slow(event):
    global speed_bot
    if speed_bot > 0:
        speed_bot -= 1
    window.update()


# Movement of food objects
def movebot():
    global x, y, junkbots, hc, wc, healthybots, xx, yy, beerbots, xxx, yyy, run
    pos = list()
    hpos = list()
    while run is True:

        # movement of junkfood
        for i in range(len(junkbots)):
            pos = canvas.bbox(junkbots[i])
            if pos[3] > hc or pos[1] < 0:
                y[i] = -y[i]
            if pos[2] > wc or pos[0] < 0:
                x[i] = -x[i]
            for j in range(len(junkbots)):
                if j == i:
                    continue
                pos2 = canvas.bbox(junkbots[j])
                if (pos[0] < pos2[2] and pos[2] > pos2[0] and
                        pos[1] < pos2[3] and pos[3] > pos2[1]):
                    y[i] = -y[i]
                    x[i] = -x[i]
                    y[j] = -y[j]
                    x[j] = -x[j]

            canvas.move(junkbots[i], x[i], y[i])
        sleep(0.002)
        window.update()

        # movement of healthy food
        for i in range(len(healthybots)):
            hpos = canvas.bbox(healthybots[i])
            if hpos[3] > hc or hpos[1] < 0:
                yy[i] = -yy[i]
            if hpos[2] > wc or hpos[0] < 0:
                xx[i] = -xx[i]
            for j in range(len(healthybots)):
                if j == i:
                    continue
                hpos2 = canvas.bbox(healthybots[j])
                if (hpos[0] < hpos2[2] and hpos[2] > hpos2[0] and
                        hpos[1] < hpos2[3] and hpos[3] > hpos2[1]):
                    yy[i] = -yy[i]
                    xx[i] = -xx[i]
                    yy[j] = -yy[j]
                    xx[j] = -xx[j]
            canvas.move(healthybots[i], xx[i], yy[i])
        sleep(0.002)
        window.update()

        # movement of beer
        for i in range(len(beerbots)):
            bpos = canvas.bbox(beerbots[i])
            if bpos[3] > hc or bpos[1] < 0:
                yyy[i] = -yyy[i]
            if bpos[2] > wc or bpos[0] < 0:
                xxx[i] = -xxx[i]
            for j in range(len(beerbots)):
                if j == i:
                    continue
                bpos2 = canvas.bbox(beerbots[j])
                if (bpos[0] < bpos2[2] and bpos[2] > bpos2[0] and
                        bpos[1] < bpos2[3] and bpos[3] > bpos2[1]):
                    yyy[i] = -yyy[i]
                    xxx[i] = -xxx[i]
                    yyy[j] = -yyy[j]
                    xxx[j] = -xxx[j]
            canvas.move(beerbots[i], xxx[i], yyy[i])
        sleep(0.002)
        window.update()

        # collision detection of junk and healthy
        for i in range(len(junkbots)):
            uhpos = canvas.bbox(junkbots[i])
            for j in range(len(healthybots)):
                htpos = canvas.bbox(healthybots[j])
                if (uhpos[0] < htpos[2] and uhpos[2] > htpos[0] and
                        uhpos[1] < htpos[3] and uhpos[3] > htpos[1]):
                    x[i] = -x[i]
                    y[i] = -y[i]
                    yy[j] = -yy[j]
                    xx[j] = -xx[j]
                    canvas.move(healthybots[j], xx[j], yy[j])
                    canvas.move(junkbots[i], x[i], y[i])
                    sleep(0.002)
                    window.update()

        # collision detection of junk and beer
        for i in range(len(junkbots)):
            unhpos = canvas.bbox(junkbots[i])
            for j in range(len(beerbots)):
                btpos = canvas.bbox(beerbots[j])
                if (unhpos[0] < btpos[2] and unhpos[2] > btpos[0] and
                        unhpos[1] < btpos[3] and unhpos[3] > btpos[1]):
                    x[i] = -x[i]
                    y[i] = -y[i]
                    yyy[j] = -yyy[j]
                    xxx[j] = -xxx[j]
                    canvas.move(beerbots[j], xxx[j], yyy[j])
                    canvas.move(junkbots[i], x[i], y[i])
                    sleep(0.002)
                    window.update()

        # collision detection of healthy and beer
        for i in range(len(healthybots)):
            hunhpos = canvas.bbox(healthybots[i])
            for j in range(len(beerbots)):
                bbtpos = canvas.bbox(beerbots[j])
                if (hunhpos[0] < bbtpos[2] and hunhpos[2] > bbtpos[0] and
                        hunhpos[1] < bbtpos[3] and hunhpos[3] > bbtpos[1]):
                    xx[i] = -xx[i]
                    yy[i] = -yy[i]
                    yyy[j] = -yyy[j]
                    xxx[j] = -xxx[j]
                    canvas.move(beerbots[j], xxx[j], yyy[j])
                    canvas.move(healthybots[i], xx[i], yy[i])
                    sleep(0.002)
                    window.update()


# eating the food
def overlapping(a, b):
    global junkbots, score, wc, hc, lives, run, img7, healthybots,\
        beerbots, speed_bot, p1, sm_image, img, messi, sr_image, image_switch

    for i in range(len(b)):
        x3 = randint(60, wc-50)
        y3 = randint(60, hc-50)
        x4 = randint(60, wc-50)
        y4 = randint(60, hc-50)
        x5 = randint(60, wc-50)
        y5 = randint(60, hc-50)
        food = b[i]
        post = canvas.bbox(b[i])
        if (a[0] < post[2] and a[2] > post[0] and
                a[1] < post[3] and a[3] > post[1]):  # collision detection

            canvas.move(food, post[0]*(-1), post[1]*(-1))
            canvas.move(food, x3, y3)

            # changing scores and lives
            if b == junkbots:
                score += -10
                canvas.itemconfig(scoreText, text="Score:" + str(score))
                if score < 0:
                    canvas.itemconfig(scoreText,
                                      text="Score:" + str(score), fill="red")
                    if messi:
                        canvas.itemconfig(p1, image=sm_image)
                    else:
                        canvas.itemconfig(p1, image=sr_image)

            elif b == healthybots:
                score += 20
                canvas.itemconfigure(scoreText, text="Score:" + str(score))
                if score >= 0:
                    canvas.itemconfigure(scoreText,
                                         text="Score:" + str(score),
                                         fill="white")
                    if messi:
                        canvas.itemconfig(p1, image=img)
                    else:
                        canvas.itemconfig(p1, image=image_switch)
                if score >= 200 and len(beerbots) == 2:
                    canvas.move(healthybots[0], -1000, -1000)
                    beerbots.append(canvas.create_image(x4, y4,
                                                        image=img6,
                                                        tag="food"))
                    junkbots.append(canvas.create_image(x5, y5, image=img7))
                if score >= 300:
                    canvas.itemconfigure(scoreText,
                                         text="Score:" + str(score),
                                         fill="#FFD700")
                    if len(beerbots) == 3:
                        canvas.move(healthybots[2], -1000, -1000)
                        beerbots.append(canvas.create_image(x4, y4,
                                                            image=img6,
                                                            tag="food"))
                        beerbots.append(canvas.create_image(x4, y4,
                                                            image=img6,
                                                            tag="food"))
                        speed_bot += 2

            elif b == beerbots:
                lives += -1
                canvas.itemconfigure(livesText, text="Lives:" + str(lives))
                if lives == 0:
                    run = False
                    game_over()

        window.update()


# Game Over; Option to Restart or Quit Game
def game_over():
    global run, score, final_score, btn11
    if run is False:
        canvas.create_text(wc/2, hc/2, font='Terminal 50 bold',
                           text='GAME OVER', fill='red')
        canvas.create_text(wc/2 + 1, hc/2 + 40, font='Terminal 25',
                           text="Press SPACE to restart", fill='white')
        canvas.create_text(wc/2 - 5, hc/2 + 70, font='Terminal 25',
                           text="Press Q to quit", fill='white')
        final_score = str(score)
        leaderboard()
        try:
            Button.destroy(btn11)
        except:
            pass
        window.bind('<space>', restart)
        window.bind('<q>', quit_game)
        canvas.bind("<b>", bosskey)


# User's Player Motion
def p1_move():
    if run:
        positions = []
        positions.append(canvas.coords(p1))
        # making player appear in screen from opposite end
        global wc, hc, junkbots, speed
        if positions[0][0] < 0:
            canvas.coords(p1, wc, positions[0][1])
        elif positions[0][0] > wc:
            canvas.coords(p1, 0-15, positions[0][1])
        elif positions[0][1] > hc:
            canvas.coords(p1, positions[0][0], 0 - 15)
        elif positions[0][1] < 0:
            canvas.coords(p1, positions[0][0], hc)
        positions.clear()
        positions.append(canvas.coords(p1))
        # moving player here using keyboard
        if direction == "left":
            canvas.move(p1, -20, 0)
        elif direction == "right":
            canvas.move(p1, 20, 0)
        elif direction == "up":
            canvas.move(p1, 0, -20)
        elif direction == "down":
            canvas.move(p1, 0, 20)
        window.after(speed, p1_move)

        # eating of food
        p1box = canvas.bbox(p1)
        overlapping(p1box, junkbots)
        overlapping(p1box, healthybots)
        overlapping(p1box, beerbots)


# some cheat codes
def increase_speed(event):
    global speed
    if speed > 0:
        speed -= 10
    else:
        decrease_speed_()


def decrease_speed_():
    global speed
    if speed < 100:
        speed += 10
    else:
        speed = 100


def decrease_speed(event):
    global speed
    if speed < 100:
        speed += 10
    else:
        speed = 100


def live_increase(event):
    global lives, canvas
    lives += 1
    canvas.itemconfigure(livesText, text="Lives:" + str(lives))
    window.update()


def no_beer(event):
    for i in range(len(beerbots)):
        post = canvas.bbox(beerbots[i])
        food = beerbots[i]
        a = randint(70, 1300)
        b = randint(70, 700)
        canvas.move(food, post[0]*(-2), post[1]*(-2))


# setting up the window
def setWindowDimensions(w, h):
    window = Tk()
    window.title("F O O T Y F I T")
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)  # calculate centre
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))  # window size
    return window


# restarting game
def restart(event):
    global score, lives, run, canvas
    canvas.delete(ALL)
    window.destroy()
    score = 0
    lives = 0
    run = True
    game()


# running of the main game
def startgame():
    global canvas, pause_text, speed, messi, wc, hc,\
            bkey_display, btn9, bimage, p1, image_switch,\
            window, img, sm_image, sr_image, speed_bot, junkbots,\
            y, x, healthybots, yy, xx, yyy, xxx, beerbots, scoreText,\
            livesText, run, direction, lives, img2, img3,\
            img4, img5, img6, img7, score
    width = 1366
    height = 768
    canvas = Canvas(window, bg="black", width=width, height=height)
    canvas.pack(fill=BOTH, expand=True)
    bimage = PhotoImage(file="Graphic/bkey.gif")

    # setting bg
    image_bg = PhotoImage(file="Graphic/chalkb.gif")
    canvas.create_image(0, 0, image=image_bg, anchor="nw")

    wc = 1366
    hc = 768
    txt = "Score:" + str(score)
    scoreText = canvas.create_text(wc/2, 10, fill="white",
                                   font="Times 20 italic bold", text=txt)
    image_switch = PhotoImage(file="Graphic/h_r.gif")
    sr_image = PhotoImage(file="Graphic/s_r.gif")
    sm_image = PhotoImage(file="Graphic/s_m.gif")
    img = PhotoImage(file="Graphic/h_m.gif")
    p1 = canvas.create_image(400, 300, anchor=NW,  image=img)
    livesText = canvas.create_text(wc/2, 30, fill="white",
                                   font="Times 20 italic bold",
                                   text="Lives:" + str(lives))

    # junk section
    img2 = PhotoImage(file="Graphic/lapizza.gif")
    img3 = PhotoImage(file="Graphic/coke.gif")
    img7 = PhotoImage(file="Graphic/burger.gif")
    junkbots = list()
    for i in range(2):
        x1 = randint(50, wc-50)
        y1 = randint(50, hc-50)
        junkbots.append(canvas.create_image(x1, y1, image=img2, tag="food"))
    for i in range(3):
        x1 = randint(50, wc-50)
        y1 = randint(50, hc-50)
        junkbots.append(canvas.create_image(x1, y1, image=img3, tag="food"))

    speed_bot = 2

    x = [speed_bot] * 10
    y = [speed_bot] * 10

    # healthy sec
    img4 = PhotoImage(file="Graphic/apple.gif")
    img5 = PhotoImage(file="Graphic/banana.gif")
    healthybots = list()
    for i in range(2):
        x1 = randint(70, wc-50)
        y1 = randint(70, hc-50)
        healthybots.append(canvas.create_image(x1, y1, image=img4, tag="food"))
    for i in range(2):
        x1 = randint(70, wc-50)
        y1 = randint(70, hc-50)
        healthybots.append(canvas.create_image(x1, y1, image=img5, tag="food"))
    xx = [speed_bot] * 10
    yy = [speed_bot] * 10

    # alcohol
    img6 = PhotoImage(file="Graphic/covbeer.gif")
    beerbots = list()
    for i in range(2):
        x1 = randint(70, wc-50)
        y1 = randint(70, hc-50)
        beerbots.append(canvas.create_image(x1, y1, image=img6, tag="food"))

    xxx = [speed_bot] * 10
    yyy = [speed_bot] * 10
    run = True
    speed = 60

    # binding keys
    canvas.bind("<Left>", leftKey)
    canvas.bind("<Right>", rightKey)
    canvas.bind("<Up>", upKey)
    canvas.bind("<Down>", downKey)
    canvas.bind("<p>", pause)
    canvas.bind("<b>", bosskey)
    canvas.bind("<q>", quit_game)
    pause_text = ""
    btn9 = ""
    bkey_display = ""
    direction = "right"

    # cheat sheet
    canvas.bind("<l>", increase_speed)
    canvas.bind("<k>", decrease_speed)
    canvas.bind("<r>", player_switch_r)
    canvas.bind("<m>", player_switch_m)
    canvas.bind("<n>", no_beer)
    canvas.bind("<h>", speed_bot_fast)
    canvas.bind("<g>", speed_bot_slow)
    canvas.bind("1", live_increase)

    # default
    messi = True
    canvas.focus_set()
    p1_move()
    window.after(2000)
    movebot()

    window.mainloop()


def clearr(window):
    listval = window.winfo_children()

    for item in listval:
        if item.winfo_children():
            listval.extend(item.winfo_children())
    for items in listval:
        items.pack_forget()


# The GAME
def game():
    global window, canvass, btn1, btn2, btn3, btn4, manager, star, width
    width = 1366
    height = 768
    window = setWindowDimensions(width, height)
    window.resizable(width=False, height=False)
    canvass = Canvas(window, bg="black", width=width, height=height)
    canvass.pack(fill=BOTH, expand=True)
    mainmenu()
    window.mainloop()


# Main Menu
def mainmenu():
    global window, canvass, btn1, btn2, btn3, btn4, btn10,\
           manager, star, width, score, lives

    try:
        Button.destroy(btn11)
    except:
        pass

    # default variables
    score = 0
    lives = 2

    # setting up background using shapes
    star = list()
    c = ["white", "#dfdfdf", "#fefefe"]

    for i in range(500):
        x = randint(1, 1366)
        y = randint(1, 768)
        size = randint(1, 4)
        f = randint(0, 2)
        xy = (x, y, x + size, y + size)
        stars = canvass.create_oval(xy, fill=c[f])
        star.append(stars)

    # structuring main menu
    canvass.create_text(width/2, 50, fill="red",
                        font="Times 80 italic bold", text="FOOTYFIT")
    btn1 = Button(window, text="Start Game", font=("Arial", 50),
                  command=lambda: clicked(),
                  background="#ffff4d", width=10, activeforeground="red")
    btn1.place(x=580, y=150)
    btn2 = Button(window, text="Instructions", font=("Arial", 50),
                  command=lambda: inst1(), background="#ffff4d",
                  width=10, activeforeground="red")
    btn2.place(x=580, y=275)
    btn3 = Button(window, text="Leaderboard", font=("Arial", 50),
                  command=lambda: creating_leaderboard_dict(),
                  background="#ffff4d", width=10, activeforeground="red")
    btn3.place(x=580, y=400)
    btn4 = Button(window, text="Exit Game", font=("Arial", 50),
                  command=window.destroy, background="#ffff4d",
                  width=10, activeforeground="red")
    btn4.place(x=580, y=650)
    btn10 = Button(window, text="Load Game", font=("Arial", 50),
                   command=lambda: openfile(), background="#ffff4d",
                   width=10, activeforeground="red")
    btn10.place(x=580, y=525)
    manager = PhotoImage(file="Graphic/boss.gif")
    canvass.bind("<b>", bosskey)


# when start game is clicked
def clicked():
    global window, canvass, btn1, btn2, btn3, btn4, manager,\
           e, star, width, player_name, btn5, btn6

    # deleting all buttons
    canvass.delete(ALL)
    canvass.create_text(width/2, 50, fill="red",
                        font="Times 80 italic bold", text="FOOTYFIT")
    Button.destroy(btn1)
    Button.destroy(btn2)
    Button.destroy(btn3)
    Button.destroy(btn4)
    Button.destroy(btn10)

    # title
    canvass.create_image(1366/2, 200, image=manager)
    # body
    welcome_text = canvass.create_text(700, 350,
                                       text=("Hello there!! My name is Rushil"
                                             "Dhanuka and "
                                             "I'm the manager of "
                                             "Krillford FC."),
                                       font="Times 20 italic bold",
                                       tags="h", fill="white")
    intro_text = canvass.create_text(690, 370,
                                     text=("Thank you for applying for vacant"
                                           "Club Nutritionist role. "
                                           "Uhh... What was your name again?"),
                                     font="Times 20 italic bold",
                                     tags="h", fill="white")
    e = Entry(window, width=30, fg="black", bg="white", justify=CENTER)
    e.place(x=520, y=400)
    e.insert(0, "Enter Your Name-")
    player_name = ""
    btn5 = Button(window, text="Next", font=("Arial", 10),
                  command=lambda: game_go(), background="#ffff4d",
                  width=2, height=2, activeforeground="red")
    btn6 = Button(window, text="Back", font=("Arial", 20),
                  command=lambda: back1(), background="#ffff4d",
                  width=10, activeforeground="red")
    btn5.place(x=790, y=397)
    btn6.place(x=100, y=700)


def game_go():
    global window, canvass, e, p1_name, btn7
    player_name = e.get()
    p1_name = player_name
    canvass.create_text(680, 500,
                        text=("Glad To have you "
                              "on board Mr/Mrs ") + player_name + "!!",
                        font="Times 20 italic bold",
                        tags="h", fill="white")
    btn7 = Button(window, text="Start Game",
                  font=("Arial", 20), command=lambda: game_start(),
                  background="#ffff4d", width=10,
                  activeforeground="red")
    btn7.place(x=1150, y=690)


def back1():
    global btn11
    canvass.itemconfigure("h", state=HIDDEN)
    try:
        Button.destroy(btn5)
        Button.destroy(btn6)
        Entry.destroy(e)
    except:
        pass
    try:
        Button.destroy(btn7)
    except:
        pass
    try:
        Button.destroy(btn8)
    except:
        pass
    try:
        Button.destroy(btn11)
    except:
        pass
    try:
        Button.destroy(btn11)
    except:
        pass

    mainmenu()


# Instruction Functions
def inst1():
    global btn11, intro1
    canvass.delete(ALL)
    canvass.create_text(width/2, 50, fill="red",
                        font="Times 80 italic bold", text="FOOTYFIT")
    Button.destroy(btn1)
    Button.destroy(btn2)
    Button.destroy(btn3)
    Button.destroy(btn4)
    Button.destroy(btn10)
    intro1 = PhotoImage(file="Graphic/Intro1.png")
    sh = canvass.create_image(0, 0, image=intro1, anchor=NW, tags="h")
    btn11 = Button(window, text="Back", font=("Arial", 20),
                   command=lambda: back1(), background="#ffff4d",
                   width=10, activeforeground="red")
    btn11.place(x=100, y=700)
    canvass.bind("<Right>", inst2)
    canvass.bind("<Left>", nothin)
    canvass.focus_set()


# had to create this function to fix bug
def nothin(event):
    pass


def inst1_(event):
    inst1()


def inst2(event):
    global intro2
    try:
        Button.destroy(btn11)
    except:
        pass
    canvass.delete(ALL)
    intro2 = PhotoImage(file="Graphic/Intro2.png")
    canvass.create_image(0, 0, image=intro2, anchor=NW, tags="h")
    canvass.bind("<Left>", inst1_)
    canvass.bind("<Right>", inst3)
    canvass.focus_set()


def inst3(event):
    global intro3
    try:
        Button.destroy(btn11)
    except:
        pass
    canvass.delete(ALL)
    intro3 = PhotoImage(file="Graphic/Intro3.png")
    canvass.create_image(0, 0, image=intro3, anchor=NW, tags="h")
    canvass.bind("<Left>", inst2)
    canvass.bind("<Right>", inst4)
    canvass.focus_set()


def inst4(event):
    global intro4
    try:
        Button.destroy(btn11)
    except:
        pass

    canvass.delete(ALL)
    intro4 = PhotoImage(file="Graphic/Intro4.png")
    canvass.create_image(0, 0, image=intro4, anchor=NW, tags="h")
    canvass.bind("<Left>", inst3)
    canvass.focus_set()


# making the leaderboard
def leaderboard():
    global player_name, final_score
    lbfile = open("Graphic/leaderboard.txt", "a")
    inputv = p1_name + ":" + final_score + "\n"
    lbfile.write(inputv)
    lbfile.close()
    creating_leaderboard_dict()


def creating_leaderboard_dict():
    global tmp, btn8, leaderimg

    canvass.delete(ALL)
    canvass.create_text(width/2, 50, fill="red",
                        font="Times 80 italic bold", text="FOOTYFIT", tags="h")

    leaderimg = PhotoImage(file="Graphic/leader.gif")
    canvass.create_image(width/2, 240, image=leaderimg, tag="h")

    btn8 = Button(window, text="Back", font=("Arial", 20),
                  command=lambda: back1(), background="#ffff4d",
                  width=10, activeforeground="red")
    btn8.place(x=100, y=700)

    Button.destroy(btn1)
    Button.destroy(btn2)
    Button.destroy(btn3)
    Button.destroy(btn4)
    Button.destroy(btn10)

    canvass.create_text(width/2, 150, fill="yellow",
                        font="Times 40 italic bold",
                        text="LEADERBOARD", tags="h")

    # outputting leaderboad on canvas
    # reading into file

    dic = dict()
    # inserting player name and score in dictionary
    with open("Graphic/leaderboard.txt") as f:
        for line in f:
            (key, val) = line.split(":")
            dic[key] = int(val)

    tmp = list()

    # converting to tuples to sort
    for k, v in dic.items():
        tmp.append((v, k))
    tmp = sorted(tmp, reverse=True)
    yval = 350
    n = 1

    # outputting top 10
    for val, key in tmp[:10]:
        canvass.create_text(width/2, yval,
                            text=str(n) + ". " + key + " : " + str(val),
                            fill="red", font="Times 30 italic bold", tags="h")
        yval += 30
        n += 1


# SAVE game feature
def savefile():

    # allowing user to select name and destination
    file_name = filedialog.asksaveasfilename(initialdir="Graphic/data",
                                             title="Save Game",
                                             filetypes=(("Text Files",
                                                         "*.txt"),
                                                        ("All Files", "*.*")))
    if file_name:
        if file_name.endswith(".txt"):
            pass
        else:
            file_name = f'{file_name}.txt'

        # writing data in file
        output_file = open(file_name, "w")
        savevar = p1_name + "," + str(score) + "," + str(lives)
        output_file.write(savevar)
        output_file.close()

        canvas.bind("<p>", pause)
    else:
        canvas.bind("<p>", pause)


# LOAD game feature
def openfile():
    global p1_name, score, lives

    # allowing user to search file
    file_name = filedialog.askopenfilename(initialdir="Graphic/data",
                                           title="Load Game",
                                           filetypes=(("Text Files", "*.txt"),
                                                      ("All Files", "*.*")))

    # taking data out
    if file_name:
        input_file = open(file_name, "r")
        dat = input_file.read()
        datlist = dat.split(",")
        p1_name = datlist[0]
        score = int(datlist[1])
        lives = int(datlist[2])
        game_start()


# clearing canvas and starting game
def game_start():
    global window
    clearr(window)
    startgame()


# quit game
def exitt():
    window.destroy()


# calling function to run game
game()

# Hope you enjoyed the game !!!
