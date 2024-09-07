
import matplotlib.pyplot as plt
import numpy as np

# Variables iniciales
x0 = 5
y0 = 5

# Vectores unitarios en forma escalar
uf = 1  # velocidad frontal
ul = -1  # velocidad lateral
phy = 0.1  # velocidad angular
dt = 0.01  # paso de integración
t = np.arange(0, 10, dt)  # vector de tiempo

# Inicializar vectores para almacenar los resultados
xc_dot_v = np.zeros_like(t)
yc_dot_v = np.zeros_like(t)
w_dot_v = np.zeros_like(t)
xc_v = np.zeros_like(t)
yc_v = np.zeros_like(t)
w_v = np.zeros_like(t)

def CalculateVelocity(uf, ul, phy):
    xc_dot = uf * np.cos(phy) - ul * np.sin(phy)
    yc_dot = uf * np.sin(phy) + ul * np.cos(phy)
    omega = phy
    return xc_dot, yc_dot, omega

def CalculatePosition(xcA, ycA, phyA, xc_dot, yc_dot, omega):
    # Se integra para determinar la posición
    xc = xcA + xc_dot * dt
    yc = ycA + yc_dot * dt
    phy = phyA + omega * dt
    return xc, yc, phy

def Bucle():
    # Inicializar las posiciones y la orientación inicial
    xc_v[0] = x0
    yc_v[0] = y0
    w_v[0] = phy

    for i in range(1, len(t)):
        xc_dot_v[i], yc_dot_v[i], w_dot_v[i] = CalculateVelocity(uf, ul, w_v[i-1])
        xc_v[i], yc_v[i], w_v[i] = CalculatePosition(xc_v[i-1], yc_v[i-1], w_v[i-1], xc_dot_v[i], yc_dot_v[i], w_dot_v[i])

    # Graficar los resultados
    plt.figure(figsize=(12, 12))

    plt.subplot(2, 2, 1)
    plt.plot(t, xc_v, label='Posición X')
    plt.xlabel('Tiempo')
    plt.ylabel('Posición')
    plt.title('Posiciones en el tiempo')
    plt.legend()
    plt.grid()

    plt.subplot(2, 2, 2)
    plt.plot(t, yc_v, label='Posición Y')
    plt.xlabel('Tiempo')
    plt.ylabel('Posición')
    plt.title('Posiciones en el tiempo')
    plt.legend()
    plt.grid()

    plt.subplot(2, 2, 3)
    plt.plot(xc_v, yc_v, label='Posición X vs Y')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Posición X vs Y')
    plt.legend()
    plt.grid()

    plt.subplot(2, 2, 4)
    plt.plot(t, w_v, label='Velocidad Angular', color='orange')
    plt.xlabel('Tiempo')
    plt.ylabel('Velocidad Angular')
    plt.title('Velocidad Angular en el tiempo')
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()

Bucle()

#Inversa
#Trayectoria


dt = 0.01
TParametic = np.arange(0,2*np.pi,dt)











import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros del robot
R = 0.05   # Radio de las ruedas (metros)
L = 0.2    # Distancia desde el centro del robot a las ruedas (metros)

# Variables de movimiento (cambiar estas variables para ver cómo se mueve el robot)
u_f = 1.0  # Velocidad frontal del robot (m/s)
u_l = 1.0  # Velocidad lateral del robot (m/s)
omega = -2 # Velocidad angular del robot (rad/s)

# Cinemática inversa para obtener las velocidades angulares de las ruedas
def wheel_speeds(u_f, u_l, omega, L, R):
    w1 = (u_f - u_l + omega * L) / R
    w2 = (u_f + u_l + omega * L) / R
    w3 = (u_f - u_l - omega * L) / R
    w4 = (u_f + u_l - omega * L) / R
    return w1, w2, w3, w4

# Función de simulación para actualizar la posición del robot
def update_position(x, y, phi, u_f, u_l, omega, dt):
    x_dot = u_f * np.cos(phi) - u_l * np.sin(phi)
    y_dot = u_f * np.sin(phi) + u_l * np.cos(phi)
    phi_dot = omega
    x += x_dot * dt
    y += y_dot * dt
    phi += phi_dot * dt
    return x, y, phi

