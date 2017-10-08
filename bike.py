# Defining Bike
class Bike(object):
   
    # Initializiation & what it has
   
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
   
    # Actions    
    
    def displayInfo(self):
        print "The price is: " + str(self.price)
        print "Your max speed is: " + str(self.max_speed) + 'MPH'
        print "Total miles put in: " + str(self.miles) + 'miles'
    
    def ride(self):
        print "Riding"
        self.miles += 10

    def reverse(self):
        print "Going in reverse"
        self.miles -= 5

bike1 = Bike(99.99, 12)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(139.99, 20)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()