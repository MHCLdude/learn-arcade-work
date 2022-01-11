import arcade

arcade.open_window(800, 600, "Lab 3 Drawing")
arcade.set_background_color(arcade.color.DEEP_SKY_BLUE)

arcade.start_render()

def draw_grass(x1, y1, x2, y2):
    arcade.draw_lrtb_rectangle_filled(x1, y1, x2, y2, arcade.csscolor.GREEN)

def draw_sun(x, y, size):
    arcade.draw_circle_filled(x, y, size, arcade.csscolor.ORANGE)

def draw_head(x, y, size):
    arcade.draw_circle_filled(x, y, size, arcade.color.YELLOW)

def draw_body(x1, y1, x2, y2):
    arcade.draw_lrtb_rectangle_filled(x1, y1, x2, y2, arcade.color.BLUE)

def draw_left_eye(x, y, size):
    arcade.draw_point(x, y, arcade.color.BLACK, size)

def draw_right_eye(x, y, size):
    arcade.draw_point(x, y, arcade.color.BLACK, size)

def draw_mouth(x, y, width, height, start_angle, end_angle, border_width):
    arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, border_width)

def draw_person():
    draw_body(200, 300, 300, 200)
    draw_head(250, 350, 70)
    draw_left_eye(220, 365, 10)
    draw_right_eye(280, 365, 10)
    draw_mouth(250, 330, 50, 50, 180, 360, 10)

#draws everything
def draw_all():
    draw_grass(0, 800, 200, 0)
    draw_sun(700, 500, 60)
    draw_person()
draw_all()

arcade.run()