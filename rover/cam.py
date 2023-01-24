import cv2
from datetime import datetime


class Camera:
    def __init__(self):
        self.grayscale: bool = False
        self.flip: bool = False
        self.filters: bool = False
        pass

    def toggle_grayscale(self):
        '''Enable/Disable Grayscale mode'''
        pass

    def take_picture(self, grasycale: bool, flip: bool, filters: bool) -> str:
        '''Take a picture and apply all filters and effects and the time stamp
        and return location where the file was saved'''

        save_location: str

        # Code Here -------------

        # remember to enable grayscale and flip image if needed

        # -----------------------

        if filters:
            save_location = self.apply_Filters()

        save_location = self.apply_time_stamp(save_location)

        return save_location

    def apply_time_stamp(self, img: str) -> str:
        '''Apply timestamp to image and return saved location'''
        save_location: str

        # Code Here -------------

        dt = datetime.now()
        print(str(dt))

        imgs = cv2.imread(img, 1)

        cv2.putText(img=imgs, text=str(dt), org =(0, 30),fontFace = cv2.FONT_HERSHEY_PLAIN, fontScale = 1, color = (10, 235, 245))


        cv2.imshow("image", imgs)
        cv2.waitKey(0)
        cv2.destroyAllWindows()





        ts = datetime.timestamp(dt)

        print("Date and time is: ", dt)
        print("Timestamp is: ", ts)

        # -----------------------

        return save_location

    def apply_filters(self, img: str) -> str:
        '''Apply filters to image and return saved location'''
        save_location: str

        # Code Here -------------

        # -----------------------

        return save_location


c = Camera()
c.apply_time_stamp("./imagen.jpg")
