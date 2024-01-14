#zarady,muiz,chong
from robolink import *  # RoboDK's API
from robodk import *    # Math toolbox for robots
import csv              # to import excel file

# Opening Excel Files
file = open(r"C:\Users\USER\OneDrive - International Islamic University Malaysia\Desktop\BMCT\Robodk\Project\HIT.csv") 
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
    
# Converting the values into floats
rows = [list(map(float, sublist)) for sublist in rows]
print(rows) # for verification of the float type  

# Start the RoboDK API
RDK = Robolink()

# Get the robot 
robot = RDK.Item('Select a Robot', ITEM_TYPE_ROBOT)
#print(RDK.ItemList())

if robot.Valid():
    print("Invalid targets. Exiting...")
    quit()

# Get the refference target by name :
target = RDK.Item('Write')
home = RDK.Item('Home')
target_pose = target.Pose()
xyz_ref = [target_pose.Pos()]
print(xyz_ref) # For verification of float types

robot.MoveJ(home)
robot.MoveJ(target)

print("Number of rows:", len(rows))

    
# Start engraving 
for i in range(500):
    # Calculate the new position
    x = xyz_ref[0][0] 
    y = xyz_ref[0][1]- (rows[i][0]/1.5) 
    z = xyz_ref[0][2]- (rows[i][1]/1.5)
    target_pose.setPos([x,y,z])
    robot.MoveJ(target_pose) 

    
# Trigger a program call at the end of the moment
robot.RunInstruction('Program_Done')
print("Done Execute...")



