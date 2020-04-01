from tkinter import *
from ButtonFunctions import Database

    
class Window (object):
    def __init__(self,window):
            self.window=window         
            self.window.wm_title(" The Book Store")
            
            l1=Label(window, text='Book Title')
            l1.grid(column=0, row=0)

            l2=Label(window, text='Book Author')
            l2.grid(column=2, row=0)

            l3=Label(window, text='year')
            l3.grid(column=0, row=1)

            l4=Label(window, text='ISBN')
            l4.grid(column=2, row=1)


            self.title=StringVar()
            self.e1=Entry(window, width=16, textvariable=self.title)
            self.e1.grid(column=1,row=0)

            self.author=StringVar()
            self.e2=Entry(window, width=16, textvariable=self.author)
            self.e2.grid(column=3,row=0)

            self.year=StringVar()
            self.e3=Entry(window, width=16, textvariable=self.year)
            self.e3.grid(column=1,row=1)

            self.isbn=StringVar()
            self.e4=Entry(window, width=16, textvariable=self.isbn)
            self.e4.grid(column=3,row=1)

            self.list1 = Listbox(window, height=6, width=35)
            self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

            self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        # now we need to attach a scrollbar to the listbox, and the other direction,too
            sb1 = Scrollbar(window)
            sb1.grid(row=2, column=2, rowspan=6)
            self.list1.config(yscrollcommand=sb1.set)
            sb1.config(command=self.list1.yview)
            
            ##############for all buttons###################
            b1=Button(window,width= 14, text="View All", command=self.view_command)
            b1.grid(column=3 , row=2)

            b2=Button(window,width= 14,text="Search Entry", command=self.search_command)
            b2.grid(column=3 , row=3)

            b3 = Button(window,  width=14, text="Add entry", command=self.add_command)
            b3.grid(row=4, column=3)

            b4=Button(window,width= 14,text="Update selected", command=self.update_command)
            b4.grid(column=3 , row=5)

            b5=Button(window,width= 14,text="delete selected", command= self.delete_command)
            b5.grid(column=3 , row=6)

            b6=Button(window,width= 14,text="close", command=window.destroy)
            b6.grid(column=3 , row=7)

    def get_selected_row(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END,self.selected_tuple[4])
        except IndexError:
            pass                #in the case where the listbox is empty, the code will not execute

    def view_command(self):
        self.list1.delete(0, END)  # make sure we've cleared all entries in the listbox every time we press the View all button
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.title.get(), self.author.get(), self.year.get(), self.isbn.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.title.get(), self.author.get(), self.year.get(), self.isbn.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title.get(), self.author.get(), self.year.get(), self.isbn.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])
        self.view_command()

    def update_command(self):
        database.update(self.selected_tuple[0],self.title.get(), self.author.get(), self.year.get(), self.isbn.get())
        self.view_command()

window= Tk()
Window(window)
database=Database("BookStore.db")
window.mainloop()
