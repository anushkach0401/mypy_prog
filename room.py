from vpython import *
from time import *
ceil=box(pos=vector(0,5,0),color=color.blue,length=10,width=10,height=0.1)
floor=box(pos=vector(0,-5,0),color=color.blue,length=10,width=10,height=0.1)
right_wall=box(pos=vector(5,0,0),color=color.blue,length=0.1,width=10,height=10)
left_wall=box(pos=vector(-5,0,0),color=color.blue,length=0.1,width=10,height=10)
back=box(pos=vector(0,0,-5),color=color.blue,length=10,width=0.1,height=10)
ball=sphere(color=color.red)
sleep(2)
ball.color=color.black
while True:
    pass

