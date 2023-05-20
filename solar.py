import tkinter

class Solar:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window, width=40000, height=40000, bg="black") # bg sets the background color to black
        self.canvas.pack()
        
        # Draw the Sun
        sun_radius = 50 # Set the radius of the sun
        sun_color = "yellow" # Set the color of the sun
        x = 200 # Set the x-coordinate of the center of the sun
        y = 200 # Set the y-coordinate of the center of the sun
        self.canvas.create_oval(x-sun_radius, y-sun_radius, x+sun_radius, y+sun_radius, fill=sun_color) # Draw the sun using create_oval method

        # Defining each planet
        planets = [
            {"name": "Mercury", "radius": 25, "color": "gray", "distance": 900},
            {"name": "Venus", "radius": 25, "color": "orange", "distance": 2000},
            {"name": "Earth", "radius": 30, "color": "blue", "distance": 3000},
            {"name": "Mars", "radius": 30, "color": "red", "distance": 4000},
            {"name": "Jupiter", "radius": 35, "color": "brown", "distance": 5000},
            {"name": "Saturn", "radius": 35, "color": "tan", "distance": 6000},
            {"name": "Uranus", "radius": 25, "color": "light blue", "distance": 7200},
            {"name": "Neptune", "radius": 15, "color": "dark blue", "distance": 8230},
            {"name": "Pluto", "radius": 15, "color": "light gray", "distance": 9200}
        ]

    
       
        # Draw the planets
        for planet in planets:
            radius = planet["radius"] # Get the radius of the current planet
            color = planet["color"] # Get the color of the current planet
            distance = planet["distance"] # Get the distance of the current planet
            
            x = 200 + distance/10 # Calculate the x-coordinate of the center of the current planet
            y = 200 # Set the y-coordinate of the center of the current planet
            
            self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color) # Draw the current planet using create_oval method
            self.canvas.create_text(x, y+radius+10, text=planet["name"], fill="white") # Label the current planet using create_text method
           


        self.main_window.title("Solar System")
        tkinter.mainloop()

if __name__ == "__main__":
    solar_system = Solar()