# Inicializar la posición del robot
x = 0
y = 0
phi = 0
c=0
dt = 0.1  # Paso de tiempo

# Configuración de la animación
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
robot_plot, = ax.plot([], [], 'ro')

# Función de animación
def animate(i):
    global x, y, phi, c
    c+=1
    x, y, phi = update_position(x, y, phi, u_f, u_l, omega, dt)
    robot_plot.set_data([x], [y])
    w1, w2, w3, w4 = wheel_speeds(u_f, u_l, omega, L, R)
    print(f"Velocidad angular de las ruedas (rad/s): w1={w1}, w2={w2}, w3={w3}, w4={w4} --->{c}")
    return robot_plot,


anim = FuncAnimation(fig, animate, frames=10, interval=10)
plt.show()

# Mostrar velocidades angulares de las ruedas
w1, w2, w3, w4 = wheel_speeds(u_f, u_l, omega, L, R)
print(f"Velocidad angular de las ruedas (rad/s): w1={w1}, w2={w2}, w3={w3}, w4={w4}")




import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Definición de las variables del robot
def omnidirectional_robot_simulation_with_animation(time_step, total_time, omega, initial_state, ul, uf):
    # Variables de tiempo
    t = np.arange(0, total_time, time_step)

    # Estados iniciales
    xr, yr, phy = initial_state

    # Listas para almacenar la trayectoria
    trajectory_x = []
    trajectory_y = []
    orientations = []

    for _ in t:
        # Ecuaciones del robot
        xr_dot = uf * np.cos(phy) - ul * np.sin(phy)
        yr_dot = uf * np.sin(phy) + ul * np.cos(phy)

        # Actualización de la posición del robot
        xr += xr_dot * time_step
        yr += yr_dot * time_step
        phy += omega * time_step

        # Guardar la posición y orientación
        trajectory_x.append(xr)
        trajectory_y.append(yr)
        orientations.append(phy)

    # Hacer la trayectoria cerrada
    trajectory_x.append(trajectory_x[0])
    trajectory_y.append(trajectory_y[0])
    orientations.append(orientations[0])

    # Función para actualizar la animación
    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')

    # El robot es un cuadrado representado por 4 puntos
    robot, = ax.plot([], [], 'b-')
    # Línea para la estela de la trayectoria
    trail, = ax.plot([], [], 'r-', lw=1)

    # Función para obtener los vértices del cuadrado dado el centro y el ángulo
    def get_square(x, y, angle, size=1):
        # Define los vértices del cuadrado en el sistema local
        local_square = np.array([[-size, -size], [size, -size], [size, size], [-size, size], [-size, -size]])

        # Matriz de rotación
        rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                    [np.sin(angle), np.cos(angle)]])

        # Rotar y trasladar los puntos
        rotated_square = local_square @ rotation_matrix.T + [x, y]
        return rotated_square[:, 0], rotated_square[:, 1]

    def update(frame):
        # Actualiza la posición del cuadrado
        x = trajectory_x[frame]
        y = trajectory_y[frame]
        angle = orientations[frame]

        # Obtener los vértices del cuadrado en la nueva posición y orientación
        square_x, square_y = get_square(x, y, angle, size=0.5)

        # Actualiza el gráfico del robot
        robot.set_data(square_x, square_y)

        # Actualiza la estela de la trayectoria
        trail.set_data(trajectory_x[:frame + 1], trajectory_y[:frame + 1])

        return robot, trail

    # Crear la animación
    anim = FuncAnimation(fig, update, frames=len(t), interval=100, blit=True)
    plt.show()


# Parámetros de la simulación
time_step = 0.1  # Paso de tiempo
total_time = 10  # Tiempo total de simulación
omega = 0.5  # Velocidad angular
initial_state = [0, 0, 0]  # Estado inicial (xr, yr, phy)
ul = 1  # Vector lateral
uf = 1  # Vector frontal

# Ejecutar la simulación con animación
omnidirectional_robot_simulation_with_animation(time_step, total_time, omega, initial_state, ul, uf)
