import matplotlib.pyplot as plt
import math


VOriginal = 80 # m/s __initial speed
V = VOriginal

Degree = 65  # degree __initial angle in degree
Angle = math.pi * (Degree / 180)  # Rad __initial angle to RAD

AirDensity = 1.18  # kg/m^3
Cd = 0.5  # ball type Cd
S = 0.0095  # m^2 __section of ball in m^2
m = 0.460  # Kg __Mass of ball

# F_air = Cd * AirDensity * S * V**2 / 2
t_pace = 0.01  # s __in 1/100 seconds slice
# DeltaV = F_air * t_pace / m  # __use later

Vx = V * math.cos(Angle)  # m/s
Vy = V * math.sin(Angle)  # m/s

Vector = [0, Vx, Vy]
Dots = [[0, 0.0, 0.0], ]

VVacuum = V  # for reference
AngleVacuum = Angle  # for Reference
VectorVacuum = [0, Vx, Vy]
DotsVacuum = [[0, 0.0, 0.0], ]

g = 9.81  # m/s^2

for t in range(0, 1000):
    Vector[2] -= g * t_pace
    V = math.sqrt(Vector[1] ** 2 + Vector[2] ** 2)
    Angle = math.atan(Vector[2]/Vector[1])

    F_air = Cd * AirDensity * S * (V ** 2) / 2

    DeltaV = F_air * t_pace / m
    V = V - DeltaV
    Vector[1] = V * math.cos(Angle)  # m/s
    Vector[2] = V * math.sin(Angle)  # m/s
    DotAddX = Dots[t][1] + Vector[1]*t_pace
    DotAddY = Dots[t][2] + Vector[2]*t_pace
    Dots.append([t, DotAddX, DotAddY])

    Plot_Real = plt.scatter(DotAddX, DotAddY, s=1, marker='.', color='b')
    Plot_Speed = plt.scatter(DotAddX, V, s=1, marker='.', color='g')
    Plot_SpeedX = plt.scatter(DotAddX, Vector[1], s=1, marker='.', color='olive')

    # vacuum---------------------------------------------------------------------------------

    VectorVacuum[2] -= g * t_pace
    VVacuum = math.sqrt(VectorVacuum[1] ** 2 + VectorVacuum[2] ** 2)
    AngleVacuum = math.atan(VectorVacuum[2]/VectorVacuum[1])

    #  F_air = Cd * AirDensity * S * V ** 2 / 2

    #  DeltaV = F_air * t_pace / m
    #  V -= DeltaV
    VectorVacuum[1] = VVacuum * math.cos(AngleVacuum)  # m/s
    VectorVacuum[2] = VVacuum * math.sin(AngleVacuum)  # m/s
    DotAddXVacuum = DotsVacuum[t][1] + VectorVacuum[1] * t_pace
    DotAddYVacuum = DotsVacuum[t][2] + VectorVacuum[2] * t_pace
    DotsVacuum.append([t, DotAddXVacuum, DotAddYVacuum])

    Plot_Ref = plt.scatter(DotAddXVacuum, DotAddYVacuum, s=1, marker='.', color='r')

#   plt.plot(DotAddXVacuum[t][1],DotAddXVacuum[t][2], linewidth=2, color='g', linestyle='--', )


Title = ''.join(['V=', str(VOriginal), 'm/s, Angle= ', str(Degree), '/180*PI, m=', str(m), 'kg,\n Air Density=', str(AirDensity), '$kg/m^3$, Cd=', str(Cd)])
plt.title(Title)
plt.grid()
plt.xlim(0, 300)
plt.ylim(0, 160)
plt.xlabel('Meter')
plt.ylabel('Meter')
plt.legend([Plot_Real, Plot_Ref, Plot_Speed, Plot_SpeedX], ('Real', 'Reference', 'Scalar Speed', 'X-Axis Speed'), numpoints =1)
ax = plt.gca()
ax.yaxis.set_minor_locator(plt.MultipleLocator(10))
ax.set_aspect(1)
# plt.scatter(Dots[:, 1], Dots[:, 2], marker='.')
plt.show()

# plt.scatter(Dots, s=5, marker='.')  # s表示面积，marker表示图形

# plt.show()
