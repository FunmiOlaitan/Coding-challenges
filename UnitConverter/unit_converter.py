import tkinter as tk
from tkinter import ttk

class UnitConverterApp:
    def __init__(self, root):
        # Main window setup 
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("300x200")

        # Variables to store user selections
        self.category_var = tk.StringVar() # (eg.Length, Temp)
        self.unit_from_var = tk.StringVar() # (e.g., Meter to Kilometer) 
        self.unit_to_var = tk.StringVar()
        self.value_var = tk.StringVar()

        # Frame for screen 1
        self.screen1_frame = ttk.Frame(root)  # A container (frame) that holds all the widgets for the first screen
        self.screen1_frame.pack()
        # Frame for screen 2 
        self.screen2_frame = ttk.Frame(root)
        # Frame for screen 3
        self.screen3_frame = ttk.Frame(root)

        # Label and dropdown for selecting category
        ttk.Label(self.screen1_frame, text="Select Category:").pack() 
        self.category_dropdown = ttk.Combobox(self.screen1_frame, textvariable=self.category_var, values=["Length", "Temperature", "Volume", "Area"])
        self.category_dropdown.pack()
        ttk.Button(self.screen1_frame, text="Next", command=self.show_screen2).pack()
        
    def show_screen2(self):
        # Hide screen 1 and show screen 2
        self.screen1_frame.pack_forget()
        self.screen2_frame.pack()
        
        # Create widgets for screen 2 based on selected category
        category = self.category_var.get()

        if category == "Length":
            units = ["Meter (m)", "Kilometer (km)", "Centimeter (cm)"]
        elif category == "Temperature":
            units = ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]
        elif category == "Volume":
            units = ["Liter (L)", "Milliliter (mL)", "Cubic Meter (m³)"]
        elif category == "Area":
            units = ["Square Meter (m²)", "Square Kilometer (km²)", "Square Centimeter (cm²)"]
        
        # Labels and dropdowns for selecting units
        ttk.Label(self.screen2_frame, text="Convert from:").pack()
        self.unit_from_dropdown = ttk.Combobox(self.screen2_frame, textvariable=self.unit_from_var, values=units)
        self.unit_from_dropdown.pack()
        ttk.Label(self.screen2_frame, text="Convert to:").pack()
        self.unit_to_dropdown = ttk.Combobox(self.screen2_frame, textvariable=self.unit_to_var, values=units)
        self.unit_to_dropdown.pack(pady=(0,20))

        # Entry widget to input value to convert
        ttk.Label(self.screen2_frame, text="Enter value to convert:").pack()
        self.value_entry = ttk.Entry(self.screen2_frame, textvariable=self.value_var)  # Entry widget for input value
        self.value_entry.pack()
        # Convert button
        ttk.Button(self.screen2_frame, text="Convert", command=self.show_screen3).pack(pady=10)
    
    def show_screen3(self):
        # Hide screen 2 and show screen 3
        self.screen2_frame.pack_forget()
        self.screen3_frame.pack()

        # Perform conversion
        result = self.convert_units()

        result_label = ttk.Label(self.screen3_frame, text=f"Conversion Result: {result}")
        result_label.pack()

    def convert_units(self):
        # Retrieve input values 
        category = self.category_var.get()
        unit_from = self.unit_from_var.get()
        unit_to = self.unit_to_var.get()
        value = float(self.value_var.get()) # Convert input to float for mathematical operations

        # Conversion logic based on the category
        if category == "Length":
            return self.convert_length(unit_from, unit_to, value)
        elif category == "Temperature":
            return self.convert_temp(unit_from, unit_to, value)
        elif category == "Volume":
            return self.convert_volume(unit_from, unit_to, value)
        elif category == "Area":
            return self.convert_area(unit_from, unit_to, value)
       
    def convert_length(self, unit_from, unit_to, value):
        conversion_factors = {
            "Meter (m)": 1,
            "Kilometer (km)": 1000,
            "Centimeter (cm)": 0.01
        }
       
        # Convert to base unit (meters)
        value_in_meters = value * conversion_factors[unit_from]
        # Convert from base unit to target unit
        return value_in_meters / conversion_factors[unit_to]

    def convert_area(self, unit_from, unit_to, value):
        conversion_factors = {
            "Square Meter (m²)": 1,
            "Square Kilometer (km²)": 1e6,
            "Square Centimeter (cm²)": 0.0001
        }
        # Convert to base unit (square meters)
        value_in_square_meters = value * conversion_factors[unit_from]
        # Convert from base unit to target unit
        return value_in_square_meters / conversion_factors[unit_to]
    
    def convert_temp(self, unit_from, unit_to, value):
        pass

    def convert_volume(self, unit_from, unit_to, value):
        conversion_factors = {
            "Liter (L)": 1,
            "Milliliter (mL)": 0.001,
            "Cubic Meter (m³)": 1000
        }
        # Convert input to liters, then to the target unit
        value_in_liters = value * conversion_factors[unit_from]
        converted_value = value_in_liters / conversion_factors[unit_to]
        return converted_value

root = tk.Tk()
converter = UnitConverterApp(root)
# Start the Tkinter event loop
root.mainloop()