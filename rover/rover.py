import TB6612FNG
import adafruit_mpu6050
import RadioHead

class Rover:
    def __init__(self, front_lidar, back_lidar, camera, servos):
        self.driver = TB6612FNG.Driver()
        self.front_lidar = front_lidar
        self.back_lidar = back_lidar
        self.mpu = adafruit_mpu6050.MPU6050()
        self.camera = camera
        self.servos = servos
        self.arms_deployed = False
        self.leveled = False

    def move_forward(self):
        """Use the driver to move the rover forward"""
        self.driver.move_forward()

    def move_backward(self):
        """Use the driver to move the rover backward"""
        self.driver.move_backward()

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

    def change_camera_mode(self, mode):
        """Change the camera mode to the specified mode (color or grayscale)"""
        if mode == "color":
            self.camera.set_color_mode()
        elif mode == "grayscale":
            self.camera.set_grayscale_mode()
        else:
            print("Invalid camera mode specified!")

    def rotate_image(self, angle):
        """Rotate the current camera image by the specified angle"""
        image = Image.open(self.camera.image_path)
        rotated_image = image.rotate(angle)
        rotated_image.save(self.camera.image_path)

    def remove_filters(self):
        """Remove any filters applied to the camera image"""
        self.camera.remove_filters()

    def apply_timestamp(self):
        """Apply a timestamp to the current camera image"""
    
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        image = Image.open(self.camera.image_path)
        draw = ImageDraw.Draw(image)
        width, height = image.size
        x = width - 350
        y = height - 50
        font = ImageFont.truetype("arial.ttf", 36)
        text_color = (255, 255, 255)
        draw.text((x, y), timestamp, font=font, fill=text_color)
        image.save(self.camera.image_path)


    def take_picture(self):
        """Take a picture with the camera and apply a timestamp"""
        self.camera.take_picture()
        self.camera.apply_timestamp()


    def process_rf_command(self):
        """Process an incoming RF command"""
        # Check if there is an incoming RF message
        if self.rf.available():
            # Read the message
            msg = self.rf.recv()
            print(f"Received RF message: {msg}")

            # Process the message
            if msg == b"color_to_grayscale":
                # Change the camera mode to grayscale
                self.camera.set_mode(arducam.GRAYSCALE)
            elif msg == b"grayscale_to_color":
                # Change the camera mode back to color
                self.camera.set_mode(arducam.COLOR)
            elif msg == b"rotate_180":
                # Rotate the current camera image 180 degrees
                self.rotate_image(180)
            elif msg == b"remove_filters":
                # Remove all filters from the current camera image
                self.remove_filters()
            elif msg == b"take_picture":
                # Take a picture
                self.camera.capture()
                # Apply a timestamp to the picture
                self.apply_timestamp()



