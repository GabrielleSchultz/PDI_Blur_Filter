#===============================================================================
# Filtro de Blur usando diferentes abordagens
#-------------------------------------------------------------------------------
# Universidade Tecnológica Federal do Paraná
# Alunos: Gabrielle Vercelhese Schultz e Laura Ferraz Pelisson
#===============================================================================

import numpy as np
import cv2

#===============================================================================

#INPUT_IMAGE = ''

def blur_Ingenuo(img):
    rows = img.shape[0]
    cols = img.shape[1]
    
    for row in range(rows):
        for col in range(cols):
            acc = np.zeros(3)
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    r = row + i
                    c = col + j
                    if 0 <= r < rows and 0 <= c < cols:
                        acc += img[r, c]
                        count += 1
            img[row, col] = acc / count

    return img
            

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

