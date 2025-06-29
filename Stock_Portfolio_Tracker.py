import tkinter as tk
from tkinter import messagebox

# Create an empty list to store stock portfolio data
Portfolio = []

# Function to add a stock entry to the portfolio
def add_stock():
    # Get user input from entry fields
    stock_name = entry_name.get()
    
    # Validate shares and price input
    try:
        shares = int(entry_shares.get())
        price = float(entry_price.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for Shares and Price.")
        return

    # Calculate total value of the stock investment
    total_value = shares * price

    # Create dictionary with stock details
    stock_info = {
        "Stock": stock_name,
        "Share": shares,
        "Price": price,
        "Total Value": total_value,
    }

    # Add the dictionary to the portfolio list
    Portfolio.append(stock_info)

    # Update the display box with current portfolio info
    update_display()

    # Clear input fields after adding the stock
    entry_name.delete(0, tk.END)
    entry_shares.delete(0, tk.END)
    entry_price.delete(0, tk.END)

# Function to update the portfolio display in the text box
def update_display():
    text_display.delete("1.0", tk.END)  # Clear previous output

    total_portfolio_value = 0

    # Loop through each stock and display the details
    for stock in Portfolio:
        text_display.insert(tk.END, f"{stock['Stock']} | Shares: {stock['Share']} | ₹{stock['Price']} each | Total: ₹{stock['Total Value']:.2f}\n")
        total_portfolio_value += stock['Total Value']

    # Display total investment value
    text_display.insert(tk.END, "-" * 50 + "\n")
    text_display.insert(tk.END, f"💰 Total Investment: ₹{total_portfolio_value:.2f}")

# Function to save portfolio data to a text file
def save_to_file():
    if not Portfolio:
        messagebox.showwarning("No Data", "No stock data to save!")
        return

    # Calculate total investment
    total_portfolio_value = sum(stock['Total Value'] for stock in Portfolio)

    # Open file in write mode with utf-8 encoding to support ₹ symbol
    with open("portfolio_summary.txt", "w", encoding="utf-8") as file:
        file.write("Your Stock Investment Details:\n")
        file.write("-" * 40 + "\n")
        for stock in Portfolio:
            file.write(f"{stock['Stock']}: {stock['Share']} shares × ₹{stock['Price']} = ₹{stock['Total Value']:.2f}\n")
        file.write("-" * 50 + "\n")
        file.write(f"Total Investment: ₹{total_portfolio_value:.2f}\n")

    messagebox.showinfo("Saved", "✅ Portfolio saved to 'portfolio_summary.txt'")



# Create the main window
root = tk.Tk()

# window title
root.title("Stock Portfolio Tracker") 

# Window size
root.geometry("500x500")                    

# Label and Entry for Stock Name
tk.Label(root, text="Stock Name / Ticker").pack()
entry_name = tk.Entry(root, width=30)
entry_name.pack()

# Label and Entry for Number of Shares
tk.Label(root, text="No. of Shares").pack()
entry_shares = tk.Entry(root, width=30)
entry_shares.pack()

# Label and Entry for Price per Share
tk.Label(root, text="Price per Share (₹)").pack()
entry_price = tk.Entry(root, width=30)
entry_price.pack()

# Button to add stock to portfolio
tk.Button(root, text="➕ Add Stock", command=add_stock).pack(pady=10)

# Button to save portfolio to file
tk.Button(root, text="💾 Save to File", command=save_to_file).pack()

# Text box to display stock portfolio details
text_display = tk.Text(root, height=15, width=60)
text_display.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()