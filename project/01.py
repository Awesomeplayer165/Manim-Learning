from manim import *

class MyAweseomeScene(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        self.wait(2)