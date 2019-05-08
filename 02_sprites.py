import cocos
from cocos.director import director

class Sprite1(cocos.layer.Layer):
    def __init__(self):
        super().__init__()

        spr = cocos.sprite.Sprite("res/red-blue/140.png")
        spr.position = 400, 360
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