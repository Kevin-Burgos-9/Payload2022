

class servo:
    def __init__ (self):
        pass
    
    def deploy_arms(self):
        """Use the servos to deploy the arms"""
        if not self.arms_deployed:
            self.servos.deploy()
            self.arms_deployed = True
        else:
            print("Arms are already deployed!")

    def self_level(self):
        """Use the mpu to check if the rover is level"""
        # Check the current pitch and roll angles
        pitch, roll = self.mpu.get_angles()
        print(f"Current pitch: {pitch} degrees")
        print(f"Current roll: {roll} degrees")

        # Check if the rover is already leveled
        if abs(pitch) < 5 and abs(roll) < 5:
            print("Rover is already leveled.")
            self.leveled = True
            return

        # Calculate the required pitch and roll angles to level the rover
        target_pitch = -pitch
        target_roll = -roll
        print(f"Target pitch: {target_pitch} degrees")
        print(f"Target roll: {target_roll} degrees")

        # Use the servos to adjust the pitch and roll until the rover is leveled
        while abs(pitch - target_pitch) > 5 or abs(roll - target_roll) > 5:
            self.servos.adjust_pitch(pitch, target_pitch)
            self.servos.adjust_roll(roll, target_roll)
            pitch, roll = self.mpu.get_angles()
            print(f"Current pitch: {pitch} degrees")
            print(f"Current roll: {roll} degrees")
            time.sleep(0.5)

        print("Rover is leveled.")
        self.level