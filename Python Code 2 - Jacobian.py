from sympy import symbols, cos, sin, zeros, eye, Matrix
import sympy as sp
# Define symbolic joint variables
q1, q2, q3, q4, q5, q6 = symbols('q1 q2 q3 q4 q5 q6', real=True)

# Define DH parameters for 6-DOF robot (modify these based on your robot)
a = [0, 390, 0, 0, 0, 0]                # Link lengths
alpha = [3*sp.pi/2, 0, 0, sp.pi/2, 0, 0]  # Link twists
d = [400, 0, 263, 107, 85, 283]        # Link offsets
theta = [0, 0, 0, 0, 0, 0]      # Joint angles

# Initialize the transformation matrix
T = eye(4)

# Initialize list to store transformation matrices A1, A2, A3, A4, A5, A6
A_list = []

# Compute the transformation matrix using DH parameters
for i in range(6):
    # Define the transformation matrix for the current joint
    A = Matrix([[cos(theta[i]), -sin(theta[i])*cos(alpha[i]), sin(theta[i])*sin(alpha[i]), a[i]*cos(theta[i])],
                [sin(theta[i]), cos(theta[i])*cos(alpha[i]), -cos(theta[i])*sin(alpha[i]), a[i]*sin(theta[i])],
                [0, sin(alpha[i]), cos(alpha[i]), d[i]],
                [0, 0, 0, 1]])

    # Store the transformation matrix in the list
    A_list.append(A)

    # Display the transformation matrix A for the current joint with 4 significant figures
    print(f'Transformation Matrix A{i+1}:')
    print(A.evalf(4))

    # Update the overall transformation matrix
    T = T * A

# Display the total transformation matrix with 4 significant figures
print('Total Transformation Matrix:')
print(T.evalf(4))

# Access individual transformation matrices A1, A2, A3, A4, A5, A6 from the list
A1, A2, A3, A4, A5, A6 = A_list

# Calculate matrices G, H, I, J, K, and L based on the product of A1, A2, A3, A4, A5, A6
G = (A1 * A2 * A3 * A4 * A5 * A6)
H = (A2 * A3 * A4 * A5 * A6)
I = (A3 * A4 * A5 * A6)
J = (A4 * A5 * A6)
K = (A5 * A6)
L = (A6)

# Display matrices G, H, I, J, K, and L with 4 significant figures
print('Matrix G:')
print(G.evalf(4))
print('Matrix H:')
print(H.evalf(4))
print('Matrix I:')
print(I.evalf(4))
print('Matrix J:')
print(J.evalf(4))
print('Matrix K:')
print(K.evalf(4))
print('Matrix L:')
print(L.evalf(4))

# Calculate matrix Z based on the specified formulas
Z = zeros(6, 6)

for j in range(6):
    # Select the matrix based on the current column
    current_matrix = G if j == 0 else H if j == 1 else I if j == 2 else J if j == 3 else K if j == 4 else L
    
    for i in range(6):
        # Elements from the current matrix
        nx, ny, nz = current_matrix[0, 0], current_matrix[1, 0], current_matrix[2, 0]
        ox, oy, oz = current_matrix[0, 1], current_matrix[1, 1], current_matrix[2, 1]
        ax, ay, az = current_matrix[0, 2], current_matrix[1, 2], current_matrix[2, 2]
        px, py, pz = current_matrix[0, 3], current_matrix[1, 3], current_matrix[2, 3]

        # Assign values to Z based on the specified formulas
        if i == 0:
            Z[i, j] = (-nx*py) + (ny*px)
        elif i == 1:
            Z[i, j] = (-ox*py) + (oy*px)
        elif i == 2:
            Z[i, j] = (-ax*py) + (ay*px)
        elif i == 3:
            Z[i, j] = nz
        elif i == 4:
            Z[i, j] = oz
        elif i == 5:
            Z[i, j] = az

# Display matrix Z with 4 significant figures
print('Matrix JACOBIAN=:')
print(Z.evalf(4))
