import numpy as np
import matplotlib.pyplot as plt
import quaternion as qt

def skew(w):
    w1, w2, w3 = w
    skew = np.array([
        [0,-w3,w2],
        [w3,0,-w1],
        [-w2,w1,0]
    ])
    return skew
def skew_4x4(w):
    w1, w2, w3 = w
    skew = np.array([
        [0,w3,-w2,w1],
        [-w3,0,w1,w2],
        [w2,-w1,0,w3],
        [-w1,-w2,-w3,0]
    ])
    return skew
def s(angle):
    sin = np.sin(angle)
    return sin
def c(angle):
    cos = np.cos(angle)
    return cos
def rot313(angles):
    y, p ,r = angles
    C = np.array([
        [c(y)*c(r)-s(y)*s(r)*c(p),c(y)*s(r)+s(y)*c(p)*c(r),s(y)*s(p)],
        [-s(y)*c(r)-c(y)*s(r)*c(p),-s(y)*s(r)+c(y)*c(p)*c(r),c(y)*s(p)],
        [s(p)*s(r),-s(p)*c(r),c(p)]
    ])
    return C
### RK4 Sistema de ecuaciones ###
def rk4_vec(f, tspan, y0, h):
    N = int(tspan / h)
    y = np.zeros((N+1, len(y0)))
    t_values = np.linspace(0, tspan, N+1)
    y[0] = y0          
    w = y0            
    for i in range(1, N+1):
        t = t_values[i-1]
        k1 = h * f(t, w)
        k2 = h * f(t + h/2, w + k1/2)
        k3 = h * f(t + h/2, w + k2/2)
        k4 = h * f(t + h, w + k3)
        w = w + (k1 + 2*k2 + 2*k3 + k4)/6
        y[i] = w   
    return t_values, y
def dwdt(t,w,wr,dwrdt,J,Jr):
    dwdt = -np.linalg.inv(J+Jr)@(skew(w)@J@w+Jr@(dwrdt+skew(w)@wr)+skew(w+wr)@Jr@(w+wr))
    return dwdt
def dwrdt(t,wr,Jr,Mr):
    dwrdt = np.linalg.inv(Jr)@(Mr-skew(wr)@Jr@wr)
    return dwrdt
def dqdt(t,w,q):
    dqdt = 0.5*skew_4x4(w)@q
    return dqdt
def sistem(t,y):
    w = y[0:3]
    wr = y[3:6]
    q = y[6:10]
    Mr_val = Mr(t)
    dwr_dt = dwrdt(t,wr,Jr,Mr_val)
    dw_dt = dwdt(t,w,wr,dwr_dt,J,Jr)
    dq_dt = dqdt(t,w,q)
    return np.concatenate((dw_dt, dwr_dt,dq_dt))

### Datos del Problema y Condiciones iniciales
J_xx = 4000
J_yy = 7500
J_zz = 8500
J = np.array([
    [J_xx,0,0],
    [0,J_yy,0],
    [0,0,J_zz]
])
Jr = np.array([
    [50,-10,0],
    [-10,100,15],
    [0,15,250]
])
#Condiciones iniciales
w0 = np.array([0,0,0])
#w0 = np.array([0.1,-0.2,0.5]) 
wr0 = np.array([0,0,0])
y0 = np.array([0,0.5*np.pi,0]) # yaw, pitch, roll 
q0 = qt.quaternion(rot313(y0))
ivs = np.concatenate((w0,wr0,q0))
def Mr(t):
    if t >= 0 and t < 5:
        Mr = np.array([7,-10,-200])
    elif t >= 5 and t < 10:
        Mr = np.array([-7,10,0])
    else:
        Mr = np.array([0,0,0])
    return Mr
t, sol = rk4_vec(sistem,400,ivs,0.01)
sol_angle = sol[:,:6]
sol_deg = np.rad2deg(sol_angle)
sol_q = sol[:,6:10]
H_sol = np.zeros((len(t), 3))
for i in range(len(t)):
    w = sol[i,0:3]    # velocidad nave
    wr = sol[i,3:6]   # velocidad rotor
    H = J @ w + Jr @ (wr+w)
    H_sol[i] = H

# Grafica velocidad nave
plt.figure()
plt.plot(t, sol_deg[:,0], label='w_x')
plt.plot(t, sol_deg[:,1], label='w_y')
plt.plot(t, sol_deg[:,2], label='w_z')
plt.legend()
plt.xlabel("Tiempo [s]")
plt.ylabel("Velocidades angulares [°/s]")
plt.grid()
# Grafica velocidad rotor
plt.figure()
plt.plot(t, sol_deg[:,3], label='w_rx')
plt.plot(t, sol_deg[:,4], label='w_ry')
plt.plot(t, sol_deg[:,5], label='w_rz')
plt.legend()
plt.xlabel("Tiempo [s]")
plt.ylabel("Velocidades angulares [°/s]")
plt.grid()
# Grafica actitud
plt.figure()
plt.plot(t, sol_q[:,0], label='q1')
plt.plot(t, sol_q[:,1], label='q2')
plt.plot(t, sol_q[:,2], label='q3')
plt.plot(t, sol_q[:,3], linestyle='--', label='q4')
plt.legend()
plt.xlabel("Tiempo [s]")
plt.ylabel("quaternion")
plt.grid()
# Grafico momento angular
plt.figure()
plt.plot(t, H_sol[:,0], label='H_x')
plt.plot(t, H_sol[:,1], label='H_y')
plt.plot(t, H_sol[:,2], label='H_z')
plt.xlabel("Tiempo [s]")
plt.ylabel("Momento angular [kg·m²/s]")
plt.title("Momento angular de la nave")
plt.legend()
plt.grid()
plt.show()
