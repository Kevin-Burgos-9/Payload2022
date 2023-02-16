import cv2
from datetime import datetime

class Camera:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        pass

    def take_picture(self, grayscale: bool, flip : bool, filters : bool) -> None:
        '''Take a picture and apply all filters and effects and the time stamp
        and return location where the file was saved'''

        # Code Here -------------

        
        return_value, image = self.cam.read()
        dt = datetime.now()
        print('Picture taken at: ' + str(dt))

        cv2.imwrite('temp.png', image)

        if grayscale :
            image = cv2.imread('temp.png', 0)
        
        if flip :
            image = cv2.flip(image, 0)

        if filters :
            image = cv2.blur(image, (10,10))

        cv2.putText(img=image, text=str(dt), org=(1000, 1000), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3.5, color=(10, 235, 245), thickness=3)
        
        #cv2.imshow(str(dt), image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        cv2.imwrite(str(dt) + '.png', image)

    def apply_time_stamp(self, img: str) -> str:
        '''Apply timestamp to image and return saved location'''
        save_location: str

        # Code Here -------------

        # Estas dos lineas son las que enseñan el timestamp en la foto

        img_original = cv2.imread('imagen.jpg')

        # cuando el valor adentro del parentesis esta es 1 producira la foto normal
        # cuando el valor de adentro es 0 producira la foto en grayscale
        imgs = cv2.imread(img, 0)

        # cuando el flip code es 0 la imagen rotara verticalmente
        # cuando el flip code es un numero positivo la imagen rotara horizontalmente
        # si es un numero negativo hara ambas
        imgs = cv2.flip(imgs, -1)

        # esta bloque se utiliza para añadirle un filtro a la foto
        # en este caso se le añadio un blur filter
        ksize = (10, 10)
        imgs = cv2.blur(imgs, ksize)

        # Que hace cada funcion
        # org(X cordenada, Y cordenada) para ajustar el timestamp en la foto
        # fronFace - El estile del timestamp
        # frontScale - Tamaño de timestamp
        
        

        # -----------------------

        return save_location
