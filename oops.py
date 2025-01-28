# class Car:
#     def __init__(self, brand, color):
#         self.color = color
#         self.brand = brand

#     def drive(self):
#         # Use f-string for proper variable interpolation
#         print(f"{self.brand} {self.color} is driving!")

# # Create objects
# car1 = Car("Toyota", "red")
# car2 = Car("Suzuki", "white")

# # Call methods
# car1.drive()  # Output: Toyota red is driving!
# car2.drive()  # Output: Suzuki white is driving!









class car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def drive(self):
            print(f"{self.name} {self.color}")
    
car1=car("toyota","white")
car2=car("suzuki","black")
car1.drive()
car2.drive()
    
