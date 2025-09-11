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
#WINDOW_SIZE = 3

def blur_ingenuo(img):
    rows = img.shape[0]
    cols = img.shape[1]
    
    img_out = img.copy()

    for row in range(rows):
        for col in range(cols):
            count = 0
            for i in range(i - WINDOW_SIZE//2,i + WINDOW_SIZE//2):
                for j in range(j - WINDOW_SIZE//2, j + WINDOW_SIZE//2):
                     count += img[i, j]
            img[row, col] = count / (WINDOW_SIZE * WINDOW_SIZE)
    
    return img_out
            

def blur_separado(img):
    rows = img.shape[0]
    cols = img.shape[1]        


def blur_integral(img):


def main():

    img = cv2.imread(INPUT_IMAGE)

    if img is None:
        print("Imagem não encontrada em %s" % INPUT_IMAGE)
        return

    # Convert to float32 and normalize to [0, 1]
    img = img.astype(np.float32) / 255.0

    borrada = blur_ingenuo(img)

    borrada = blur_separado(img)

    borrada = blur_integral(img)

    # Save the output image, converting back to [0, 255]
    cv2.imwrite('blur.png', borrada * 255)

