from ursina import *
from random import randrange
import time

app = Ursina()

camera.orthographic = True
camera.fov = 20
window.color = color.white
window.title = 'Ball game'
camera.orthographic = True

points = 0

gulky = []
gulka = Entity(
    model = 'sphere',
    color = color.black,
    scale = (0.7,0.7,.7),
    position = (0,0,0),
    collider='box'
)

enemy = Entity(
    model = 'sphere',
    color = color.red,
    position = (random.randrange(-15,15),random.randrange(-8,8)),
    scale = (.3,.3),
    collider='sphere'
)
gulky.append(enemy)

point = Entity(
    model='sphere',
    color=color.black,
    position=(random.randrange(-15, 15), random.randrange(-8, 8)),
    scale=(.3,.3),
    collider='sphere'

)

label = Text(
    text=f'{0}',
    color = color.black,
    position = (-0, 0),
)

def update():
    gulka.x += held_keys['d'] * .1
    gulka.x -= held_keys['a'] * .1
    gulka.y += held_keys['space'] * 0.1
    gulka.y = gulka.y - 4 * time.dt

    if gulka.intersects(point).hit:
        global points
        global new
        points += 1
        label.text = f'{points}'
        point.position = (random.randrange(-13, 13), random.randrange(-10,10))
        enemy.position = (random.randrange(-13, 13), random.randrange(-10,10))

        new = duplicate(enemy,position = (random.randrange(-13, 13), random.randrange(-10, 10)))
        gulky.append(new)


    if gulka.intersects(enemy).hit or gulka.intersects(new).hit:
        application.pause()
        label.text = 'You Died'

app.run()