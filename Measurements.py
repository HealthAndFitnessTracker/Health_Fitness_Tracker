# Work: Noah Hoepfinger
class Measurements():
    def __init__(self, Weight:int, Chest:int, Chest_height:int, Left_arm:int, Left_arm_height:int, Right_arm:int, Right_arm_height:int, Stomach:int, Stomach_height:int, Hips:int, Hips_height:int, Left_thigh:int, Left_thigh_height:int, Right_thigh:int, Right_thigh_height:int):
        self.weight = Weight
        self.chest = Chest
        self.chest_height = Chest_height
        self.left_arm = Left_arm
        self.left_arm_height = Left_arm_height
        self.right_arm = Right_arm
        self.right_arm_height = Right_arm_height
        self.stomach = Stomach
        self.stomach_height = Stomach_height
        self.hips = Hips
        self.hips_height = Hips_height
        self.left_thigh = Left_thigh
        self.left_thigh_height = Left_thigh_height
        self.right_thigh = Right_thigh
        self.right_thigh_height = Right_thigh_height


# The value of this def is two fold. Its for initially finding what parts you want to change, and then taking a new value and inputing it. 
    def AddMeasurement(self, value, weightvalue, heightvalue):
        if value == 0:
            self.weight = weightvalue
        if value == 1:
            self.chest = weightvalue
            self.chest_height = heightvalue
        if value == 2:
            self.left_arm = weightvalue
            self.left_arm_height = heightvalue
        if value == 3:
            self.right_arm = weightvalue
            self.right_arm_height = heightvalue
        if value == 4:
            self.stomach = weightvalue
            self.stomach_height = heightvalue
        if value == 5:
            self.hips = weightvalue
            self.hips_height = heightvalue
        if value == 6:
            self.left_thigh = weightvalue
            self.left_thigh_height = heightvalue
        if value == 7:
            self.right_thigh = weightvalue
            self.right_thigh_height = heightvalue
        
#  This function sets the measurements to zero.
    def DeleteMeasurement(self, value):
        if value == 0:
            self.weight(0)
        if value == 1:
            self.chest = 0
            self.chest_height = 0
        if value == 2:
            self.left_arm = 0
            self.left_arm_height = 0
        if value == 3:
            self.right_arm = 0
            self.right_arm_height = 0
        if value == 4:
            self.stomach = 0
            self.stomach_height = 0
        if value == 5:
            self.hips = 0
            self.hips_height = 0
        if value == 6:
            self.left_thigh = 0
            self.left_thigh_height = 0
        if value == 7:
            self.right_thigh = 0
            self.right_thigh_height = 0


test = Measurements(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
test.AddMeasurement(0)
test.DeleteMeasurement(2)
print(test.weight)
print(test.left_arm_height)
print(test)

