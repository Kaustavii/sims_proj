import numpy as np
mass = 300 #kg #300 * 9.8 gives normal force
g = 9.81
tire_rad = 0.254 #m
drive_ratio = 4.0
#aerodynamics
drag_coefficient = 0.8 
downforce_coefficient = 0
frontal_area = 1 #m/s^2
#drivetrain
drive_train = 0.9 # percentwise 90%
co_friction = 1 #max force applied by tire found by: F = mu*R, with mu=co_friction and R=normal force of cara aka mass*9.81
position = np.arange(50,550)
max_tire_F = co_friction * mass * g
#total force is sqrt(centriputalF^2 + dragF^2)**0.5 = mu * R

