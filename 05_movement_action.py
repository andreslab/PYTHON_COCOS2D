import cocos
from cocos.director import director
import pyglet
from pyglet.window import key


class Mover(cocos.actions.Move):
    def step(self, dt):
        super().step(dt)
        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 500
        vel_y = (keyboard[key.UP] - keyboard[key.DOWN]) * 500
        self.target.velocity = (vel_x, vel_y)

class Sprite1(cocos.layer.Layer):
    def __init__(self):
        super().__init__()

        # spr = cocos.sprite.Sprite("res/red-blue/140.png")
        # spr.position = 400, 360
        # self.add(spr)
        img = pyglet.image.load("res/black_cat.png")
        img_grid = pyglet.image.ImageGrid(img, 1, 4, item_width=310, item_height=188) #1 row and 4 column, dimension of sprite
        print(img_grid[0:])
        anim = pyglet.image.Animation.from_image_sequence(img_grid[0:],0.1,loop=True) #grid, speed, loop
        spr = cocos.sprite.Sprite(anim)
        spr.position = 200, 500

        spr.velocity = (0,0)
        spr.do(Mover())


        self.add(spr)

class Sprite2(cocos.sprite.Sprite):
    def __init__(self):
        super().__init__("res/red-blue/124.png")
        self.position = 640, 360

class CatLayer(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        img = pyglet.image.load("res/gato_recorte.png")
        img_grid = pyglet.image.ImageGrid(img, 4,2, item_width=281, item_height=182)
        #cambiar el orden de los sprites
        temp = []
        for i in reversed(img_grid):
            temp.append(i)
        new_tex= []
        index = 0
        for i in temp:
            new_tex.append(temp[1+index])
            new_tex.append(temp[index])
            index += 2
            if index > 6:
                break
        
        anim = pyglet.image.Animation.from_image_sequence(new_tex[0:], 0.1, loop=True)
        spr = cocos.sprite.Sprite(anim)
        spr.position = 640, 500
        self.add(spr)

if __name__ == "__main__":
    director.init(width=1080, height= 720, caption="My cocos window")


    director.window.pop_handlers() #remove default handle, remueve los comandos de teclados por defecto
    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)

    #director.window.pop_handlers()
    spr1_layer = Sprite1()#layer
    spr2_layer = Sprite2()#sprite
    #test_scene = cocos.scene.Scene(spr1_layer)
    test_scene = cocos.scene.Scene()
    test_scene.add(spr1_layer, 0, "sprite")
    test_scene.add(spr2_layer)

    cat_layer = CatLayer()
    test_scene.add(cat_layer, 0, "cat animation")


    director.run(test_scene)