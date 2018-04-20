# Vertical Motion

# t = 0.6 s, v_0 = 5 m/s, g = 9.81 m/s^2
print(5 * 0.6 - 0.5 * 9.81 * 0.6**2)

# t = 0.1 s, v_0 = 1 m/s, g = 9.81 m/s^2
print(1 * 0.1 - 0.5 * 9.81 * 0.1**2)

# Using variables
v0 = 5
g = 9.81
t = 0.6
y = v0 * t - 0.5 * g * t**2

print(y)

# Names of variables
initial_velocity = 5
acceleration_of_gravity = 9.81
TIME = 0.6
vertical_position_of_ball = initial_velocity * \
    TIME - 0.5 * acceleration_of_gravity * TIME**2

print(vertical_position_of_ball)
