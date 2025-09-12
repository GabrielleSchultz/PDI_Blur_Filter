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

    #percorre a imagem (nos três canais), desconsiderando as bordas
    for channel in range (colors):
        for row in range(h//2, rows - (h//2)):
            for col in range(w//2, cols - (w//2)):
                soma = 0
                #faz a média do pixel com os valores dos vizinhos na janela deslizante
                for i in range(row - h//2, row + h//2 + 1): 
                    for j in range(col - w//2, col + w//2 + 1):
                        soma += img[i, j, channel]
                img_out[row, col, channel] = soma / (h * w)
    
    return img_out

'Versão com filtro separado do algoritmo de blur'
'Recebe uma imagem (colorida) e o tamanho w dos lados da janela'
'Retorna a imagem recebida borrada'

def blur_separavel(img, w, h):

    rows = img.shape[0]
    cols = img.shape[1]
    colors = img.shape[2]

    buffer = img.copy() # armazena a imagem em um buffer temporário para borrar na horizontal
    
    #percorre na horizontal
    for channel in range (colors):
        for row in range (rows):
            for col in range (w//2, cols - (w//2)):
                soma = 0
                for i in range(col - w//2, col + w//2 + 1):
                    soma += img[row, i, channel]
                buffer[row, col, channel] = soma / w

    #armazena uma imagem final, a partir da imagem borrada na horizontal
    img_final = buffer.copy()

    #percorre na vertical
    for channel in range (colors):
        for row in range (h//2, rows - (h//2)):
            for col in range (cols):
                soma = 0
                for i in range(row - h//2, row + h//2 + 1):
                    soma += buffer[i, col, channel]
                img_final[row, col, channel] = soma / h

    return img_final

def blur_integral(img, w, h):
    rows = img.shape[0]
    cols = img.shape[1]
    colors = img.shape[2]

    img_integral = img.copy()
    img_out = img.copy()  

    #cria a imagem integral
    for c in range(colors):
        for i in range(rows):
            img_integral[0, i, c] = img[0, i, c]
            for j in range(cols + 1):
                img_integral[j, i, c] = img[j, i, c] + img_integral[j - 1, i, c]
        for i in range(cols):
            img_integral[i, 0, c] = img[i, 0, c]
            for j in range(rows + 1):
                img_integral[i, j, c] = img[i, j, c] + img_integral[i, j - 1, c]

    #img_out = np.zeros_like(img)
    # Create an integral image
    """integral_img = np.zeros((rows + 1, cols + 1), dtype=np.float32)
    
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            integral_img[i, j] = (img[i - 1, j - 1] +
                                  integral_img[i - 1, j] +
                                  integral_img[i, j - 1] -
                                  integral_img[i - 1, j - 1])"""
    

    # Apply the blur using the integral image
    for c in range(colors):
            for i in range(rows):
                for j in range(cols):
                    x0 = max(i - h//2, 0) # x0, y0 é o canto superior esquerdo da janela
                    y0 = max(j - w//2, 0) # y0 é o canto superior esquerdo da janela
                    x1 = min(i + h//2, rows + 1) # x1, y1 é o canto inferior direito da janela
                    y1 = min(j + w//2, cols + 1) # y1 é o canto inferior direito da janela

                    a1 = img_integral[x1, y1] # a1, a2, a3, a4 são os valores nos cantos da janela
                    a2 = img_integral[x0, y1]
                    a3 = img_integral[x1, y0]
                    a4 = img_integral[x0, y0]

                    area_sum =  a1 - a2 - a3 + a4 # soma dos valores na janela
                    img_out[i, j, c] = area_sum // (h * w) # média dos valores na janela
    return img_out

def main():

    # Leitura da imagem
    img = cv2.imread(INPUT_IMAGE)

    if img is None:
        print("Imagem não encontrada em %s" % INPUT_IMAGE)
        return

    # Converte para float
    img = img.astype(np.float32) / 255

    'funções:'
    #borrada = blur_ingenuo(img, WINDOW_WIDTH, WINDOW_HEIGHT)
    borrada = blur_separavel(img, WINDOW_WIDTH, WINDOW_HEIGHT)
    #borrada = blur_integral(img, WINDOW_WIDTH, WINDOW_HEIGHT)

    # Salva a imagem de saída (borrada)
    cv2.imwrite('blur.png', (borrada * 255).astype(np.uint8))

if __name__ == '__main__':
    main ()

