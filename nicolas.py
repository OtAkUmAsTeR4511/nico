x=0
y=0
def arriba():
    
    while True:
        if arriba():
            Y=Y-1
            if abajo():
                y=y+1
                if derecha():
                    x=x+1
                    if izquierda():
                        x=x-1
    return True

