import OpenGL
import OpenGL.GL  
import OpenGL.GLUT  
import OpenGL.GLU  
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def squarey(x,y,z):     
    glBegin(GL_QUADS)
    glVertex3f(x+.05,y,z+.05)
    glVertex3f(x-.05,y,z+.05)
    glVertex3f(x-.05,y,z-.05)
    glVertex3f(x+.05,y,z-.05)
    glEnd()

def squarex(x,y,z):     
    glBegin(GL_QUADS)
    glVertex3f(x,y+.05,z+.05)
    glVertex3f(x,y-.05,z+.05)    
    glVertex3f(x,y-.05,z-.05)
    glVertex3f(x,y+.05,z-.05)
    glEnd()
    
def squarez(x,y,z):     
    glBegin(GL_QUADS)
    glVertex3f(x+.05,y+.05,z)
    glVertex3f(x+.05,y-.05,z)
    glVertex3f(x-.05,y-.05,z)
    glVertex3f(x-.05,y+.05,z)
    glEnd()

def cubo(x,y,z):
    squarey(x,y-.05,z)
    squarey(x,y+.05,z)
    squarex(x-.05,y,z)
    squarex(x+.05,y,z)
    squarez(x,y,z+.05)
    squarez(x,y,z-.05)

def dibujar(x,y,veces,orientacion):
  for i in range(veces):
    if orientacion=="derecha":
      cubo(x,y,0)
      x=x+0.1
    elif orientacion=="izquierda":
      cubo(x,y,0)
      x=x-0.1
    elif orientacion=="arriba":
      cubo(x,y,0)
      y=y+0.1
    elif orientacion=="abajo":
      cubo(x,y,0)
      y=y-0.1

def laberinto():
    dibujar(-0.75,.95,2,"abajo")
    dibujar(-0.85,.85,3,"abajo")
    dibujar(-0.85,.65,3,"derecha")
    dibujar(-0.55,.65,3,"arriba")
    dibujar(-0.55,.85,3,"derecha")
    dibujar(-0.35,.85,3,"abajo")
    dibujar(-0.35,.65,4,"derecha")
    dibujar(-0.05,.65,3,"abajo")
    dibujar(-0.15,.65,3,"arriba")
    dibujar(-0.15,.85,4,"derecha")
    dibujar(0.15,.85,5,"abajo")
    dibujar(0.15,.45,3,"derecha")
    dibujar(0.35,.45,5,"arriba")
    dibujar(0.35,.85,5,"derecha")
    dibujar(0.75,.85,3,"abajo")
    dibujar(0.75,.65,3,"izquierda")
    dibujar(0.55,.65,5,"abajo")
    dibujar(0.55,.45,3,"derecha")
    dibujar(0.75,.45,8,"abajo")
    dibujar(0.75,.05,7,"izquierda")
    dibujar(0.15,.05,2,"abajo")
    dibujar(0.15,-.05,4,"izquierda")
    dibujar(-0.05,-.05,2,"arriba")
    dibujar(0.35,.05,3,"arriba")
    dibujar(0.35,.25,7,"izquierda")
    dibujar(-0.25,.15,4,"arriba")
    dibujar(-0.25,.15,3,"izquierda")
    dibujar(-0.45,.25,3,"izquierda")
    dibujar(-0.25,.45,7,"izquierda")
    dibujar(-0.85,.45,8,"abajo")
    dibujar(-0.85,.05,3,"derecha")
    dibujar(-0.85,-.25,3,"derecha")
    dibujar(-0.65,-.25,3,"abajo")
    dibujar(-0.65,-.45,3,"izquierda")
    dibujar(-0.85,-.45,5,"abajo")
    dibujar(-0.65,-.05,4,"derecha")
    dibujar(-0.35,-.05,3,"abajo")
    dibujar(-0.45,-.25,3,"abajo")
    dibujar(-0.45,-.45,4,"derecha")
    dibujar(-0.15,-.45,3,"arriba")
    dibujar(-0.15,-.25,3,"derecha")
    dibujar(0.05,-.25,5,"abajo")
    dibujar(.15,-.65,9,"izquierda")
    dibujar(-0.65,-.65,3,"abajo")
    dibujar(-0.65,-.85,15,"derecha")
    dibujar(0.35,-.85,5,"arriba")
    dibujar(0.25,-.45,3,"arriba")
    dibujar(0.35,-.25,2,"arriba")
    dibujar(0.35,-.15,3,"derecha")
    dibujar(0.55,-.15,4,"abajo")
    dibujar(0.55,-.45,4,"derecha")
    dibujar(0.75,-.45,3,"abajo")
    dibujar(0.75,-.65,3,"izquierda")
    

def iterate():  
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION) #Seleccionamos la matriz de proyección
    glLoadIdentity()#Limpiamos la matriz seleccionada
    glOrtho(-1.5,1.5, -1.5,1.5, -1.0, 1.0)#Definimos la proyección a usar como una ortogonal
    glMatrixMode (GL_MODELVIEW) #Seleccionamos la matriz del modelo 
    glLoadIdentity()#Limpiamos la matriz seleccionada, a partir de este punto lo que se haga quedara en la matriz del modelo de vista


def showScreen():   
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate();
    glRotatef(45,0.0,1.0,0.0)
    laberinto()
    #squarey(0,0,0)
    glutSwapBuffers()

def main():
    print('hola mundo')
    glutInit() # Iniciamos la instancia de glut
    glutInitDisplayMode(GLUT_RGB| GLUT_DOUBLE| GLUT_DEPTH) # Asignamos el modelo de color que usaremos   
    glutInitWindowSize(600, 600)   # Damos el tamaño de la ventana que se mostrará  
    glutInitWindowPosition(0, 0)   # Coordenadas en donde aparecerá la venta en la pantalla   
    glutCreateWindow("Laberinto") # Damos un titulo para la ventana
    glClearColor(0,0,0,1)
     
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(showScreen)  # Designamos la función que contiene los elemntos que serán mostrados en la escena 
    glutIdleFunc(showScreen)     
    glutMainLoop()  # Iniciamos el loop principal
    return 0

main()
