import numpy as np
import math
mass = 300 #kg #300 * 9.8 gives normal force
g = 9.81
tire_rad = 0.254 #m
drive_ratio = 4.0
#aerodynamics
cd = 0.8 
downforce_coefficient = 0
frontal_area = 1 #m/s^2
#drivetrain
drive_train = 0.9 # percentwise 90%
co_friction = 1 #max force applied by tire found by: F = mu*R, with mu=co_friction and R=normal force of cara aka mass*9.81
position = np.arange(50,550)
max_tire_F = co_friction * mass * g
#total force is sqrt(centriputalF^2 + dragF^2)**0.5 = mu * R
curve_rad = 50
max_v_on_curve = (curve_rad * co_friction * g)**0.5
arc_len = 50 * (180* (math.pi/180))
curve_time = arc_len / max_v_on_curve
arr = np.arange(0, 501, 50)
"""def speed_at_sectors():
    i = 1
    speeds = [0] 
    while i < len(arr):
        prev = arr[i-1]
        curr = arr[i]
        v_curr = (prev)
        speeds.append(v_curr)
        u = v_curr
        i += 1
    return np.array(speeds)
velocities = speed_at_sectors()
print(velocities)"""