from tkinter import *
from tkinter import ttk, colorchooser


class PaintApp:
    # Stores current drawing tool used
    drawing_tool = "dot"

    # Tracks whether left mouse is down
    left_but = "down"

    # Tracks x & y when the mouse is clicked and released
    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None
    x1_box_pt, y1_box_pt, x2_box_pt, y2_box_pt = None, None, None, None

    display = None
    ox = None
    oy = None
    xleft = None
    xright = None
    ytop = None
    ybottom = None
    old_x = None
    old_y = None


    Menggambar = False
    penwidth = 5
    color_bg = 'white'
    color_fg = 'black'

    # ---------- CATCH MOUSE DOWN ----------

    def left_but_down(self, event=None):
        self.left_but = "down"

        # Set x & y when mouse is clicked
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y
        self.x1_box_pt = event.x
        self.y1_box_pt = event.y
        self.ox = event.x
        self.oy = event.y

    # ---------- CATCH MOUSE UP ----------

    def left_but_up(self, event=None):
        self.left_but = "up"

        # Set x & y when mouse is released
        self.x2_line_pt = event.x
        self.y2_line_pt = event.y
        self.x2_box_pt = event.x
        self.y2_box_pt = event.y

        # If mouse is released and line tool is selected
        # draw the line
        if self.drawing_tool == "line":
            self.line_draw(event)
        elif self.drawing_tool == "rectangle":
            self.rectangle_draw(event)
        elif self.drawing_tool == "dot":
            self.dot_draw(event)
        elif self.drawing_tool == "eraser":
            self.eraser(event)
        elif self.drawing_tool == "pointer":
            self.pointer(event)



    def pointer(self, event=None):
        self.refresh_rect()
        if None not in (self.x1_line_pt, self.y1_line_pt):
            self.drawing_area.delete("gambar2")
            
            self.ox = self.x1_line_pt
            self.oy = self.y1_line_pt

            xleft_asli = self.ox - 3
            xright_asli = self.ox + 3
            ytop_asli = self.oy - 3
            ybottom_asli = self.oy + 3
            
            self.xleft = self.ox -3
            self.xright = self.ox +3
            self.ytop = self.oy -3
            self.ybottom = self.oy +3

            ox_asli = self.ox
            oy_asli = self.oy

            for counter in range(len(self.x1_arr)):

                x1_asli = self.x1_arr[counter]
                x2_asli = self.x2_arr[counter]
                y1_asli = self.y1_arr[counter]
                y2_asli = self.y2_arr[counter]

                self.display = None

                self.nln(counter)

                print(self.display)
                if self.display:
                    if self.x1_arr[counter] == self.x2_arr[counter] and self.y1_arr[counter] == self.y2_arr[counter]:
                        self.drawing_area.create_rectangle(self.x1_arr[counter], self.y1_arr[counter], self.x1_arr[counter],
                                                       self.y1_arr[counter],
                                                       width=7,
                                                       tag="gambar2")
                    else:
                        self.drawing_area.create_line(int(x1_asli), int(y1_asli),
                                                  int(x2_asli), int(y2_asli),
                                                  fill="red",
                                                  tag="gambar2")
                        
                self.xleft = xleft_asli
                self.xright = xright_asli
                self.ytop = ytop_asli
                self.ybottom = ybottom_asli
                self.ox = ox_asli
                self.oy = oy_asli

                self.x1_arr[counter] = x1_asli
                self.x2_arr[counter] = x2_asli
                self.y1_arr[counter] = y1_asli
                self.y2_arr[counter] = y2_asli

            self.xleft = None
            self.xright = None
            self.ytop = None
            self.ybottom = None
            self.ox = None
            self.oy = None

            
        
    # ---------- ERASER ----------
    def eraser(self, event=None):
        self.refresh_rect()
        if None not in (self.x1_line_pt, self.y1_line_pt):
            flag = 0
            
            self.ox = self.x1_line_pt
            self.oy = self.y1_line_pt

            xleft_asli = self.ox - 3
            xright_asli = self.ox + 3
            ytop_asli = self.oy - 3
            ybottom_asli = self.oy + 3
            
            self.xleft = self.ox -3
            self.xright = self.ox +3
            self.ytop = self.oy -3
            self.ybottom = self.oy +3

            ox_asli = self.ox
            oy_asli = self.oy

            for counter in range(len(self.x1_arr)):

                x1_asli = self.x1_arr[counter]
                x2_asli = self.x2_arr[counter]
                y1_asli = self.y1_arr[counter]
                y2_asli = self.y2_arr[counter]

                self.display = None

                self.nln(counter)

                print(self.display)
                if self.display:
                    flag = 1
                    del self.x1_arr[counter]
                    del self.y1_arr[counter]
                    del self.x2_arr[counter]
                    del self.y2_arr[counter]
                    break
                        
                self.xleft = xleft_asli
                self.xright = xright_asli
                self.ytop = ytop_asli
                self.ybottom = ybottom_asli
                self.ox = ox_asli
                self.oy = oy_asli

                self.x1_arr[counter] = x1_asli
                self.x2_arr[counter] = x2_asli
                self.y1_arr[counter] = y1_asli
                self.y2_arr[counter] = y2_asli

            
            if flag == 1:   
               self.drawing_area.delete("rect")
               self.drawing_area.delete("gambar")
            
               for counter in range(len(self.x1_arr)):
                    if self.x1_arr[counter] == self.x2_arr[counter] and self.y1_arr[counter] == self.y2_arr[counter]:
                        self.drawing_area.create_rectangle(self.x1_arr[counter], self.y1_arr[counter], self.x1_arr[counter],
                                                       self.y1_arr[counter],
                                                       tag="gambar")
                    else:
                        self.drawing_area.create_line(int(self.x1_arr[counter]), int(self.y1_arr[counter]),
                                              int(self.x2_arr[counter]), int(self.y2_arr[counter]), fill="black",
                                              tag="gambar")
                        
                    self.drawing_area.tag_lower("gambar")

            
            self.xleft = None
            self.xright = None
            self.ytop = None
            self.ybottom = None
            self.ox = None
            self.oy = None


    # ---------- DRAW DOT ----------

    def dot_draw(self, event=None):
        self.refresh_rect()

        # Shortcut way to check if none of these values contain None
        if None not in (self.x1_line_pt, self.y1_line_pt):
            event.widget.create_rectangle(self.x1_line_pt, self.y1_line_pt, self.x1_line_pt, self.y1_line_pt,
                                          fill=self.color_fg,
                                          width=self.penwidth,
                                          tag="gambar")

            self.x1_arr.append(self.x1_line_pt)
            self.y1_arr.append(self.y1_line_pt)
            self.x2_arr.append(self.x1_line_pt)
            self.y2_arr.append(self.y1_line_pt)

    # ---------- DRAW LINE ----------

    def line_draw(self, event=None):
        self.refresh_rect()

        # Shortcut way to check if none of these values contain None
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            event.widget.create_line(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt,
                                     smooth=TRUE,
                                     fill = self.color_fg,
                                     width=self.penwidth,
                                     tag="gambar")

            # save coordinate to array
            self.x1_arr.append(self.x1_line_pt)
            self.y1_arr.append(self.y1_line_pt)
            self.x2_arr.append(self.x2_line_pt)
            self.y2_arr.append(self.y2_line_pt)

    # ---------- PAINT ----------
    def paint(self, event=None):
        self.refresh_rect()
        if self.old_x and self.old_y:
            event.widget.create_line(self.old_x, self.old_y, event.x, event.y, width=self.penwidth, fill=self.color_fg,
                                    capstyle=ROUND, smooth=True)

        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event= None):  # reseting or cleaning the canvas
        self.old_x = None
        self.old_y = None

        # ---------- DRAW RECTANGLE ----------

    def rectangle_draw(self, event=None):
        self.drawing_area.delete("rect")
        if None not in (self.x1_box_pt, self.y1_box_pt, self.x2_box_pt, self.y2_box_pt):
            event.widget.create_rectangle(self.x1_box_pt, self.y1_box_pt, self.x2_box_pt, self.y2_box_pt,
                                          dash=(5, 5),
                                          width=self.penwidth,
                                          tag="rect")
        
    def pointer_button(self, event=None):
        self.drawing_area.delete("gambar2")
        self.drawing_tool = "pointer"

    def dot_button(self, event=None):
        self.drawing_area.delete("gambar2")
        self.drawing_tool = "dot"

    def line_button(self, event=None):
        self.drawing_area.delete("gambar2")
        self.drawing_tool = "line"

    def rect_button(self, event=None):
        self.drawing_area.delete("gambar2")
        self.drawing_tool = "rectangle"

    def eraser_button(self, event=None):
        self.drawing_area.delete("gambar2")
        self.drawing_tool = "eraser"

    def clear_canvas(self, event=None):
        self.drawing_area.delete("gambar2")
        self.drawing_area.delete("gambar")

        # To delete all coordinate in array where clear all gambar
        del self.x1_arr[:]
        del self.x2_arr[:]
        del self.y1_arr[:]
        del self.y2_arr[:]
        del self.x1_crop[:]
        del self.x2_crop[:]
        del self.y1_crop[:]
        del self.y2_crop[:]

    def refresh_rect(self, event=None):
        self.drawing_area.delete("gambar2")
        self.drawing_area.delete("rect")

        self.x1_box_pt = None
        self.y1_box_pt = None
        self.x2_box_pt = None
        self.y2_box_pt = None

    def save_file(self, event=None):
        self.drawing_area.delete("gambar2")
        
        newwin = Toplevel(root)
        e = Entry(newwin)
        e.pack()

        e.focus_set()

        def saveIT():
            with open(e.get(), "w") as file:
                file.write("x1 \n")
                for counter in range(len(self.x1_arr)):
                    file.write(str(self.x1_arr[counter]))
                    file.write(" ")
                file.write("\ny1 \n")
                for counter in range(len(self.y1_arr)):
                    file.write(str(self.y1_arr[counter]))
                    file.write(" ")

                file.write("\nx2 \n")
                for counter in range(len(self.x2_arr)):
                    file.write(str(self.x2_arr[counter]))
                    file.write(" ")
                file.write("\ny2 \n")
                for counter in range(len(self.y2_arr)):
                    file.write(str(self.y2_arr[counter]))
                    file.write(" ")

                if self.x1_crop:
                    file.write("\nx1_crop \n")
                    for counter in range(len(self.x1_crop)):
                        file.write(str(self.x1_crop[counter]))
                        file.write(" ")
                    file.write("\ny1_crop \n")
                    for counter in range(len(self.y1_crop)):
                        file.write(str(self.y1_crop[counter]))
                        file.write(" ")
                    file.write("\nx2_crop \n")
                    for counter in range(len(self.x2_crop)):
                        file.write(str(self.x2_crop[counter]))
                        file.write(" ")
                    file.write("\ny2_crop \n")
                    for counter in range(len(self.y2_crop)):
                        file.write(str(self.y2_crop[counter]))
                        file.write(" ")

                print("save successfull")

        button1 = Button(newwin, text="save", command=saveIT)  # command linked
        button1.pack()

    def load_file(self, event=None):
        self.drawing_area.delete("gambar2")
        
        newwin = Toplevel(root)
        e = Entry(newwin)
        e.pack()

        e.focus_set()

        def loadIT():
            ind = None
            self.drawing_area.delete("rect")
            self.drawing_area.delete("gambar")
            del self.x1_arr[:]
            del self.x2_arr[:]
            del self.y1_arr[:]
            del self.y2_arr[:]
            del self.x1_crop[:]
            del self.x2_crop[:]
            del self.y1_crop[:]
            del self.y2_crop[:]

            with open(e.get()) as file:
                data = file.readlines()
                for line in data:
                    temp = line.split()
                    if temp[0] == 'x1':
                        ind = "x1"
                        continue
                    elif temp[0] == 'y1':
                        ind = "y1"
                        continue
                    elif temp[0] == 'x2':
                        ind = "x2"
                        continue
                    elif temp[0] == 'y2':
                        ind = "y2"
                        continue
                    elif temp[0] == 'x1_crop':
                        ind = "x1_crop"
                        continue
                    elif temp[0] == 'y1_crop':
                        ind = "y1_crop"
                        continue
                    elif temp[0] == 'x2_crop':
                        ind = "x2_crop"
                        continue
                    elif temp[0] == 'y2_crop':
                        ind = "y2_crop"
                        continue

                    if ind == "x1":
                        self.x1_arr = list(map(int, temp))
                        continue
                    elif ind == "y1":
                        self.y1_arr = list(map(int, temp))
                        continue
                    elif ind == "x2":
                        self.x2_arr = list(map(int, temp))
                        continue
                    elif ind == "y2":
                        self.y2_arr = list(map(int, temp))
                        continue
                    elif ind == "x1_crop":
                        self.x1_crop = list(map(float, temp))
                        continue
                    elif ind == "y1_crop":
                        self.y1_crop = list(map(float, temp))
                        continue
                    elif ind == "x2_crop":
                        self.x2_crop = list(map(float, temp))
                        continue
                    elif ind == "y2_crop":
                        self.y2_crop = list(map(float, temp))
                        continue

            print(self.x1_arr)
            print(self.y1_arr)
            print(self.x2_arr)
            print(self.y2_arr)
            
            for counter in range(len(self.x1_arr)):
                if self.x1_arr[counter] == self.x2_arr[counter] and self.y1_arr[counter] == self.y2_arr[counter]:
                    self.drawing_area.create_rectangle(self.x1_arr[counter], self.y1_arr[counter], self.x1_arr[counter],
                                                       self.y1_arr[counter],
                                                       tag="gambar")
                else:
                    self.drawing_area.create_line(int(self.x1_arr[counter]), int(self.y1_arr[counter]),
                                              int(self.x2_arr[counter]), int(self.y2_arr[counter]), fill="black",
                                              tag="gambar")
                self.drawing_area.tag_lower("gambar")
                
            for counter in range(len(self.x1_crop)):
                if self.x1_crop[counter] == self.x2_crop[counter] and self.y1_crop[counter] == self.y2_crop[counter]:
                    self.drawing_area.create_rectangle(self.x1_crop[counter], self.y1_crop[counter], self.x1_crop[counter],
                                                       self.y1_crop[counter],
                                                       width=7,
                                                       tag="gambar")
                else:
                    self.drawing_area.create_line(int(self.x1_crop[counter]), int(self.y1_crop[counter]),
                                              int(self.x2_crop[counter]), int(self.y2_crop[counter]), fill="red",
                                              tag="gambar")
                self.drawing_area.tag_lower("gambar")

        button1 = Button(newwin, text="load", command=loadIT)  # command linked
        button1.pack()

    def nln(self, counter):

        def rotate90c(ox, oy, px, py):

            qx = ox + -1 * (px - ox)
            sementara = py
            qy = qx
            qx = sementara

            return qx, qy

        def rotate270c(ox, oy, px, py):
            sementara = px
            qy = oy + -1 * (py - oy)
            qx = qy
            qy = sementara

            return qx, qy

        def rotate180c(ox, oy, px, py):
            qx = ox + -1 * (px - ox)
            qy = oy + -1 * (py - oy)

            return qx, qy

        def reflectxaxis(ox, oy, px, py):
            qx = px
            qy = oy + -1 * (py - oy)
            return qx, qy

        def reflectxminusy(ox, oy, px, py):
            qx = ox + -1 * (px - ox)
            qy = oy + -1 * (py - oy)
            sementara_q = qx
            qx = qy
            qy = sementara_q

            return qx, qy

        def leftcolumn(xleft, ytop, xright, ybottom, x1, y1, x2, y2):
            if x2 < xleft:
                self.display = False
                print("I'm in leftcolumn, FALSE, CAUSE x2<xleft")

            elif y1 < ytop:

                print("I'm in leftcolumn, y1<ytop, i'm going to topleftcorner")
                topleftcorner(xleft, ytop, xright, ybottom, x1, y1, x2, y2)


            elif y1 > ybottom:
                print("I'm in leftcolumn, Y1>YBOTTOM")

                first_value = reflectxaxis(self.ox, self.oy, x1, y1)
                x1 = first_value[0]
                y1 = first_value[1]
                second_value = reflectxaxis(self.ox, self.oy, x2, y2)
                x2 = second_value[0]
                y2 = second_value[1]

                print("I'm in left column, After reflectxaxis new value of x1,y1,x2,y2")
                print(x1, y1, x2, y2)

                first_value = reflectxaxis(self.ox, self.oy, xleft, ytop)
                self.xleft = first_value[0]
                self.ybottom = first_value[1]
                second_value = reflectxaxis(self.ox, self.oy, xright, ybottom)
                self.xright = second_value[0]
                self.ytop = second_value[1]

                # sudah benar

                print("I'm in left column, After reflectxaxis new value of xleft,ytop,xright,ybottom")
                print(xleft, ytop, xright, ybottom)

                self.ox = (self.xleft + self.xright) / 2
                self.oy = (self.ytop + self.ybottom) / 2

                print("I'm in left column, New Value ox, oy")
                print(self.ox, self.oy)

                print("I'm in left column, I'm going to topleftcorner")

                topleftcorner(self.xleft, self.ytop, self.xright, self.ybottom, x1, y1, x2, y2)

                first_value = reflectxaxis(self.ox, self.oy, self.x1_arr[counter], self.y1_arr[counter])
                self.x1_arr[counter] = first_value[0]
                self.y1_arr[counter] = first_value[1]
                second_value = reflectxaxis(self.ox, self.oy, self.x2_arr[counter], self.y2_arr[counter])
                self.x2_arr[counter] = second_value[0]
                self.y2_arr[counter] = second_value[1]

                print("I'm in left column, After reflectxaxis new value of x1,y1,x2,y2")
                print(self.x1_arr[counter], self.y1_arr[counter], self.x2_arr[counter], self.y2_arr[counter])

                first_value = reflectxaxis(self.ox, self.oy, self.xleft, self.ytop)
                self.xleft = first_value[0]
                self.ybottom = first_value[1]
                second_value = reflectxaxis(self.ox, self.oy, self.xright, self.ybottom)
                self.xright = second_value[0]
                self.ytop = second_value[1]

                print("I'm in left column, After reflectxaxis new value of xleft,ytop,xright,ybottom")
                print(self.xleft, self.ytop, self.xright, self.ybottom)

                self.ox = (self.xleft + self.xright) / 2
                self.oy = (self.ytop + self.ybottom) / 2

                print("I'm in left column, New Value ox, oy")
                print(self.ox, self.oy)

            else:
                print("I'm in leftcolumn, x2 >= xleft, y1 >= ytop, y1 <= bottom, I'm going to leftedge")
                leftedge(xleft, ytop, xright, ybottom, x1, y1, x2, y2)

        def topleftcorner(xleft, ytop, xright, ybottom, x1, y1, x2, y2):
            if y2 >= ytop and y2 <= ybottom and x2 >= xleft and x2 <= xright:
                sementara_x = x1
                sementara_y = y1
                x1 = x2
                y1 = y2
                x2 = sementara_x
                y2 = sementara_y
                inside(xleft, ytop, xright, ybottom, x1, y1, x2, y2)
            elif y2 < ytop:
                self.display = False
                print("I'm in topleftcorner, FALSE CAUSE, y2<ytop")
            else:
                print("I'm in topleftcorner, Y2 >= YTOP")
                relx2 = x2 - x1
                print("I'm in topleftcorner, relx2: " + str(relx2))
                rely2 = y2 - y1
                print("I'm in topleftcorner, rely2: " + str(rely2))
                topproduct = (ytop - y1) * relx2
                print("I'm in topleftcorner, topproduct: " + str(topproduct))
                leftproduct = (xleft - x1) * rely2
                print("I'm in topleftcorner, leftproduct: " + str(leftproduct))
                if (topproduct - leftproduct) < 0:
                    print("I'm in topleftcorner, x2,y2 below line x1,y1 and xleft, ytop")
                    leftbottomregion(xleft, ytop, xright, ybottom, x1, y1, x2, y2, relx2, rely2, leftproduct)
                else:
                    print("I'm in topleftcorner, x2,y2 above line x1,y1 and xleft, ytop")
                    first_value = reflectxminusy(self.ox, self.oy, x1, y1)
                    x1 = first_value[0]
                    y1 = first_value[1]
                    second_value = reflectxminusy(self.ox, self.oy, x2, y2)
                    x2 = second_value[0]
                    y2 = second_value[1]

                    print("I'm in topleftcorner, After reflectxminusy new value of x1,y1,x2,y2")
                    print(x1, y1, x2, y2)

                    first_value = reflectxminusy(self.ox, self.oy, xleft, ytop)
                    self.xleft = first_value[0]
                    self.ytop = first_value[1]
                    second_value = reflectxminusy(self.ox, self.oy, xright, ybottom)
                    self.xright = second_value[0]
                    self.ybottom = second_value[1]

                    # sudah benar

                    print("I'm in topleftcorner, After reflectxminusy new value of xleft,ytop,xright,ybottom")
                    print(self.xleft, self.ytop, self.xright, self.ybottom)

                    self.ox = (self.xleft + self.xright) / 2
                    self.oy = (self.ytop + self.ybottom) / 2

                    print("I'm in topleftcorner, New Value ox, oy")
                    print(self.ox, self.oy)

                    print("I'm in topleftcorner, I'm going to leftbottomregion")

                    leftbottomregion(self.xleft, self.ytop, self.xright, self.ybottom, x1, y1, x2, y2, -rely2,
                                     -relx2, topproduct)

                    first_value = reflectxminusy(self.ox, self.oy, self.x1_arr[counter], self.y1_arr[counter])
                    self.x1_arr[counter] = first_value[0]
                    self.y1_arr[counter] = first_value[1]
                    second_value = reflectxminusy(self.ox, self.oy, self.x2_arr[counter], self.y2_arr[counter])
                    self.x2_arr[counter] = second_value[0]
                    self.y2_arr[counter] = second_value[1]

                    print("I'm in topleftcorner, After reflectxminusy new value of x1,y1,x2,y2")
                    print(self.x1_arr[counter], self.y1_arr[counter], self.x2_arr[counter], self.y2_arr[counter])

                    first_value = reflectxminusy(self.ox, self.oy, self.xleft, self.ytop)
                    self.xleft = first_value[0]
                    self.ytop = first_value[1]
                    second_value = reflectxminusy(self.ox, self.oy, self.xright, self.ybottom)
                    self.xright = second_value[0]
                    self.ybottom = second_value[1]

                    # sudah benar

                    print("I'm in topleftcorner, After reflectxminusy new value of xleft,ytop,xright,ybottom")
                    print(xleft, ytop, xright, ybottom)

                    self.ox = (self.xleft + self.xright) / 2
                    self.oy = (self.ytop + self.ybottom) / 2

                    print("I'm in topleftcorner, New Value ox, oy")
                    print(self.ox, self.oy)

        def leftbottomregion(xleft, ytop, xright, ybottom, x1, y1, x2, y2, relx2, rely2, leftproduct):

            if y2 <= ybottom and x2 > xright:
                bottomproduct = (ybottom - y1) * relx2
                print("I'm in leftbottomregion, x2>xright")
                rightproduct = (xright - x1) * rely2
                print("I'm in leftbottomregion, rightproduct: " + str(rightproduct))
                if (bottomproduct - rightproduct) < 0:
                    print("I'm in leftbottomregion, x2,y2 below line x1,y1 and xright, ybottom")
                    self.x2_arr[counter] = x1 + bottomproduct / rely2
                    self.y2_arr[counter] = ybottom
                else:
                    print("I'm in leftbottomregion, x2,y2 above line x1,y1 and xright, ybottom")
                    self.y2_arr[counter] = y1 + rightproduct / relx2
                    self.x2_arr[counter] = xright

                self.y1_arr[counter] = y1 + leftproduct / relx2
                self.x1_arr[counter] = xleft
                self.display = True

            else:
                print("I'm in leftbottomregion, y2>ybottom")
                bottomproduct = (ybottom - y1) * relx2
                print("I'm in leftbottomregion, bottomproduct: " + str(bottomproduct))
                print("I'm in leftbottomregion, leftproduct: " + str(leftproduct))
                if (bottomproduct - leftproduct) < 0:
                    print("I'm in leftbottomregion, FALSE CAUSE, x2,y2 below line x1, y1 and xleft, ybottom")
                    self.display = False

                else:
                    if self.x2_arr[counter] > self.xright:

                        print("I'm in leftbottomregion, x2>xright")
                        rightproduct = (xright - x1) * rely2
                        print("I'm in leftbottomregion, rightproduct: " + str(rightproduct))
                        if (bottomproduct - rightproduct) < 0:
                            print("I'm in leftbottomregion, x2,y2 below line x1,y1 and xright, ybottom")
                            self.x2_arr[counter] = x1 + bottomproduct / rely2
                            self.y2_arr[counter] = ybottom
                        else:
                            print("I'm in leftbottomregion, x2,y2 above line x1,y1 and xright, ybottom")
                            self.y2_arr[counter] = y1 + rightproduct / relx2
                            self.x2_arr[counter] = xright
                    else:
                        print("I'm in leftbottomregion, x2 <= xright")
                        self.x2_arr[counter] = x1 + bottomproduct / rely2
                        self.y2_arr[counter] = ybottom
                    self.y1_arr[counter] = y1 + leftproduct / relx2
                    self.x1_arr[counter] = xleft
                    self.display = True

        def leftedge(xleft, ytop, xright, ybottom, x1, y1, x2, y2):
            if x2 < xleft:
                print("I'm in leftedge, FALSE because x2 < xleft")
                self.display = False

            elif y2 > ybottom:
                print("I'm in leftedge, y2>ybottom. Go TO P2BOTTOM")
                p2bottom(xleft, ytop, xright, ybottom, x1, y1, x2, y2)
            elif y2 < ytop:
                print("I'm in leftedge, y2<ytop")
                first_value = reflectxaxis(self.ox, self.oy, x1, y1)
                x1 = first_value[0]
                y1 = first_value[1]
                second_value = reflectxaxis(self.ox, self.oy, x2, y2)
                x2 = second_value[0]
                y2 = second_value[1]

                print("I'm in leftedge, After reflectxaxis new value of x1,y1,x2,y2")
                print(x1, y1, x2, y2)

                first_value = reflectxaxis(self.ox, self.oy, xleft, ytop)
                self.xleft = first_value[0]
                self.ybottom = first_value[1]
                second_value = reflectxaxis(self.ox, self.oy, xright, ybottom)
                self.xright = second_value[0]
                self.ytop = second_value[1]

                # sudah benar

                print("I'm in leftedge, After reflectxaxis new value of xleft,ytop,xright,ybottom")
                print(self.xleft, self.ytop, self.xright, self.ybottom)

                self.ox = (self.xleft + self.xright) / 2
                self.oy = (self.ytop + self.ybottom) / 2

                print("I'm in leftedge, New Value ox, oy")
                print(self.ox, self.oy)

                print("I'm in leftedge, I'm going to p2bottom")

                p2bottom(self.xleft, self.ytop, self.xright, self.ybottom, x1, y1, x2, y2)

                first_value = reflectxaxis(self.ox, self.oy, self.x1_arr[counter], self.y1_arr[counter])
                self.x1_arr[counter] = first_value[0]
                self.y1_arr[counter] = first_value[1]
                second_value = reflectxaxis(self.ox, self.oy, self.x2_arr[counter], self.y2_arr[counter])
                self.x2_arr[counter] = second_value[0]
                self.y2_arr[counter] = second_value[1]

                print("I'm in leftedge, After reflectxaxis new value of x1,y1,x2,y2")
                print(self.x1_arr[counter], self.y1_arr[counter], self.x2_arr[counter], self.y2_arr[counter])

                first_value = reflectxaxis(self.ox, self.oy, self.xleft, self.ytop)
                self.xleft = first_value[0]
                self.ybottom = first_value[1]
                second_value = reflectxaxis(self.ox, self.oy, self.xright, self.ybottom)
                self.xright = second_value[0]
                self.ytop = second_value[1]

                print("I'm in leftedge, After reflectxminusy new value of xleft,ytop,xright,ybottom")
                print(self.xleft, self.ytop, self.xright, self.ybottom)

                self.ox = (self.xleft + self.xright) / 2
                self.oy = (self.ytop + self.ybottom) / 2

                print("I'm in leftedge, New Value ox, oy")
                print(self.ox, self.oy)

            else:
                print("I'm in leftedge, x2>= xleft, y2 <= ybottom, y2 >= ytop")
                relx2 = x2 - x1
                print("I'm in leftedge, relx2: " + str(relx2))
                rely2 = y2 - y1
                print("I'm in leftedge, rely2: " + str(rely2))
                if x2 > xright:
                    print("I'm in leftedge, x2 > xright")
                    self.y2_arr[counter] = y1 + rely2 * (xright - x1) / relx2
                    self.x2_arr[counter] = xright
                self.y1_arr[counter] = y1 + rely2 * (xleft - x1) / relx2
                self.x1_arr[counter] = xleft
                self.display = True

        def p2bottom(xleft, ytop, xright, ybottom, x1, y1, x2, y2):
            print("I'm in p2bottom.")
            relx2 = x2 - x1
            print("I'm in p2bottom. relx2: " + str(relx2))
            rely2 = y2 - y1
            print("I'm in p2bottom. rely2: " + str(rely2))
            leftproduct = (xleft - x1) * rely2
            print("I'm in p2bottom. leftproduct: " + str(leftproduct))
            bottomproduct = (ybottom - y1) * relx2
            print("I'm in p2bottom. bottomproduct: " + str(bottomproduct))
            if (bottomproduct - leftproduct) < 0:
                print("I'm in p2bottom. FALSE CAUSE  x2,y2 below line x1, y1 and xleft, ybottom")
                self.display = False
            else:
                print("I'm in p2bottom.  x2,y2 above line x1, y1 and xleft, ybottom")
                if self.x2_arr[counter] <= self.xright:
                    print("I'm in p2bottom. x2<=xright")
                    self.x2_arr[counter] = x1 + bottomproduct / rely2
                    self.y2_arr[counter] = ybottom
                else:
                    print("I'm in p2bottom. x2 > xright")
                    rightproduct = (xright - x1) * rely2
                    print("I'm in p2bottom. rightproduct: " + str(rightproduct))
                    if (bottomproduct - rightproduct) < 0:
                        print("I'm in p2bottom.  x2,y2 below line x1, y1 and xright, ybottom")
                        self.x2_arr[counter] = x1 + bottomproduct / rely2
                        self.y2_arr[counter] = ybottom
                    else:
                        print("I'm in p2bottom.  x2,y2 above line x1, y1 and xleft, ybottom")
                        self.y2_arr[counter] = y1 + rightproduct / relx2
                        self.x2_arr[counter] = xright
                self.y1_arr[counter] = y1 + leftproduct / relx2
                self.x1_arr[counter] = xleft
                self.display = True

        def inside(xleft, ytop, xright, ybottom, x1, y1, x2, y2):
            print("I'm in inside.")

            def p2left(xleft, ytop, xright, ybottom, x1, y1, x2, y2):
                print("I'm in inside,p2left.")

                def p2lefttop(xleft, ytop, xright, ybottom, x1, y1, x2, y2):
                    self.x1_arr[counter] = x1
                    self.y1_arr[counter] = y1
                    print("I'm in inside,p2left,p2lefttop.")

                    relx2 = x2 - x1
                    print("I'm in inside,p2left,p2lefttop. relx2: " + str(relx2))
                    rely2 = y2 - y1
                    print("I'm in inside,p2left,p2lefttop. rely2: " + str(rely2))
                    leftproduct = rely2 * (xleft - x1)
                    print("I'm in inside,p2left,p2lefttop. leftproduct: " + str(leftproduct))
                    topproduct = relx2 * (ytop - y1)
                    print("I'm in inside,p2left,p2lefttop. topproduct: " + str(topproduct))
                    if (topproduct - leftproduct) < 0:
                        print("I'm in inside,p2left,p2lefttop. x2,y2 below line x1, y1 and xleft, ybottom")
                        self.x2_arr[counter] = x1 + topproduct / rely2
                        self.y2_arr[counter] = ytop
                    else:
                        print("I'm in inside,p2left,p2lefttop. x2,y2 above line x1, y1 and xleft, ybottom")
                        self.y2_arr[counter] = y1 + leftproduct / relx2
                        self.x2_arr[counter] = xleft

                if y2 < ytop:
                    print("I'm in inside,p2left. y2 < ytop. I'm going to p2lefttop")
                    p2lefttop(xleft, ytop, xright, ybottom, x1, y1, x2, y2)
                elif y2 > ybottom:
                    print("I'm in inside,p2left. y2 > ybottom")

                    first_value = rotate90c(self.ox, self.oy, self.x1_arr[counter], self.y1_arr[counter])
                    self.x1_arr[counter] = first_value[0]
                    self.y1_arr[counter] = first_value[1]
                    second_value = rotate90c(self.ox, self.oy, self.x2_arr[counter], self.y2_arr[counter])
                    self.x2_arr[counter] = second_value[0]
                    self.y2_arr[counter] = second_value[1]

                    print("I'm in inside,p2left. After rotate90c value of x1,y1,x2,y2:")
                    print(self.x1_arr[counter], self.y1_arr[counter], self.x2_arr[counter], self.y2_arr[counter])

                    first_value = reflectxminusy(self.ox, self.oy, xleft, ytop)
                    second_value = reflectxminusy(self.ox, self.oy, xright, ytop)
                    self.xleft = self.ybottom
                    self.xright = self.ytop
                    self.ytop = first_value[1]
                    self.ybottom = second_value[1]

                    print("I'm in inside,p2left. After reflectxminusy value of xleft,ytop,xright,ybottom:")
                    print(self.xleft, self.ytop, self.xright, self.ybottom)

                    self.ox = (self.xleft + self.xright) / 2
                    self.oy = (self.ytop + self.ybottom) / 2

                    print("I'm in inside,p2left. new value of origin:")
                    print(self.ox, self.oy)

                    print("I'm in inside,p2left. I'm going to p2lefttop")

                    p2lefttop(self.xleft, self.ytop, self.xright, self.ybottom, self.x1_arr[counter],
                              self.y1_arr[counter], self.x2_arr[counter], self.y2_arr[counter])

                    first_value = rotate270c(self.ox, self.oy, self.x1_arr[counter], self.y1_arr[counter])
                    self.x1_arr[counter] = first_value[0]
                    self.y1_arr[counter] = first_value[1]
                    second_value = rotate270c(self.ox, self.oy, self.x2_arr[counter], self.y2_arr[counter])
                    self.x2_arr[counter] = second_value[0]
                    self.y2_arr[counter] = second_value[1]
                    print("I'm in inside,p2left. After rotate 270c value of x1,y1,x2,y2:")
                    print(self.x1_arr[counter], self.y1_arr[counter], self.x2_arr[counter], self.y2_arr[counter])

                    first_value = reflectxminusy(self.ox, self.oy, self.xleft, self.ytop)
                    second_value = reflectxminusy(self.ox, self.oy, self.xleft, self.ybottom)
                    self.ybottom = self.xleft
                    self.ytop = self.xright
                    self.xleft = first_value[0]
                    self.xright = second_value[0]

                    print("I'm in inside,p2left. After reflectxminusy value of xleft,ytop,xright,ybottom:")
                    print(self.xleft, self.ytop, self.xright, self.ybottom)

                    self.ox = (self.xleft + self.xright) / 2
                    self.oy = (self.ytop + self.ybottom) / 2

                    print("I'm in inside,p2left. new value of origin:")
                    print(self.ox, self.oy)

                else:
                    print("I'm in inside, p2left.y2 >= top, y2 <= ybottom")
                    self.y2_arr[counter] = y1 + (y2 - y1) * (xleft - x1) / (x2 - x1)
                    self.x2_arr[counter] = xleft
                    self.x1_arr[counter] = x1
                    self.y1_arr[counter] = y1

            self.display = True
            if x2 < xleft:
                print("I'm in inside. x2 < xleft. I'm going to p2 left")
                p2left(xleft, ytop, xright, ybottom, x1, y1, x2, y2)
            elif x2 > xright:
                print("I'm in inside. x2 > right")
                first_value = rotate180c(self.ox, self.oy, self.x1_arr[counter], self.y1_arr[counter])
                self.x1_arr[counter] = first_value[0]
                self.y1_arr[counter] = first_value[1]
                second_value = rotate180c(self.ox, self.oy, x2, y2)
                self.x2_arr[counter] = second_value[0]
                self.y2_arr[counter] = second_value[1]
                print("I'm in inside. After rotate 180 value of x1,y1,x2,y2:")
                print(self.x1_arr[counter], self.y1_arr[counter], self.x2_arr[counter], self.y2_arr[counter])

                first_value = reflectxminusy(self.ox, self.oy, xleft, ytop)
                second_value = reflectxminusy(self.ox, self.oy, xright, ybottom)
                self.xleft = second_value[1]
                self.xright = first_value[1]
                self.ytop = second_value[0]
                self.ybottom = first_value[0]
                print("I'm in inside. After reflectxminusy value of xleft,ytop,xright,ybottom:")
                print(self.xleft, self.ytop, self.xright, self.ybottom)

                self.ox = (self.xleft + self.xright) / 2
                self.oy = (self.ytop + self.ybottom) / 2

                print("I'm in inside. new value of origin:")
                print(self.ox, self.oy)

                print("I'm in inside. I'm going to p2left")

                p2left(self.xleft, self.ytop, self.xright, self.ybottom, self.x1_arr[counter], self.y1_arr[counter],
                       self.x2_arr[counter], self.y2_arr[counter])

                first_value = rotate180c(self.ox, self.oy, self.x1_arr[counter], self.y1_arr[counter])
                self.x1_arr[counter] = first_value[0]
                self.y1_arr[counter] = first_value[1]
                second_value = rotate180c(self.ox, self.oy, self.x2_arr[counter], self.y2_arr[counter])
                self.x2_arr[counter] = second_value[0]
                self.y2_arr[counter] = second_value[1]
                print("I'm in inside. After rotate 180 value of x1,y1,x2,y2:")
                print(self.x1_arr[counter], self.y1_arr[counter], self.x2_arr[counter], self.y2_arr[counter])

                first_value = reflectxminusy(self.ox, self.oy, self.xleft, self.ytop)
                second_value = reflectxminusy(self.ox, self.oy, self.xright, self.ybottom)
                self.xleft = second_value[1]
                self.xright = first_value[1]
                self.ytop = second_value[0]
                self.ybottom = first_value[0]

                print("I'm in inside. After reflectxminusy value of xleft,ytop,xright,ybottom:")
                print(self.xleft, self.ytop, self.xright, self.ybottom)

                self.ox = (self.xleft + self.xright) / 2
                self.oy = (self.ytop + self.ybottom) / 2

                print("I'm in inside. new value of origin:")
                print(self.ox, self.oy)

            elif y2 < ytop:
                print("I'm in inside. y2<ytop")
                self.x2_arr[counter] = x1 + (x2 - x1) * (ytop - y1) / (y2 - y1)
                self.y2_arr[counter] = ytop
            elif y2 > ybottom:
                print("I'm in inside. y2>ybottom")
                self.x2_arr[counter] = x1 + (x2 - x1) * (ybottom - y1) / (y2 - y1)
                self.y2_arr[counter] = ybottom
            else:
                print("I'm in inside. x2 > left, x2 < left , y2 > top, y2 < ybottom")
                self.x1
                self.display = True

        def centrecolumn(xleft, ytop, xright, ybottom, x1, y1, x2, y2):
            if y2 >= ytop and y2 <= ybottom and x2 >= xleft and x2 <= xright:
                sementara_x = x1
                sementara_y = y1
                hasil_x = x2
                hasil_y = y2
                x1 = x2
                y1 = y2
                x2 = sementara_x
                y2 = sementara_y
                inside(xleft, ytop, xright, ybottom, x1, y1, x2, y2)
                self.x1_arr[counter] = hasil_x
                self.y1_arr[counter] = hasil_y


            elif y1 < ytop:

                print("I'm in centrecolumn. y1 < ytop")

                first_value = rotate90c(self.ox, self.oy, self.x1_arr[counter], self.y1_arr[counter])

                self.x1_arr[counter] = first_value[0]

                self.y1_arr[counter] = first_value[1]

                second_value = rotate90c(self.ox, self.oy, self.x2_arr[counter], self.y2_arr[counter])

                self.x2_arr[counter] = second_value[0]

                self.y2_arr[counter] = second_value[1]

                print("I'm in centrecolumn. After rotate 90c value of x1,y1,x2,y2:")

                print(self.x1_arr[counter], self.y1_arr[counter], self.x2_arr[counter], self.y2_arr[counter])

                first_value = reflectxminusy(self.ox, self.oy, xleft, ytop)

                second_value = reflectxminusy(self.ox, self.oy, xright, ybottom)

                self.xleft = self.ytop

                self.xright = self.ybottom

                self.ytop = second_value[1]

                self.ybottom = first_value[1]

                print("I'm in centrecolumn. After reflectxminusy value of xleft,ytop,xright,ybottom:")

                print(self.xleft, self.ytop, self.xright, self.ybottom)

                self.ox = (self.xleft + self.xright) / 2

                self.oy = (self.ytop + self.ybottom) / 2

                print("I'm in centrecolumn. new value of origin:")

                print(self.ox, self.oy)

                print("I'm in centrecolumn. I'm going to leftedge")

                leftedge(self.xleft, self.ytop, self.xright, self.ybottom, self.x1_arr[counter],
                         self.y1_arr[counter], self.x2_arr[counter], self.y2_arr[counter])

                first_value = rotate270c(self.ox, self.oy, self.x1_arr[counter], self.y1_arr[counter])

                self.x1_arr[counter] = first_value[0]

                self.y1_arr[counter] = first_value[1]

                second_value = rotate270c(self.ox, self.oy, self.x2_arr[counter], self.y2_arr[counter])

                self.x2_arr[counter] = second_value[0]

                self.y2_arr[counter] = second_value[1]

                print("I'm in centrecolumn. After rotate 270c value of x1,y1,x2,y2:")

                print(self.x1_arr[counter], self.y1_arr[counter], self.x2_arr[counter], self.y2_arr[counter])

                first_value = reflectxminusy(self.ox, self.oy, self.xleft, self.ytop)

                second_value = reflectxminusy(self.ox, self.oy, self.xright, self.ybottom)

                self.ybottom = self.xright

                self.ytop = self.xleft

                self.xleft = second_value[0]

                self.xright = first_value[0]

                print("I'm in centrecolumn. After reflectxminusy value of xleft,ytop,xright,ybottom:")

                print(self.xleft, self.ytop, self.xright, self.ybottom)

                print("I'm in centrecolumn. new value of origin:")

                print(self.ox, self.oy)

                print("I'm in centrecolumn. I'm going to leftedge")


            elif y1 > ybottom:

                first_value = rotate270c(self.ox, self.oy, self.x1_arr[counter], self.y1_arr[counter])

                self.x1_arr[counter] = first_value[0]

                self.y1_arr[counter] = first_value[1]

                second_value = rotate270c(self.ox, self.oy, self.x2_arr[counter], self.y2_arr[counter])

                self.x2_arr[counter] = second_value[0]

                self.y2_arr[counter] = second_value[1]

                print("I'm in centrecolumn. After rotate270c value of x1,y1,x2,y2:")

                print(self.x1_arr[counter], self.y1_arr[counter], self.x2_arr[counter], self.y2_arr[counter])

                first_value = reflectxminusy(self.ox, self.oy, xleft, ytop)

                second_value = reflectxminusy(self.ox, self.oy, xright, ybottom)

                self.xleft = self.ytop

                self.xright = self.ybottom

                self.ytop = second_value[1]

                self.ybottom = first_value[1]

                print("I'm in centrecolumn. After reflectxminusy value of xleft,ytop,xright,ybottom:")

                print(self.xleft, self.ytop, self.xright, self.ybottom)

                self.ox = (self.xleft + self.xright) / 2

                self.oy = (self.ytop + self.ybottom) / 2

                print("I'm in centrecolumn. new value of origin:")

                print(self.ox, self.oy)

                print("I'm in centrecolumn. I'm going to leftedge")

                leftedge(self.xleft, self.ytop, self.xright, self.ybottom, self.x1_arr[counter],
                         self.y1_arr[counter], self.x2_arr[counter], self.y2_arr[counter])

                first_value = rotate90c(self.ox, self.oy, self.x1_arr[counter], self.y1_arr[counter])

                self.x1_arr[counter] = first_value[0]

                self.y1_arr[counter] = first_value[1]

                second_value = rotate90c(self.ox, self.oy, self.x2_arr[counter], self.y2_arr[counter])

                self.x2_arr[counter] = second_value[0]

                self.y2_arr[counter] = second_value[1]

                print("I'm in centrecolumn. After rotate 90c value of x1,y1,x2,y2:")

                print(self.x1_arr[counter], self.y1_arr[counter], self.x2_arr[counter], self.y2_arr[counter])

                first_value = reflectxminusy(self.ox, self.oy, self.xleft, self.ytop)

                second_value = reflectxminusy(self.ox, self.oy, self.xright, self.ybottom)

                self.ybottom = self.xright

                self.ytop = self.xleft

                self.xleft = second_value[0]

                self.xright = first_value[0]

                print("I'm in centrecolumn. After reflectxminusy value of xleft,ytop,xright,ybottom:")

                print(self.xleft, self.ytop, self.xright, self.ybottom)

                self.ox = (self.xleft + self.xright) / 2

                self.oy = (self.ytop + self.ybottom) / 2

                print("I'm in centrecolumn. new value of origin:")

                print(self.ox, self.oy)

            else:
                print("I'm in centrecolumn. y1 >= ytop, y1 <= bottom")
                inside(xleft, ytop, xright, ybottom, x1, y1, x2, y2)

        if self.x1_arr[counter] >= self.xleft and self.x1_arr[counter] <= self.xright and self.y1_arr[
            counter] >= self.ytop and self.y1_arr[counter] <= self.ybottom and self.x2_arr[
            counter] >= self.xleft and self.x2_arr[counter] <= self.xright and self.y2_arr[counter] >= self.ytop and \
                self.y2_arr[counter] <= self.ybottom:
            self.display = True
        elif self.x1_arr[counter] < self.xleft:
            print("I'm still outside, x1_arr[counter]<xleft, i'm going to leftcolumn")
            leftcolumn(self.xleft, self.ytop, self.xright, self.ybottom,
                       self.x1_arr[counter], self.y1_arr[counter],
                       self.x2_arr[counter], self.y2_arr[counter])
        elif self.x1_arr[counter] > self.xright:
            print("I'm still outside, x1_arr[counter] > xright")
            first_value = rotate180c(self.ox, self.oy, self.x1_arr[counter], self.y1_arr[counter])
            self.x1_arr[counter] = first_value[0]
            self.y1_arr[counter] = first_value[1]
            second_value = rotate180c(self.ox, self.oy, self.x2_arr[counter], self.y2_arr[counter])
            self.x2_arr[counter] = second_value[0]
            self.y2_arr[counter] = second_value[1]
            print("I'm still outside, After rotate180c new value of x1, y1, x2,y2")
            print(self.x1_arr[counter], self.y1_arr[counter], self.x2_arr[counter], self.y2_arr[counter])

            first_value = reflectxminusy(self.ox, self.oy, self.xleft, self.ytop)
            second_value = reflectxminusy(self.ox, self.oy, self.xright, self.ybottom)
            self.xleft = second_value[1]
            self.xright = first_value[1]
            self.ytop = second_value[0]
            self.ybottom = first_value[0]

            print("I'm still outside, After reflectxminusy new value of xleft, ytop, xright,ybottom")
            print(self.xleft, self.ytop, self.xright, self.ybottom)

            print("I'm still outside, new value of origin")
            self.ox = (self.xleft + self.xright) / 2
            self.oy = (self.ytop + self.ybottom) / 2
            print(self.ox, self.oy)
            print("I'm still outside, I'm going to leftcolumn")

            leftcolumn(self.xleft, self.ytop, self.xright, self.ybottom,
                       self.x1_arr[counter], self.y1_arr[counter],
                       self.x2_arr[counter], self.y2_arr[counter])

            first_value = rotate180c(self.ox, self.oy, self.x1_arr[counter], self.y1_arr[counter])
            self.x1_arr[counter] = first_value[0]
            self.y1_arr[counter] = first_value[1]
            second_value = rotate180c(self.ox, self.oy, self.x2_arr[counter], self.y2_arr[counter])
            self.x2_arr[counter] = second_value[0]
            self.y2_arr[counter] = second_value[1]

            print("I'm still outside, After rotate180c new value of x1, y1, x2,y2")
            print(self.x1_arr[counter], self.y1_arr[counter], self.x2_arr[counter], self.y2_arr[counter])

            first_value = reflectxminusy(self.ox, self.oy, self.xleft, self.ytop)
            second_value = reflectxminusy(self.ox, self.oy, self.xright, self.ybottom)
            self.xleft = second_value[1]
            self.xright = first_value[1]
            self.ytop = second_value[0]
            self.ybottom = first_value[0]

            print("I'm still outside, After reflectxminusy new value of xleft, ytop, xright,ybottom")
            print(self.xleft, self.ytop, self.xright, self.ybottom)

        else:
            print("I'm still outside, x1_arr[counter]>=xleft, x1_arr[counter] <= right i'm going to centrecolumn")
            centrecolumn(self.xleft, self.ytop, self.xright, self.ybottom,
                         self.x1_arr[counter], self.y1_arr[counter],
                         self.x2_arr[counter], self.y2_arr[counter])

    def crop(self, event=None):
        self.drawing_area.delete("gambar2")

        if self.x1_box_pt <= self.x2_box_pt:
            self.xleft = self.x1_box_pt
            self.xright = self.x2_box_pt
        else:
            self.xleft = self.x2_box_pt
            self.xright = self.x1_box_pt
        if self.y1_box_pt <= self.y2_box_pt:
            self.ytop = self.y1_box_pt
            self.ybottom = self.y2_box_pt
        else:
            self.ytop = self.y2_box_pt
            self.ybottom = self.y1_box_pt

        xleft_asli = self.xleft
        xright_asli = self.xright
        ytop_asli = self.ytop
        ybottom_asli = self.ybottom

        self.ox = (self.xleft + self.xright) / 2
        self.oy = (self.ytop + self.ybottom) / 2

        ox_asli = self.ox
        oy_asli = self.oy

        # ngecek doang valuenya dah disave ke array belum
        print(range(len(self.x1_arr) - 1))

        print("ox, oy")
        print(self.ox, self.oy)

        print("xleft, xright,ytop,ybottom")
        print(self.xleft, self.xright, self.ytop, self.ybottom)

        for counter in range(len(self.x1_arr)):

            x1_asli = self.x1_arr[counter]
            x2_asli = self.x2_arr[counter]
            y1_asli = self.y1_arr[counter]
            y2_asli = self.y2_arr[counter]

            print("ox, oy")
            print(self.ox, self.oy)

            print("xleft, xright,ytop,ybottom")
            print(self.xleft, self.xright, self.ytop, self.ybottom)

            # if self.x1_arr[counter] > self.x2_arr[counter] and self.y1_arr[counter] > self.y2_arr[counter]:
            # sementara_x = self.x1_arr[counter]
            # self.x1_arr[counter] = self.x2_arr[counter]
            # self.x2_arr[counter] = sementara_x
            # sementara_y = self.y1_arr[counter]
            # self.y1_arr[counter] = self.y2_arr[counter]
            # self.y2_arr[counter] = sementara_y

            self.display = None
            print("line x1")
            print(self.x1_arr[counter])
            print("line y1")
            print(self.y1_arr[counter])
            print("line x2")
            print(self.x2_arr[counter])
            print("line y2")
            print(self.y2_arr[counter])

            self.nln(counter)

            print(self.display)
            if self.display:
                print("new line x1")
                print(self.x1_arr[counter])
                print("new line y1")
                print(self.y1_arr[counter])
                print("new line x2")
                print(self.x2_arr[counter])
                print("new line y2")
                print(self.y2_arr[counter])
                if self.x1_arr[counter] == self.x2_arr[counter] and self.y1_arr[counter] == self.y2_arr[counter]:
                    self.drawing_area.create_rectangle(self.x1_arr[counter], self.y1_arr[counter], self.x1_arr[counter],
                                                       self.y1_arr[counter],
                                                       width=7,
                                                       tag="gambar")
                else:
                    # self.drawing_area.delete("gambar")
                    self.drawing_area.create_line(int(self.x1_arr[counter]), int(self.y1_arr[counter]),
                                                  int(self.x2_arr[counter]), int(self.y2_arr[counter]),
                                                  fill="red",
                                                  tag="gambar")

                self.x1_crop.append(self.x1_arr[counter])
                self.y1_crop.append(self.y1_arr[counter])
                self.x2_crop.append(self.x2_arr[counter])
                self.y2_crop.append(self.y2_arr[counter])

            self.xleft = xleft_asli
            self.xright = xright_asli
            self.ytop = ytop_asli
            self.ybottom = ybottom_asli
            self.ox = ox_asli
            self.oy = oy_asli

            self.x1_arr[counter] = x1_asli
            self.x2_arr[counter] = x2_asli
            self.y1_arr[counter] = y1_asli
            self.y2_arr[counter] = y2_asli

        self.xleft = None
        self.xright = None
        self.ytop = None
        self.ybottom = None
        self.ox = None
        self.oy = None

    def change_paint(self,event =None):
        self.Menggambar= False



    def change_bg(self,event = None):  # changing the background color canvas
        self.color_bg = colorchooser.askcolor(color=self.color_bg)[1]
        self.drawing_area['bg'] = self.color_bg

    def change_fg(self,event = None):  # changing the pen color
        self.color_fg = colorchooser.askcolor(color=self.color_fg)[1]


    def changeW(self,event = None): #change Width of pen through slider
        self.penwidth = event

    def __init__(self, root):
        width = 1000
        height = 600

        self.controls = Frame(root, padx=5, pady=5)
        Label(self.controls, text='Pen Width:', font=('arial 18')).grid(row=0, column=0)
        self.slider = ttk.Scale(self.controls, from_=0, to=100, command=self.changeW, orient=VERTICAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0, column=1, ipadx=30)
        self.controls.pack(side=LEFT)



        self.drawing_area = Canvas(root, width=width, height=height, bg=self.color_bg)
        self.drawing_area.pack(fill=BOTH,expand=True)
        if self.Menggambar:
            self.drawing_area.bind("<B1-Motion>", self.paint)
            self.drawing_area.bind("<ButtonRelease-1>", self.reset)
        else:
            self.drawing_area.bind("<ButtonPress-1>", self.left_but_down)
            self.drawing_area.bind("<ButtonRelease-1>", self.left_but_up)

        # dot_photo = PhotoImage(file="dot.png")
        B_pointer = Button(root, text="Pointer", command=self.pointer_button)
        B_pointer.pack(side=LEFT, padx=10, pady=10, ipadx=5, ipady=5)

        B_dot = Button(root, text="Dot", command=self.dot_button, state=ACTIVE)
        B_dot.config(state=ACTIVE)
        B_dot.pack(side=LEFT, padx=10, pady=10, ipadx=5, ipady=5)

        B_line = Button(root, text="Line", command=self.line_button, state=ACTIVE)
        B_line.pack(side=LEFT, padx=10, pady=10, ipadx=5, ipady=5)

        B_rect = Button(root, text="Rectangle", command=self.rect_button, state=ACTIVE)
        B_rect.pack(side=LEFT, padx=10, pady=10, ipadx=5, ipady=5)

        B_eraser = Button(root, text="Delete", command=self.eraser_button, state=ACTIVE)
        B_eraser.pack(side=LEFT, padx=10, pady=10, ipadx=5, ipady=5)

        B_clear = Button(root, text="Clear Canvas", command=self.clear_canvas, state=ACTIVE)
        B_clear.pack(side=LEFT, padx=10, pady=10, ipadx=5, ipady=5)

        B_refresh = Button(root, text="Refresh Rectangle", command=self.refresh_rect, state=ACTIVE)
        B_refresh.pack(side=LEFT, padx=10, pady=10, ipadx=5, ipady=5)

        B_crop = Button(root, text="Crop", command=self.crop)
        B_crop.pack(side=LEFT, padx=10, pady=10, ipadx=5, ipady=5)

        B_save= Button(root, text="Save", command=self.save_file)
        B_save.pack(side=LEFT, padx=10, pady=10, ipadx=5, ipady=5)

        B_load = Button(root, text="Load", command=self.load_file)
        B_load.pack(side=LEFT, padx=10, pady=10, ipadx=5, ipady=5)

        B_paint = Button(root, text="Paint", command=self.paint)
        B_paint.pack(side=LEFT, padx=10, pady=10, ipadx=5, ipady=5)


        # Save coordinate into array
        self.x1_arr = []
        self.x2_arr = []
        self.y1_arr = []
        self.y2_arr = []

        self.x1_crop = []
        self.x2_crop = []
        self.y1_crop = []
        self.y2_crop = []


        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        colormenu = Menu(menu)
        menu.add_cascade(label='Colors', menu=colormenu)
        colormenu.add_command(label='Brush Color', command=self.change_fg)
        colormenu.add_command(label='Background Color', command=self.change_bg)
        optionmenu = Menu(menu)
        menu.add_cascade(label='Options', menu=optionmenu)
        optionmenu.add_command(label='Clear Canvas', command=self.clear_canvas)
        optionmenu.add_command(label='Exit', command="")


root = Tk()

paint_app = PaintApp(root)

root.mainloop()
