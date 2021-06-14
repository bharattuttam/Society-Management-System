from BackGroundPage import *
from Components.ButtonComponent import WhiteButton
from DatabaseHelper import *
from Components.table import SimpleTable
from Components.MessageComponent import WhiteMessage
from Components.ButtonComponent import *
from Components.ButtonComponent import *
from tkinter import messagebox
# from AdminAnalytics import Analytics
from Queries.Admin import *
from PIL import Image, ImageTk


class AdminHomePage(BackGroundPage):
    def __init__(self, root, admin_details):
        print("Admin home page called")
        super().__init__(root)
        self.root.state('zoomed')  # Maximize the screen
                                                                                        # Dict received from DATABASE. Eg=> {id:2, name:'Ritesh', password:'SGT', email:'riteshagicha@gmail.com', photo:'RiteshPic3.jpg'}
        self.details = admin_details
        # Dictionary to store the pending order checkbox IntVars
        self.dct_IntVar = {}

        self.admin_page = WhiteMessage(self.f, text="Admin Page")
        self.admin_page.place(x=150, y=100)
        # self.add_admin_details()
        self.add_buttons()


    def add_buttons(self):
        # Add 3 buttons
        # View Maintenance Details
        # View Notices
        # logout
        # view complaints

        # doesn't matter, you can add to the frame or panel(Label- for image)
        self.pending_button = GrayButton(self.f, "View Maintanance Details", self.Give_all_Bills)
        self.pending_button.place(x=400, y=90)
        self.completed_button = GrayButton(self.f, "View Complaints", self.view_complaints)
        self.completed_button.place(x=600, y=90)
        self.logout = WhiteButton(self.f, "Logout", self.admin_logout, width=10)

        self.logout.place(x=800, y=20)

        self.order_status_button = GrayButton(self.f, text="Notice", command=self.notice_image)
        self.order_status_button.place(x=850, y=100)

    def notice_image(self):
        self.menu_frame = Frame(self.panel, height=500, width=600, bg="white")
        self.menu_frame.place(x=730, y=170)
        self.menu_frame.pack_propagate(0)

        self.raw_menu_image = Image.open("images/notice.jpg")
        self.raw_menu_image = self.raw_menu_image.resize((600, 500))
        self.menu_img = ImageTk.PhotoImage(self.raw_menu_image)
        self.menu_panel = Label(self.menu_frame, image=self.menu_img)
        self.menu_panel.pack()

    def view_complaints(self):
        # same as pending orders, only diff is we dont need checkbutton here
        query = Query.ALL_COMPLAINTS
        result = DatabaseHelper.get_all_data(query)
        self.complaint_table = SimpleTable(self.f, rows=len(result), columns=len(result[0]), height=500, width=660)
        self.complaint_table.grid_propagate(0)
        self.complaint_table.place(x=30, y=170)

        for i in range(len(result)):
            for j in range(len(result[0])):
                self.complaint_table.set(row=i, column=j, value=result[i][j])


    def Give_all_Bills(self):


            query = Query.ALL_BILLS
            # parameters = (self.details["MemberId"],)
            result = DatabaseHelper.get_all_data(query)

            self.recent_orders_table = SimpleTable(self.f, rows=len(result), columns=len(result[0]), width=570,
                                                   height=500)
            self.recent_orders_table.grid_propagate(0)
            self.recent_orders_table.place(x=30, y=170)
            for i in range(len(result)):
                for j in range(len(result[0])):
                    if (j == 0):
                        self.recent_orders_table.set(row=i, column=j, value=result[i][j], width=50)
                    else:
                        self.recent_orders_table.set(row=i, column=j, value=result[i][j], width=10)

    def admin_logout(self):
        import MainPage as main
        self.f.destroy()
        main.MainPage(self.root)


if (__name__ == "__main__"):
    root = Tk()
    admin_details = {'AdminId': 1, 'AdminName': 'bharat', 'AdminPassword': 'bharat'}

    a = AdminHomePage(root, admin_details)
    root.mainloop()
