import cocos
from cocos.director import director
import pyglet

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
        self.add(spr)

class Sprite2(cocos.sprite.Sprite):
    def __init__(self):
        super().__init__("res/red-blue/124.png")
        self.position = 640, 360

if __name__ == "__main__":
    director.init(width=1080, height= 720, caption="My cocos window")
    #director.window.pop_handlers()
    spr1_layer = Sprite1()#layer
    spr2_layer = Sprite2()#sprite
    #test_scene = cocos.scene.Scene(spr1_layer)
    test_scene = cocos.scene.Scene()
    test_scene.add(spr1_layer)
    test_scene.add(spr2_layer)
    director.run(test_scene)