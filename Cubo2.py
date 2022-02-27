import OpenGL
import OpenGL.GL  
import OpenGL.GLUT  
import OpenGL.GLU  
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

theta=45
rx=0 #variables de rotacion de la camara
ry=0
rz=0
dirx=1.2 #variables de posicion de la camara
diry=1.2
dirz=1.2
def square1():     
    glBegin(GL_QUADS)
    glColor3f(1.0,1.0,0.0)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f( 0.5, 0.5, 0.5)
    glVertex3f( 0.5,-0.5, 0.5)
    glVertex3f(-0.5,-0.5, 0.5)
    glEnd()

def square2():     
    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,1.0)
    glVertex3f(-0.5, 0.5,-0.5)
    glVertex3f(0.5, 0.5,-0.5)
    glVertex3f(0.5,-0.5,-0.5)
    glVertex3f(-0.5,-0.5,-0.5)
    glEnd()

def square3():     
    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,0.0)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5,-0.5)
    glVertex3f(-0.5,-0.5,-0.5)
    glVertex3f(-0.5,-0.5, 0.5)
    glEnd()

def square4():     
    glBegin(GL_QUADS)
    glColor3f(0.0,1.0,0.0)
    glVertex3f( 0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5,-0.5)
    glVertex3f(0.5,-0.5,-0.5)
    glVertex3f(0.5,-0.5, 0.5)
    glEnd()

def square5():     
    glBegin(GL_QUADS)
    glColor3f(0.0,0.0,1.0)
    glVertex3f(0.5,-0.5, 0.5)
    glVertex3f(-0.5,-0.5, 0.5)
    glVertex3f(-0.5,-0.5,-0.5)
    glVertex3f(0.5,-0.5,-0.5)
    glEnd()

def square6():     
    glBegin(GL_QUADS)
    glColor3f(0.1,0.0,0.0)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5,-0.5)
    glVertex3f(-0.5, 0.5,-0.5)
    glEnd()        

def cubo():
    square1()
    square2()
    square3()
    square4()
    square5()
    square6()
    global theta
    theta = theta + 0.20
    if(theta > 360):
        theta = 0

def iterate():  
    screenSize = (600, 100)
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION) #Seleccionamos la matriz de proyección
    glLoadIdentity()#Limpiamos la matriz seleccionada
    #glOrtho(-5.0,5.0, -5.0,5.0, -1.0, 1.0)#Definimos la proyección a usar como una ortogonal
    glFrustum(-3, 3, -3, 3, 1, 5)
    glMatrixMode (GL_MODELVIEW) #Seleccionamos la matriz del modelo 
    glLoadIdentity()#Limpiamos la matriz seleccionada, a partir de este punto lo que se haga quedara en la matriz del modelo de vista


def showScreen():   
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    print(rx,ry,rz)
    gluLookAt(dirx, diry, dirz, rx, ry, rz, 0, 0, 1)
    glRotatef(theta,1.0,1.0,1.0)
    cubo()
    glutSwapBuffers()

def mover(key,x,y):
    global ry
    global rx
    global rz
    global dirx
    global diry
    global dirz
    if (key==GLUT_KEY_F10):
        ry=0
        rx=0
        rz=0
        dirx=1
        diry=1
        dirz=1
    elif (key==GLUT_KEY_RIGHT):
        ry= ry+0.05  
    elif (key==GLUT_KEY_LEFT):
        ry= ry-0.05
    elif (key==GLUT_KEY_UP):
        rx= rx+0.05
    elif (key==GLUT_KEY_DOWN):
        rx= rx-0.05
    elif (key==GLUT_KEY_F11):
        rz= rz+0.05
    elif (key==GLUT_KEY_F12):
        rz= rz-0.05
    if(key==GLUT_KEY_F1):
        diry= diry+0.05
        ry= ry+0.05
    elif(key==GLUT_KEY_F2):
        diry= diry-0.05
        ry= ry-0.05
    elif(key==GLUT_KEY_F3):
        dirx= dirx+0.05
        rx= rx+0.05 
    elif(key==GLUT_KEY_F4):
        dirx= dirx-0.05
        rx= rx-0.05 
    elif(key==GLUT_KEY_F5):
        dirz= dirz+0.05
        rz= rz+0.05 
    elif(key==GLUT_KEY_F6):
        dirz= dirz-0.05
        rz= rz-0.05
def main():
    print('hola mundo')
    glutInit() # Iniciamos la instancia de glut
    glutInitDisplayMode(GLUT_RGB| GLUT_DOUBLE| GLUT_DEPTH) # Asignamos el modelo de color que usaremos   
    glutInitWindowSize(600, 600)   # Damos el tamaño de la ventana que se mostrará  
    glutInitWindowPosition(0, 0)   # Coordenadas en donde aparecerá la venta en la pantalla   
    glutCreateWindow("Cubo") # Damos un titulo para la ventana
    glClearColor(0,0,0,1)
    glColor3f(1,0,0)            
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(showScreen)  # Designamos la función que contiene los elemntos que serán mostrados en la escena 
    glutIdleFunc(showScreen)
    glutSpecialFunc(mover)    
    glutMainLoop()  # Iniciamos el loop principal
    return 0

main()