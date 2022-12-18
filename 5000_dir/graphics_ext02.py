from tkinter import *

def DrawNetwork(layers):

    width = 1366
    height = 768
    parts_w = int(width / len(layers))
    parts_h = 0
    x = int(parts_w/2)
    y = 0
    win = Tk()
    win.attributes('-fullscreen', True)
    scale01 = str(width) + "x" + str(height)
    win.geometry(scale01)
    canv = Canvas(win, width=width, height=height)
    canv.pack()


    table01 = []
    for layer in range(len(layers)):
        temp_list01 = []
        if layers[layer] >= 10:
            y = int((height / layers[layer])/1.4)
        else:
            y = int((height / layers[layer])/2)
        for item in range(layers[layer]):
            parts_h = int(height / layers[layer])
            if layers[layer] == 1:
                y = height / 2
            temp_list02 = [x, y]  # draw circle
            if layers[layer] != 1:
                y += parts_h
            temp_list01.append(temp_list02)
        table01.append(temp_list01)
        x += parts_w

    cRad = 13

    for a in range(len(layers)):
        cRad = 15

        #if layers[a] <= 5:
        #    cRad = 20
        #elif layers[a] <= 10:
        #    cRad = 15
        #elif layers[a] <= 20:
        #    cRad = 12
        #else:
        #    cRad = 8
        for b in range(layers[a]):

            if a == 0:
                filler = "red"
            elif a <= len(layers)-2:
                filler = "blue"
            else:
                filler = "green"
            if b==0:
                title = "L" + str(a+1)
                if layers[a] > 9:
                    canv.create_text(table01[a][b][0], table01[a][b+1][1]-int( (width/layers[a]/2)/1.5  ), fill=filler, font="Consolas", text=title, anchor="w")
                else:
                    canv.create_text(table01[a][b][0], table01[a][b][1]-cRad*2, fill=filler, font="Consolas", text=title, anchor="w")

            canv.create_oval(table01[a][b][0], table01[a][b][1],table01[a][b][0]+cRad,table01[a][b][1]-cRad, fill=filler)
            if a > 0:
                for c in range(layers[a - 1]):
                    if len(layers) < 10:
                        canv.create_line(table01[a - 1][c][0] + (cRad), table01[a - 1][c][1] - int(cRad / 2),
                                         table01[a - 1][c][0] + (cRad)*3, table01[a - 1][c][1] - int(cRad / 2),
                                         table01[a][b][0]-(cRad)*2, table01[a][b][1]- int(cRad/2),
                                         table01[a][b][0], table01[a][b][1]- int(cRad/2),smooth=1)
                    else:
                        canv.create_line(table01[a - 1][c][0] + (cRad), table01[a - 1][c][1] - int(cRad / 2),
                                         table01[a][b][0], table01[a][b][1]- int(cRad/2))

                    #canv.create_line(150, 150, 100, 50, 50, 20, 20, 50, 60, 60, smooth=1)

    win.mainloop()

#t01 = DrawNetwork([8,6,9,5,7,3,4,6,7])
t01 = DrawNetwork([3,4,2,3])
