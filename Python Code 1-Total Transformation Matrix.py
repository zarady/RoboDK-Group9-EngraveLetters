import sympy as sp

# Define symbolic joint variables
q1, q2, q3, q4, q5, q6 = sp.symbols('q1 q2 q3 q4 q5 q6', real=True)

# Define DH parameters for 6-DOF robot (modify these based on your robot)
a = [0, 390, 0, 0, 0, 0]                # Link lengths
alpha = [3*sp.pi/2, 0, 0, sp.pi/2, 0, 0]  # Link twists
d = [400, 0, 263, 107, 85, 283]        # Link offsets
theta = [q1, q2, q3, q4, q5, q6]       # Joint angles

# Initialize the transformation matrix
T = sp.eye(4)

# Compute the transformation matrix using DH parameters
for i in range(6):
    # Define the transformation matrix for the current joint
    A = sp.Matrix([[sp.cos(theta[i]), -sp.sin(theta[i])*sp.cos(alpha[i]), sp.sin(theta[i])*sp.sin(alpha[i]), a[i]*sp.cos(theta[i])],
                   [sp.sin(theta[i]), sp.cos(theta[i])*sp.cos(alpha[i]), -sp.cos(theta[i])*sp.sin(alpha[i]), a[i]*sp.sin(theta[i])],
                   [0, sp.sin(alpha[i]), sp.cos(alpha[i]), d[i]],
                   [0, 0, 0, 1]])

    # Display the transformation matrix A for the current joint with 4 significant figures
    print(f'Transformation Matrix A{i + 1}:')
    sp.pprint(A.evalf(), use_unicode=True)

    # Update the overall transformation matrix
    T = T * A

# Display the total transformation matrix with 4 significant figures
print('Total Transformation Matrix:')
sp.pprint(T.evalf(), use_unicode=True)
