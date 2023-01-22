import numpy as np 
import trigonometric as tr
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

mm2m = 1/1000


def dh_parse(j1, j2, j3, j4, j5, j6, type=None):
    if type == None:
        a1 = 150 * mm2m
        a2 = 700 * mm2m
        a3 = 0 * mm2m
        d1 = 486.5 * mm2m
        d4 = 600 * mm2m
        d6 = 65 * mm2m
    else: pass 

    j = np.array([[j1, j2-90, j3+90+90, j4, j5, j6],  # joints
            [d1, 0, 0, d4, 0, d6],          # d
            [a1, a2, a3, 0, 0, 0],          # a    
            [-90, 0, 90, -90, 90, 0]])      # alpha

    return j

def kinematics(j):
    """This function is in charge to compute the forward kinematics.
    Args:
        j (np.array): 1 = q, 2=d, 3=a, 4=alpha

    Returns:
        np.hstack: return the transformation matrixes
    """
    T01 = mA(j[0, 0], j[1, 0], j[2, 0], j[3, 0])
    T12 = mA(j[0, 1], j[1, 1], j[2, 1], j[3, 1])
    T23 = mA(j[0, 2], j[1, 2], j[2, 2], j[3, 2])
    T34 = mA(j[0, 3], j[1, 3], j[2, 3], j[3, 3])
    T45 = mA(j[0, 4], j[1, 4], j[2, 4], j[3, 4])
    T56 = mA(j[0, 5], j[1, 5], j[2, 5], j[3, 5])

    T02 = T01@T12
    T03 = T02@T23
    T04 = T03@T34
    T05 = T04@T45
    T06 = T05@T56

    m = np.hstack((T01, T02, T03, T04, T05, T06))

    return m



def mA(th, d, a, al):
    A1 = rotz(th)
    A2 = traz(d)
    A3 = trax(a)
    A4 = rotx(al)
    A5 = A1@A2@A3@A4
    return np.array(A5)

def rotz(th):
    rz = np.array([[tr.cosd(th), -tr.sind(th), 0, 0],
        [tr.sind(th), tr.cosd(th), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]])
    return rz

def traz(z):
    ry = np.array([[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, z],
    [0, 0, 0, 1]])
    return ry

def rotx(al):
    rx = np.array([[1, 0, 0, 0],
    [0, tr.cosd(al), -tr.sind(al), 0],
    [0, tr.sind(al), tr.cosd(al), 0],
    [0, 0, 0, 1]])
    return rx

def trax(x):
    tx = np.array([[1, 0, 0, x],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]])    
    return tx


# def xyz_pos(m):
#     Q1 = np.array([0, m[0, 0], m[0, 3], m[0, 7], m[0, 11], m[0, 15], m[0, 19], m[0, 23]])
#     Q2 = np.array([0, m[1, 0], m[1, 3], m[1, 7], m[1, 11], m[1, 15], m[1, 19], m[1, 23]])
#     Q3 = np.array([0, m[2, 0], m[2, 3], m[2, 7], m[2, 11], m[2, 15], m[2, 19], m[2, 23]])
#     Q = np.vstack((Q1, Q2, Q3))

#     return  Q

def xyz_pos(m):

    Q1 = np.array([0, 0, m[0, 3], m[0, 7], m[0, 11], m[0, 15], m[0, 19], m[0, 23] ])
    Q2 = np.array([0, 0, m[1, 3], m[1, 7], m[1, 11], m[1, 15], m[1, 19], m[1, 23]])
    Q3 = np.array([0, m[2, 3], m[2, 3], m[2, 7], m[2, 11], m[2, 15], m[2, 19], m[2, 23]])
    
    P = np.vstack((Q1, Q2, Q3))

    Ux = np.array([m[0, 23], m[0, 23]+m[0, 20]*.4])
    Uy = np.array([m[1, 23], m[1, 23]+m[1, 20]*.4])
    Uz = np.array([m[2, 23], m[2, 23]+m[2, 20]*.4])

    Vx = np.array([m[0, 23], m[0, 23]+m[0, 21]*.4])
    Vy = np.array([m[1, 23], m[1, 23]+m[1, 21]*.4])
    Vz = np.array([m[2, 23], m[2, 23]+m[2, 21]*.4])

    Wx = np.array([m[0, 23], m[0, 23]+m[0, 22]*.4])
    Wy = np.array([m[1, 23], m[1, 23]+m[1, 22]*.4])
    Wz = np.array([m[2, 23], m[2, 23]+m[2, 22]*.4])

    U = np.vstack((Ux, Uy, Uz))
    V = np.vstack((Vx, Vy, Vz))
    W = np.vstack((Wx, Wy, Wz))

    return  P, U, V, W

def draw_robot(Q,U,V,W):
    X, Y, Z = Q[0, :], Q[1, :], Q[2, :]
    X0,Y0,Z0= Q[0,0:3],Q[1,0:3],Q[2,0:3]
    X1,Y1,Z1= Q[0,1:4],Q[1,1:4],Q[2,1:4]
    X2,Y2,Z2= Q[0,2:4],Q[1,2:4],Q[2,2:4]
    X3,Y3,Z3= Q[0,3:5],Q[1,3:5],Q[2,3:5]
    X4,Y4,Z4= Q[0,4:6],Q[1,4:6],Q[2,4:6]
    X5,Y5,Z5= Q[0,5:6],Q[1,5:6],Q[2,5:6]
    X6,Y6,Z6= Q[0,6:6],Q[1,6:6],Q[2,6:6]

    fig = plt.figure(num=None, figsize=(14, 20), dpi=80, edgecolor='k')
    ax = fig.add_subplot(111, projection='3d')
    
    ax.plot(U[0, : ], U[1,: ], U[2, : ], linewidth=5)
    ax.plot(V[0, : ], V[1,: ], V[2, : ], linewidth=5)
    ax.plot(W[0, : ], W[1,: ], W[2, : ], linewidth=5)
    ax.plot(X0,Y0,Z0, color='red', marker='o', linestyle='solid', linewidth=5, markersize=10)
    ax.plot(X1,Y1,Z1, color='green', marker='o', linestyle='solid', linewidth=5, markersize=10)
    ax.plot(X2,Y2,Z2, color='red', marker='o', linestyle='solid', linewidth=5, markersize=10)
    ax.plot(X3,Y3,Z3, color='blue', marker='o', linestyle='solid', linewidth=5, markersize=10)
    ax.plot(X4,Y4,Z4, color='black', marker='o', linestyle='solid', linewidth=5, markersize=10)
    ax.plot(X5,Y5,Z5, color='green', marker='o', linestyle='solid', linewidth=5, markersize=10)
    ax.plot(X6,Y6,Z6, color='red', marker='o', linestyle='solid', linewidth=5, markersize=10)
    ax.set_xlabel('X[m]')
    ax.set_ylabel('Y[m]')
    ax.set_zlabel('Z[m]')
    ax.set_xlim([-4, 4])
    ax.set_ylim([-4, 4])
    ax.set_zlim([0, 2])
    ax.set_title('Forward Kinematics')
    ax.view_init(20, -120)
    plt.show()
    return X1,Y1,Z1,X2,Y2,Z2,X2,Y2,Z2

