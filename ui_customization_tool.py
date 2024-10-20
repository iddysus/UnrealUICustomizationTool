
import tkinter as tk
from tkinter import filedialog

# Written by Idlan bin Hafiz

# Main window setup
root = tk.Tk()
root.title("UI Customization Tool")
root.geometry("800x600")

# Canvas where UI elements will be placed
canvas = tk.Canvas(root, bg="gray", width=700, height=500)
canvas.pack(pady=20)

# A list to keep track of UI elements on the canvas
ui_elements = []

# Function to create a draggable rectangle (simulating a UI element like a health bar)
def create_ui_element():
    element = canvas.create_rectangle(50, 50, 150, 100, fill="green", tags="draggable")
    ui_elements.append(element)

# Function to allow dragging of the elements
def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.canvasx(event.x)
    y = widget.canvasy(event.y)
    
    # Move the object on the canvas
    canvas.move(tk.CURRENT, x - widget.startX, y - widget.startY)
    widget.startX = x
    widget.startY = y

# Create a menu for adding new elements
menu = tk.Menu(root)
root.config(menu=menu)

# Add "Create Element" option
menu.add_command(label="Add UI Element", command=create_ui_element)

# Save the layout in JSON format
def save_layout():
    layout = []
    
    for element in ui_elements:
        coords = canvas.coords(element)  # Get the position of the UI element
        layout.append({
            "type": "rectangle",
            "coords": coords
        })
    
    # Save the layout to a JSON file
    save_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if save_path:
        import json
        with open(save_path, 'w') as file:
            json.dump(layout, file)
        print(f"Layout saved to {save_path}")

# Add a save option to the menu
menu.add_command(label="Save Layout", command=save_layout)

# Bind mouse events for dragging
canvas.tag_bind("draggable", "<Button-1>", drag_start)
canvas.tag_bind("draggable", "<B1-Motion>", drag_motion)

root.mainloop()
