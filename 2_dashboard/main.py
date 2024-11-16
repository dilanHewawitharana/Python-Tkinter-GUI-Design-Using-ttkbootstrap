import tkinter as tk
import matplotlib.pyplot as plt
from data import sales_data, inventory_data, product_data, sales_year_data, inventory_month_data
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#4C2A85", "#BE96FF", "#957DAD", "#5E366E", "#A98CCC"])

fig01, ax01 = plt.subplots()
ax01.bar(sales_data.keys(), sales_data.values())
ax01.set_title("Sales Data")
ax01.set_xlabel("Products")
ax01.set_ylabel("Sales")
# plt.show()

fig02, ax02 = plt.subplots()
ax02.barh(list(inventory_data.keys()), inventory_data.values())
ax02.set_title("Inventory Data")
ax02.set_xlabel("Inventory")
ax02.set_ylabel("Products")
# plt.show()

fig03, ax03 = plt.subplots()
ax03.pie(product_data.values(), labels=product_data.keys(), autopct='%1.1f%%')
ax03.set_title("Product Data")
# plt.show()

fig04, ax04 = plt.subplots()
ax04.plot(list(sales_year_data.keys()), list(sales_year_data.values()))
ax04.set_title("Sales Year Data")
ax04.set_xlabel("Years")
ax04.set_ylabel("Sales")
# plt.show()

fig05, ax05 = plt.subplots()
ax05.fill_between(inventory_month_data.keys(), inventory_month_data.values())
ax05.set_title("Inventory Month Data")
ax05.set_xlabel("Months")
ax05.set_ylabel("Inventory")
# plt.show()

root = tk.Tk()
root.title("Dashboard")
root.state("zoomed")

side_frame = tk.Frame(root, bg="#4C2A85")
side_frame.pack(side="left", fill="y")

label01 = tk.Label(side_frame, text="Sales", bg="#4C2A85", fg="white", font=("Arial", 20))
label01.pack(padx=50, pady=20)

charts_frame = tk.Frame(root)
charts_frame.pack()

upper_frame = tk.Frame(charts_frame)
upper_frame.pack(fill="both", expand=True)

chart01 = FigureCanvasTkAgg(fig01, upper_frame)
chart01.draw()
chart01.get_tk_widget().pack(side="left", fill="both", expand=True)

chart02 = FigureCanvasTkAgg(fig02, upper_frame)
chart02.draw()
chart02.get_tk_widget().pack(side="left", fill="both", expand=True)

chart03 = FigureCanvasTkAgg(fig03, upper_frame)
chart03.draw()
chart03.get_tk_widget().pack(side="left", fill="both", expand=True)

lower_frame = tk.Frame(charts_frame)
lower_frame.pack(fill="both", expand=True)

chart04 = FigureCanvasTkAgg(fig04, lower_frame)
chart04.draw()
chart04.get_tk_widget().pack(side="left", fill="both", expand=True)

chart05 = FigureCanvasTkAgg(fig05, lower_frame)
chart05.draw()
chart05.get_tk_widget().pack(side="left", fill="both", expand=True)


root.mainloop()