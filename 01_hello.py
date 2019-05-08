import cocos
from cocos.director import director

#default handle
#ctrl + f : fullscreen
#ctrl + s : screenshot
#ctrl + p : pause
#ctrl + x : display fps
#ctrl + i : pipeline of python
#space : exit

class HelloCocos(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        label = cocos.text.Label("Hello cocos", font_name="Times New Roman", font_size=32, anchor_x="center", anchor_y="center")
        size = director.get_window_size()
        print(size)
        label.position = size[0]/2, size[1]/2
        self.add(label)

if __name__ == "__main__":
    director.init(width=1280, height=720, caption="My cocos window")
    hello_layer = HelloCocos()
    test_scene = cocos.scene.Scene(hello_layer)
    director.run(test_scene)


