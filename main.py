


import cv2


def blur_Ingenuo(img):

def blur_Separado(img):

def blur_Integral(img):


def main():

    img = cv2.imread(INPUT_IMAGE)

    if img is None:
        print("Imagem não encontrada em %s" % INPUT_IMAGE)
        return

    # Convert to float32 and normalize to [0, 1]
    img = img.astype(np.float32) / 255.0

    img_out = blur_Ingenuo(img)

    img_out = blur_Separado(img)

    img_out = blur_Integral(img)

    # Save the output image, converting back to [0, 255]
    cv2.imwrite('blur.png', img_out * 255)

