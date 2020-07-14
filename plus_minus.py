def findPoint(px, py, qx, qy):
    #Pegando o delta_x do ponto Qx - Px
    delta_x = qx - px
    #Pegando o delta_y do ponto Qy - Py
    delta_y = qy - py

    #O resultado da soma dos pontos Qx + delta_x e Qy + delta_y é o
    #point reflection ou reflexão desses pontos
    return qx + delta_x, qy + delta_y

findPoint(0, 0, 1, 1)