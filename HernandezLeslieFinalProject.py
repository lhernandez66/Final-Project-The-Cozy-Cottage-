import tkinter as tk
from tkinter import PhotoImage, messagebox

class CandyCottageApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x1300")
        self.root.title("The Candy Cottage")
        
        # Background image
        self.bg_image = PhotoImage(file=r"bluecottage.png")
        self.bg_text = "blue cottage"
        tk.Label(self.root, image=self.bg_image).place(relheight=1, relwidth=1)
        
        # Main Label
        tk.Label(root, text="The Candy Cottage", bg="light pink", fg="white", font=('Comic Sans MS', 35)).pack(padx=250, pady=250)
        
        # Main Button
        tk.Button(root, text="Open Candy Selection", bg="light pink", fg="white", font=('Comic Sans MS', 25), command=self.open_new_window).pack()

    def open_new_window(self):
        self.root.destroy()
        top = tk.Tk()
        top.geometry("1500x1300")
        top.title("Candy Selection")
        
        # Background image
        self.bg_image = PhotoImage(file=r"candies.png")
        self.bg_text = "candies"
        tk.Label(top, image=self.bg_image).place(relheight=1, relwidth=1)
        
        # Candy Selection Label
        tk.Label(top, text="Candy Selection:", bg="light pink", fg="white", font=('Comic Sans MS', 45)).pack(padx=155, pady=155)
        
        # Candy Selection Button Frame
        buttonframe = tk.LabelFrame(top)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.columnconfigure(2, weight=1)

        def add_to_cart(item, price):
            self.cart[item] = self.cart.get(item, 0) + 1
            self.update_cart_display()

        candies = {
            "Chocolate Pretzels": 16.99,
            "Chocolate Cherries": 17.99,
            "Funfetti Fudge": 19.99,
            "Flower Gummies": 10.99,
            "Peach Rings": 12.99,
            "Taffy Mix": 13.99
        }

        for i, (item, price) in enumerate(candies.items()):
            btn = tk.Button(buttonframe, text=f"{item} - ${price:.2f}", font=('Arial', 25), command=lambda i=item, p=price: add_to_cart(i, p))
            btn.grid(row=i//3, column=i%3, sticky=tk.W+tk.E)
            btn.config(bg="light pink", fg="white")

        # Adjusting padding and fill for the button frame
        buttonframe.pack(padx=50, pady=50, expand=True)
        
        # Cart
        self.cart = {}
        self.total = tk.DoubleVar()
        self.total.set(0.00)
        self.cart_display = tk.Label(top, text="Cart:", bg="light pink", fg="white", font=('Comic Sans MS', 35))
        self.cart_display.pack(padx=10)
        self.cart_listbox = tk.Listbox(top, height=6, font=('Arial', 15))
        self.cart_listbox.pack(pady=10)
        
        # Total
        tk.Label(top, text="Total:", bg="light pink", fg="white", font=('Comic Sans MS', 25)).pack()
        tk.Label(top, textvariable=self.total, bg="light pink", fg="white", font=('Arial', 15)).pack(pady=10)

        # Delete Button
        tk.Button(top, text="Empty Cart", bg="light pink", fg="white", font=('Comic Sans MS', 20), command= self.delete_all_items).pack()
        # Checkout Button
        tk.Button(top, text="Checkout", bg="light pink", fg="white", font=('Comic Sans MS', 25), command=lambda: self.checkout(top)).pack()
    # Cart Display    
    def update_cart_display(self):
        self.cart_listbox.delete(0, tk.END)
        for item, quantity in self.cart.items():
            self.cart_listbox.insert(tk.END, f"{item} x {quantity}")
        self.calculate_total()
        
    # Delete all Items
    def delete_all_items(self):
        self.cart_listbox.delete(0, tk.END)
        self.cart.clear()
        self.calculate_total()
        
    # Calculate Total
    def calculate_total(self):
        if not self.cart:
            total = "Enter valid input"
        candies = {
            "Chocolate Pretzels": 16.99,
            "Chocolate Cherries": 17.99,
            "Funfetti Fudge": 19.99,
            "Flower Gummies": 10.99,
            "Peach Rings": 12.99,
            "Taffy Mix": 13.99
        }
        subtotal = sum(candies[item] * self.cart[item] for item in self.cart)
        total = subtotal
        self.total.set(f"${total:.2f}")

    def checkout(self, top):
        # Check if cart is empty
        if not self.cart:
            messagebox.showwarning("Empty Cart", "Your cart is empty!")
            return
        
        top.destroy()
        checkout_window = tk.Tk()
        checkout_window.geometry("1500x1300")
        checkout_window.title("Checkout")
        checkout_window.configure(bg="light pink")


        # Customer Information Labels and Entry Widgets
        tk.Label(checkout_window, text="Name:", bg="light pink", fg="white", font=('Comic Sans MS', 30)).pack()
        name_entry = tk.Entry(checkout_window, width=30)
        name_entry.pack(pady=20)

        tk.Label(checkout_window, text="Phone Number:", bg="light pink", fg="white", font=('Comic Sans MS', 30)).pack()
        phone_entry = tk.Entry(checkout_window, width=30)
        phone_entry.pack(pady=20)

        tk.Label(checkout_window, text="Email:", bg="light pink", fg="white", font=('Comic Sans MS', 30)).pack()
        email_entry = tk.Entry(checkout_window, width=30)
        email_entry.pack(pady=20)

        tk.Label(checkout_window, text="Shipping Address:", bg="light pink", fg="white", font=('Comis Sans MS', 30)).pack()
        address_entry = tk.Entry(checkout_window, width=30)
        address_entry.pack(pady=20)

        tk.Label(checkout_window, text="Card Information:", bg="light pink", fg="white", font=('Comic Sans MS', 30)).pack()
        card_entry = tk.Entry(checkout_window, width=30)
        card_entry.pack(pady=20)

        # Place Order Button
        def place_order():
            # Check if any Customer Info Entries are Empty
            if not all((name_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get(), card_entry.get())):
                messagebox.showerror("Incomplete Information", "Please fill out all fields.")
                return
            # Order Placed
            messagebox.showinfo("Order Placed", "Your order has been placed successfully!")
            checkout_window.destroy
        # Order Button    
        tk.Button(checkout_window, text="Place Order", bg="light pink", fg="white", font=('Comic Sans MS', 20), command=place_order).pack()
        def exit_checkout():
            checkout_window.destroy()
        # Exit Button
        tk.Button(checkout_window, text="Exit", bg="white", fg="red", font=('Comic Sans MS', 20), command=exit_checkout).pack(side=tk.RIGHT, padx=10, pady=15, anchor=tk.SE)
if __name__ == "__main__":
    root = tk.Tk()
    app = CandyCottageApp(root)
    root.mainloop()
