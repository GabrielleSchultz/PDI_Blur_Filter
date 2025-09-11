#===============================================================================
# Filtro de Blur usando diferentes abordagens
#-------------------------------------------------------------------------------
# Universidade Tecnológica Federal do Paraná
# Alunos: Gabrielle Vercelhese Schultz e Laura Ferraz Pelisson
#===============================================================================

import numpy as np
import cv2

#===============================================================================

INPUT_IMAGE = "Exemplos/a01 - Original.bmp"
WINDOW_HEIGHT = 13
WINDOW_WIDTH = 3

'Versão ingênua do algoritmo de blur'
'Recebe uma imagem (colorida) e o tamanho dos lados da janela deslizante.'
'Retorna a imagem recebida borrada'

def blur_ingenuo(img, w, h):
    
    img_out = img.copy()

    rows = img.shape[0]
    cols = img.shape[1]
    colors = img.shape[2]

    # Percorre a imagem (nos três canais), desconsiderando as bordas
    for channel in range (colors):
        for row in range(h//2, rows - (h//2)):
            for col in range(w//2, cols - (w//2)):
                soma = 0
                # Faz a média do pixel com os valores dos vizinhos na janela deslizante
                for i in range(row - h//2, row + h//2 + 1): 
                    for j in range(col - w//2, col + w//2 + 1):
                        soma += img[i, j, channel]
                img_out[row, col, channel] = soma / (h * w)
    
    return img_out

'Versão com filtro separado do algoritmo de blur'
'Recebe uma imagem (colorida) e o tamanho w dos lados da janela'
'Retorna a imagem recebida borrada'

#def blur_separado(img):

#def blur_integral(img):


def main():

    # Leitura da imagem
    img = cv2.imread(INPUT_IMAGE)

    if img is None:
        print("Imagem não encontrada em %s" % INPUT_IMAGE)
        return

    # Converte para float
    img = img.astype(np.float32) / 255

    borrada = blur_ingenuo(img, WINDOW_WIDTH, WINDOW_HEIGHT)

    # Salva a imagem de saída (borrada)
    cv2.imwrite('blur.png', (borrada * 255).astype(np.uint8))

if __name__ == '__main__':
    main ()

