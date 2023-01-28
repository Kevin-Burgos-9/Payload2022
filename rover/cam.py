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

        #Estas dos lineas son las que enseñan el timestamp en la foto

        dt = datetime.now()
        print(str(dt))

        img_original = cv2.imread('imagen.jpg')

        #cuando el valor adentro del parentesis esta es 1 producira la foto normal
        #cuando el valor de adentro es 0 producira la foto en grayscale
        imgs = cv2.imread(img, 0)


        #cuando el flip code es 0 la imagen rotara verticalmente
        #cuando el flip code es un numero positivo la imagen rotara horizontalmente

        imgs = cv2.flip(imgs,-1)

        #esta bloque se utiliza para añadirle un filtro a la foto
        #en este caso se le añadio un blur filter
        ksize = (10,10)
        imgs = cv2.blur(imgs, ksize)


        #Que hace cada funcion
        #org(X cordenada, Y cordenada) para ajustar el timestamp en la foto
        #fronFace - El estile del timestamp
        #frontScale - Tamaño de timestamp
        cv2.putText(img=imgs, text=str(dt), org =(250, 300),fontFace = cv2.FONT_HERSHEY_PLAIN, fontScale = 0.75, color = (10, 235, 245))

        cv2.imshow("Normal Image", img_original)
        cv2.imshow("image", imgs)
        cv2.waitKey(0)
        cv2.destroyAllWindows()







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
