import tkinter

class Solar: # defines the class for the Solar system
  def __init__(self): # defines the initializer methods for the Solar class
    
    self.main_window = tkinter.Tk() # draws the GUI with tkinter
    self.main_window.title("Solar System") # sets the window title to solar system
    self.canvas = tkinter.Canvas(self.main_window, width=4000, height=4000, bg="black") #bg sets the background color to black
    self.canvas.pack() 
        
    
    # defines the properties of the Sun and draws it
    sun_radius = 50
    sun_color = "yellow"
    x = 200
    y = 200
    self.canvas.create_oval(x-sun_radius, y-sun_radius, x+sun_radius, y+sun_radius, fill=sun_color)
    self.canvas.create_text(x-sun_radius, y-sun_radius, text= "Sun", fill="white")
        
        
    # Define planet properties
    planets = [{"name": "Mercury", "radius": 25, "color": "gray", "distance": 100}, {"name": "Venus", "radius": 25, "color": "orange", "distance": 200}, {"name": "Earth", "radius": 30, "color": "blue", "distance": 300}, {"name": "Mars", "radius": 30, "color": "red", "distance": 400}, {"name": "Jupiter", "radius": 35, "color": "brown", "distance": 500}, {"name": "Saturn", "radius": 35, "color": "tan", "distance": 600}, {"name": "Uranus", "radius": 25, "color": "light blue", "distance": 700}, {"name": "Neptune", "radius": 15, "color": "dark blue", "distance": 800}, {"name": "Pluto", "radius": 15, "color": "light gray", "distance": 900}]
        
    self.planet_objects = []  # Store the planet objects
    self.planet_text = []  # Store the planet text names of each planet object
        
    # Draw the planets
    for planet in planets:
      radius = planet["radius"]
      color = planet["color"]
      distance = planet["distance"]
            
      x = 200 + distance
      y = 200
            
      planet_obj = self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color)
      text_obj = self.canvas.create_text(x, y+radius+10, text=planet["name"], fill="white")
      self.canvas.create_text(x, y+radius+10, text=planet["name"], fill="white")
            
      self.planet_objects.append(planet_obj)
      self.planet_text.append(text_obj)
        
    self.animate_planets()  # Start the animation
        
    
    tkinter.mainloop()
        
  def animate_planets(self):
    for _ in range(685):  # Performing a complete rotation for the tkinter to fit my tkinter window descriptions
      for planet_obj, text_obj in zip(self.planet_objects, self.planet_text):
        self.move_planet(planet_obj, text_obj)
        self.canvas.update()  # Update the canvas after each planet movement
        self.canvas.after(15)  # Takes 15 milliseconds for the rotation

  
  def move_planet(self, planet_obj, text_obj):
    self.canvas.move(planet_obj, 2, 0)  # Move the planet object horizontally by 2 pixels
    self.canvas.move(text_obj, 2, 0)  # Move the planet text object along with the planet
        
        
    # Wrap around the canvas if the planet goes beyond the right edge
    if self.canvas.coords(planet_obj)[2] > self.canvas.winfo_width():
      self.canvas.move(planet_obj, -self.canvas.winfo_width()-2, 0)


if __name__ == "__main__":
    solar_system = Solar()
