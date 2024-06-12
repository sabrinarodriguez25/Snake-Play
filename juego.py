import turtle
import time 
import random

posponer=0.1

#contador
score=0
high_score=0

#configuracion de la ventana
sk=turtle.Screen() #crear una ventana
sk.title("Juego de Snake")
sk.bgcolor("black")
sk.setup(width=600,height=  600) #medidas de la ventana
sk.tracer(0)


#crear cabeza

cabeza= turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction="stop"
cabeza.color("green")


#crear comida
comida= turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.penup()
comida.goto(0,100)
comida.color("red")


#segmentos cuerpo de serpiente
segmentos=[]

#texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score:0      High Score:0", align= "center", font=("Courier",24, "normal"))
#funciones
def arriba():
    cabeza.direction="up"

def abajo():
    cabeza.direction="down"

def izquierda():
    cabeza.direction="left"

def derecha():
    cabeza.direction="right"

def mov():
    if cabeza.direction =="up":
        y = cabeza.ycor()
        cabeza.sety( y + 20)

    if cabeza.direction =="down":
        y = cabeza.ycor()
        cabeza.sety( y - 20)

    if cabeza.direction =="left":
        x = cabeza.xcor()
        cabeza.setx( x - 20)

    if cabeza.direction =="right":
        x = cabeza.xcor()
        cabeza.setx( x + 20)

#teclado

sk.listen() #eventos
sk.onkeypress(arriba,"Up")
sk.onkeypress(abajo,"Down")
sk.onkeypress(izquierda,"Left")
sk.onkeypress(derecha,"Right")










while True:
    sk.update()

    #colisione bordes

    if cabeza.xcor() >280 or cabeza.xcor() <-290 or cabeza.ycor() >290 or cabeza.ycor() <-290:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction="stop"

        #esconder segmentos
        for segmento in segmentos:
            segmento.goto(1000,1000)

        #limpiar lista
        segmentos.clear()

        #Resetear marcador
        score=0
        texto.clear()
        texto.write("Score:{}   High Score:{}".format(score,high_score), align= "center", font=("Courier",24, "normal"))



    if cabeza.distance(comida)<20:
       x=random.randint(-280,280)
       y=random.randint(-280,280)
       comida.goto(x,y) #actualizar la posicion


       nuevo_segmento= turtle.Turtle()
       nuevo_segmento.speed(0)
       nuevo_segmento.shape("square")
       nuevo_segmento.penup()
       nuevo_segmento.color("#00bb2d")
       segmentos.append(nuevo_segmento)
       

       #aumentar marcador

       score +=10
       if score > high_score:
           high_score=score
        
    texto.clear()
        
    texto.write("Score:{}   High Score:{}".format(score,high_score), align= "center", font=("Courier",24, "normal"))

    #mover el cuerpo
    totalseg=len(segmentos)
    for index in range(totalseg -1, 0, -1):
        x = segmentos[index -1].xcor()
        y =segmentos[index -1].ycor()
        segmentos[index].goto(x,y)
    
    if totalseg >0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
    mov()

    #colisionar con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) <20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction="stop"

            for segmento in segmentos:
                segmento.goto(1000,1000)

            segmentos.clear()


            score=0
            texto.clear()
            texto.write("Score:{}   High Score:{}".format(score,high_score), align= "center", font=("Courier",24, "normal"))





  
    time.sleep(posponer)