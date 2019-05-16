from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.font import Font
from tkinter import filedialog
from tkinter.ttk import Combobox
# import pdb

# pdb.set_trace()
class create_writing_pad:
    def __init__(self,root):
        self.flag=0
        self.current_name="no_name"
        root.geometry('300x300+300+300')
        self.main_menu = Menu(root)
        root.config(menu = self.main_menu)
        self.creating_file_menu()
        self.creating_edit_menu()
        self.creating_font_menu()
        self.create_shortcuts()
        self.font_size = 14
        self.font_family = 'Times New Roman'
        self.font_color = 'green'
        self.some_art()
        self.font_underline = 0
        self.my_font = Font(family=self.font_family,size=self.font_size,underline=self.font_underline)
        self.text_area = Text(root,bg="black",fg=self.font_color,selectbackground='orange',wrap=WORD ,padx=10,pady=10,undo=True)
        self.text_area.configure(font=self.my_font)
        self.text_area.pack(fill=BOTH,expand=1)

    def creating_file_menu(self):
        self.file_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label = '     file       ',menu=self.file_menu)
        self.file_menu.add_command(label = 'New window ctl+N',command = self.new_window)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = ' open file ctl+O',command = self.open_file)
        self.file_menu.add_command(label = '   save   ctl+s ',command = self.save)
        self.file_menu.add_command(label = '  save as ctl+S ',command = self.save_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = '   exit   ctl+E ',command = self.willing_to_exit)


    def creating_edit_menu(self):
        self.edit_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label='   edit         ',menu=self.edit_menu)
        self.edit_menu.add_command(label='   undo   ctl+u ',command = self.undo)
        self.edit_menu.add_command(label='   redo   ctl+r ',command = self.redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label='    cut   ctl+X ',command = self.cut_selected)
        self.edit_menu.add_command(label='   copy   ctl+C ',command = self.copy_selected)
        self.edit_menu.add_command(label='  paste   ctl+v ',command = self.paste_selected)
        self.edit_menu.add_separator()
        self.more_commands = Menu(self.edit_menu)
        self.edit_menu.add_cascade(label='   more   ',menu=self.more_commands)
        self.more_commands.add_command(label='   view   ',command=self.make_new_file) 
        self.more_commands.add_command(label='    go    ',command=self.make_new_file) 
        self.more_commands.add_command(label='   debug  ',command=self.make_new_file) 
        self.more_commands.add_command(label=' terminal ',command=self.make_new_file) 

    def creating_font_menu(self):
        self.font_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="   font         ",menu=self.font_menu)
        self.font_menu.add_command(label="   size   ctl+F ",command=self.adjust_size)
        # self.font_menu.add_command(label="  color   ",command=self.change_text_color)
        # self.font_menu.add_separator()
        # self.padding_menu = Menu(self.font_menu)
        # self.font_menu.add_cascade(label="  padding ",menu=self.padding_menu)
        # self.padding_menu.add_command(label="   padX   ",command=self.padding_in_x)
        # self.padding_menu.add_command(label="   padY   ",command=self.padding_in_y)
        # self.font_menu.add_separator()
        # self.font_menu.add_command(label="  family  ",command=self.choose_family)
        # self.font_menu.add_command(label="  weight  ",command=self.select_weight)

    def draw_structure(self):
        if self.flag == 0:
            self.make_board()
        self.structure = self.cmbx.get()
        if self.structure == 'polygon':
            self.points = list(simpledialog.askstring('coordinates','enter x,y coordinates of all points ex: x1,y1,x2,y2...').split(','))
            self.points.append(self.points[0])
            self.points.append(self.points[1])
            print(self.points)
            self.choosen_color='black'
            self.choosen_color = simpledialog.askstring('choose color','enter color to fill in  structure')
            self.pln = self.canvas.create_polygon(self.points,fill=self.choosen_color,outline='black')
        elif self.structure == 'select':
            pass
        else:
            x1,y1,x2,y2 = simpledialog.askstring('coordinates','enter two points ex: x1,y1,x2,y2...').split(',')
            self.choosen_color='black'
            self.choosen_color = simpledialog.askstring('choose color','enter color to fill in  structure')
            if self.structure == 'line':
                self.line = self.canvas.create_line(x1,y1,x2,y2)
            if self.structure == 'arc':
                self.angle_at = simpledialog.askinteger('angle','enter the angle at center in degree')
                self.arc = self.canvas.create_arc(x1,y1,x2,y2,fill=self.choosen_color,extent=self.angle_at)
            if self.structure == 'rectangle':
                self.rectangle = self.canvas.create_rectangle(x1,y1,x2,y2,fill=self.choosen_color)
            if self.structure == 'oval':
                self.oval = self.canvas.create_oval(x1,y1,x2,y2,fill=self.choosen_color)

    def some_art(self):
            self.art = Menu(self.main_menu)
            self.main_menu.add_cascade(label=" some art ",menu=self.art)
            self.art.add_command(label="add board ",command=self.make_board)
            self.art.add_command(label="deleteboard",command=self.delete_board)
            self.art.add_command(label='draw selected',command=self.draw_structure)
            self.l = ['line','arc','rectangle','oval','polygon']
            self.cmbx = Combobox(root,values=self.l,width=10)
            self.cmbx.set('select')
            self.cmbx.pack()

            

    def make_board(self):
        s = simpledialog.askstring('willing a board','enter height ,weight of board you want')
        if s:
            self.flag=1
            ht,wt = map(int,s.split(','))
            print(f"{ht} {wt}")
            pos = simpledialog.askstring('postion of board','enter x,y coordinates')
            x1,y1 =  map(int,pos.split(','))
            self.clr = simpledialog.askstring('color','enter background color you want')
            self.canvas = Canvas(self.text_area,height=ht,width=wt,bg=self.clr)
            self.canvas.place(x=x1,y=y1)


    def delete_board(self):
        self.undo()

        
    def willing_to_exit(self,event=None):
        agreement = messagebox.askyesnocancel('exit','do you really want to exit')
        if agreement == True:
            root.quit()
    
    def make_new_file(self):
        pass

    def new_window(self,event=None):
        top = Toplevel()
        top.title('new window')
    
    def open_file(self,event=None):
        opening = filedialog.askopenfile(initialdir="D://",title="open file",filetypes=(('text files','.txt'),('all files','.*')))
        if opening != None:
            self.text_area.delete(1.0,END)
            for i in opening:
                self.text_area.insert(INSERT,i)
            self.current_name=opening.name 
            opening.close()

    def save(self,event=None):
        if self.current_name == 'no_name':
            self.save_as(event)
        else:
            f = open(self.current_name,'w')
            for line in self.text_area.get(1.0,END):
                f.write(line)
            f.close()
        

    def save_as(self,event=None):
        file = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if file != None:
            for j in self.text_area.get(1.0,END):
                file.write(j)
            self.current_name = file.name
            file.close()

    def undo(self,event=None):
        self.text_area.edit_undo()

    def redo(self,event=None):
        self.text_area.edit_redo()

    def copy_selected(self,event=None):
        self.copying = self.text_area.selection_get()
        self.learn=self.copying
        print(self.learn)
        # or we can use
        # self.text_area.clipboard_clear()
        # self.text_area.clipboard_append(self.text_area.selection_get())

    def cut_selected(self,event=None):
        self.cut = self.text_area.selection_get()
        self.learn=self.cut
        # pos = self.text_area.get(1.0,END).find(self.cut)
        # print(pos)
        self.text_area.delete("sel.first","sel.last")
        # print(len(self.learn))

    def paste_selected(self,event=None):
        self.text_area.insert(INSERT,self.learn)

    def adjust_size(self,event=None):
        self.adjusted_size = simpledialog.askinteger('font size','enter font size')
        self.font_size = self.adjusted_size
        self.my_font = Font(family=self.font_family,size=self.font_size,underline=self.font_underline)
        self.text_area.configure(font=self.my_font)

    # def change_text_color(self):
    #     self.adjusted_color = simpledialog.askstring('font color','enter font color')
    #     self.font_color = self.adjusted_color
    #     self.cutting = self.text_area.get(1.0,END)
    #     self.cutting.color = self.font_color
    #     self.text_area.delete(1.0,END)
    #     self.text_area.insert(INSERT,self.cutting,foreground=self.font_color)

    # def padding_in_x(self):
    #     pass

    # def padding_in_y(self):
    #     pass

    # def choose_family(self):
    #     self.adjusted_size = simpledialog.askinteger('font size','enter font size')
    #     self.font_size = self.adjusted_size
    #     self.my_font = Font(family=self.font_family,size=self.font_size,underline=self.font_underline)
    #     self.text_area.configure(font=self.my_font)

    # def select_weight(self):
    #     self.adjusted_size = simpledialog.askinteger('font size','enter font size')
    #     self.font_size = self.adjusted_size
    #     self.my_font = Font(family=self.font_family,size=self.font_size,underline=self.font_underline)
    #     self.text_area.configure(font=self.my_font)

    def create_shortcuts(self):
        root.bind('<Control-N>',self.new_window)
        root.bind('<Control-O>',self.open_file)
        root.bind('<Control-s>',self.save)
        root.bind('<Control-S>',self.save_as)
        root.bind('<Control-E>',self.willing_to_exit)
        root.bind('<Control-u>',self.undo)
        root.bind('<Control-r>',self.redo)
        root.bind('<Control-X>',self.cut_selected)
        root.bind('<Control-C>',self.copy_selected)
        root.bind('<Control-v>',self.paste_selected)
        root.bind('<Control-F>',self.adjust_size)
        

    

root = Tk()
b = create_writing_pad(root)
root.title('my_text_editor')
root.mainloop()
