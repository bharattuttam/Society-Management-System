from Components.MessageComponent import WhiteMessage
from Components.ButtonComponent import *
from DatabaseHelper import *
from Components.table import SimpleTable
from PIL import Image, ImageTk
from tkinter import messagebox
from Queries.Customer import *
from BackGroundPage import *
from CreateComplaint import *
import datetime


class CustomerHomePage(BackGroundPage):
    def __init__(self, root, customer_details: dict):
        super().__init__(root)
        # store customer details dictionary here
        self.details = customer_details
        self.root.state('zoomed')
        print(self.details)
        # create dictionary for food menu items
        self.dct_IntVar = {}
        self.m = WhiteMessage(self.panel, text=f"Welcome {self.details['MemberName']}")
        self.m.place(x=50, y=100)
        self.m.grid_propagate(0)
        self.add_buttons()

    def add_buttons(self):
# Add 5 buttons- logout, check  Maintenance , Pay Maintenance ,Check notice ,Create complaint
        self.logout = WhiteButton(self.f, text="Logout", command=self.customer_logout)
        self.logout.place(x=800, y=30)

        self.order_history_button = GrayButton(self.f, text="Check Maintenance", command=self.recent_bills)
        self.order_history_button.place(x=250, y=100)

        self.order_status_button = GrayButton(self.f, text="Notice", command=self.notice_image)
        self.order_status_button.place(x=650, y=110)


        self.new_user_button = GrayButton(self.panel, "Have a Complain?", CreateComplaint, borderwidth=2, relief=RIDGE)
        self.new_user_button.place(x=1000, y=110)


        # self.order_history_button = GrayButton(self.f, text="Pay Maintenance", command=self.view_pending_orders)
        # self.order_history_button.place(x=500, y=100)


    def customer_logout(self):
        import MainPage
        self.f.destroy()
        self.redirect = MainPage.MainPage(self.root)

    def notice_image(self):
        self.menu_frame = Frame(self.panel, height=500, width=600, bg="white")
        self.menu_frame.place(x=650, y=170)
        self.menu_frame.pack_propagate(0)

        self.raw_menu_image = Image.open("images/notice.jpg")
        self.raw_menu_image = self.raw_menu_image.resize((600, 500))
        self.menu_img = ImageTk.PhotoImage(self.raw_menu_image)
        self.menu_panel = Label(self.menu_frame, image=self.menu_img)
        self.menu_panel.pack()

    def execute_order(self):
        selected_items = []
        for key, value in self.dct_IntVar.items():
            if (value.get() == 1):
                selected_items.append(key)
                self.dct_IntVar[key].set(0)
        print(selected_items)
        if (len(selected_items) == 0):
            messagebox.showwarning("No order", "Please select atleast one food order to execute")
        else:
            query = Query.EXECUTE_ORDERS
            DatabaseHelper.execute_all_data_multiple_input(query, selected_items)
            messagebox.showinfo("Success", f"Order Id(s) {selected_items} executed")
            self.view_pending_orders()

    def view_pending_orders(self):
        # Add execute button
        # Add table that shows pending orders with checkbutton
        self.execute_button = WhiteButton(self.f, "Execute Order", self.execute_order)
        self.execute_button.place(x=500, y=150)
        query = Query.PENDING_ORDERS
        result = DatabaseHelper.get_all_data(query)
        print(result)

        self.orders_table = SimpleTable(self.f, rows=len(result), columns=len(result[0]), height=500, width=650)
        self.orders_table.place(x=500, y=200)
        self.orders_table.grid_propagate(0)
        self.text_font = ("MS Serif", 12)

        for i in range(1, len(result)):
            # store FoodOrderID as key and a checkbutton variable as value
            self.dct_IntVar[result[i][0]] = IntVar()

        for i in range(len(result)):
            for j in range(len(result[0])):
                if (j == 0 and i != 0):
                    # Put checkbutton in the all first column apart from the first row
                    c = Checkbutton(self.orders_table, text=result[i][j], font=self.text_font,
                                    variable=self.dct_IntVar.get(result[i][j]))
                    self.orders_table.set(row=i, column=j, value=result[i][j], widget=c)
                else:
                    self.orders_table.set(row=i, column=j, value=result[i][j])


    def recent_bills(self):

        query = Query.RECENT_BILLS
        parameters = (self.details["MemberId"],)
        result = DatabaseHelper.get_all_data(query, parameters)

        self.recent_orders_table = SimpleTable(self.f, rows=len(result), columns=len(result[0]), width=570, height=500)
        self.recent_orders_table.grid_propagate(0)
        self.recent_orders_table.place(x=30, y=170)
        for i in range(len(result)):
            for j in range(len(result[0])):
                if (j == 0):
                    self.recent_orders_table.set(row=i, column=j, value=result[i][j], width=50)
                else:
                    self.recent_orders_table.set(row=i, column=j, value=result[i][j], width=10)








if __name__ == '__main__':
    root = Tk()
    details = { 'MemberId': 1, 'MemberName': 'bharat', 'MemberPassword': 'bharat', 'MemberContact': 7303064007, 'MemberEmailId': 'bharatuttam@gmail.com'}
    c = CustomerHomePage(root, details)
    root.mainloop()
