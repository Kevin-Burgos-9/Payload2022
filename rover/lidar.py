class Lidar:
    def __init__(self):
        pass

    def check_clearance(self):
        """Use the front and back lidar sensors to check if there are any objects within 10 inches"""
        front_clear = self.front_lidar.check_clearance(10)
        back_clear = self.back_lidar.check_clearance(10)
        if front_clear and back_clear:
            print("Rover has clearances in front and back.")
        elif front_clear:
            print("Rover has clearance in front only.")
        elif back_clear:
            print("Rover has clearance in back only.")
        else:
            print("Rover has no clearances in front or back.")
