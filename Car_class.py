"""
Creating a Car class that can be used to instantiate various vehicles.
It takes in arguments that depict the type, model, and name of the vehicle, provided they are set.
"""

class Car(object):

  def __init__(self, name='General', model='GM', vehicle_type=None):   
    self.name = name
    self.model = model
    self.vehicle_type = vehicle_type
    self.speed = 0

    if self.name == 'Porshe' or self.name == 'Koenigsegg':
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4

    if self.vehicle_type == 'trailer':
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4


  def is_saloon(self):
    if self.vehicle_type != 'trailer':
        self.vehicle_type == 'saloon'
        return True
    return False

  def drive(self, moving_speed):
    if self.name == 'Mercedes' and moving_speed == 3:
      self.speed = 1000
    elif moving_speed == 7:
      self.speed = 77

    return self
        
   

    
