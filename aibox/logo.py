from manim import *


class AiBoxBanner(Scene):
    def construct(self):
        # Animation Steps:
        # 1. Write text "Artificial Intelligence"
        # 2. Animate the text to be "AI"
        # 3. Rotate the "I" horizontally
        # 4. Animate square and color the letter "I"
        # 5. Move "I" to the right and rotate the square
        # 6. Write text "Box" to the right of the square

        # Code for step 1
        a_text = Text('Artificial', font_size=100, t2c={'[0:1]': PINK},
                      font="Open Sans", weight="ULTRAHEAVY").move_to(LEFT)
        i_text = Text('Intelligence', font_size=100, t2c={'[0:1]': PINK},
                      font="Open Sans", weight="ULTRAHEAVY").next_to(a_text, RIGHT, buff=0.5)
        i_text.shift(0.12 * DOWN)
        ai_text = VGroup(a_text, i_text)
        ai_text.move_to(ORIGIN)
        self.play(Write(ai_text), run_time=1)

        # Code for step 2
        ai_text2 = Text("AI", font_size=100, font="Open Sans", weight="ULTRAHEAVY")
        ai_text2.set_fill(WHITE)
        self.play(Transform(ai_text, ai_text2), run_time=1)
        ai_text2.set(font_size=300)
        self.play(Transform(ai_text, ai_text2), run_time=2)

        # Code for step 3
        letter_a = Text("A", font_size=300, font="Open Sans", weight="ULTRAHEAVY")
        letter_i = Text("I", font_size=300, font="Open Sans", weight="SEMIBOLD").rotate(PI/2, about_point=ORIGIN)
        letter_i.shift(0.6 * DOWN)
        group_ai = VGroup(letter_a, letter_i)
        # group_ai.move_to(ORIGIN)
        self.play(Transform(ai_text, group_ai), run_time=1)

        # Code for step 4
        square = Square(side_length=5).rotate(PI / 4)
        letter_i.set_fill(PINK, opacity=1)  # set the color and transparency
        group_ai = VGroup(letter_a, letter_i)
        self.play(Transform(ai_text, group_ai), Create(square), run_time=1)

        # Code for step 5
        letter_i.shift(0.95 * RIGHT)
        group_ai = VGroup(letter_a, letter_i)
        self.play(Transform(ai_text, group_ai), square.animate.rotate(PI / 4), run_time=1)

        # Code for step 6
        box_text = Text("BOX", font_size=100, font="Open Sans", weight="ULTRAHEAVY").next_to(square, RIGHT, buff=0.5)
        self.play(Write(box_text), run_time=1)
