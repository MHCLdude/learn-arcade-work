import arcade

arcade.open_window(800, 600, "My Programmed Drawing")
arcade.set_background_color(arcade.color.BLUE_GREEN)
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.GREEN)
arcade.draw_lrtb_rectangle_filled(200, 300, 300, 200, arcade.color.BLUE)
arcade.draw_circle_filled(250, 350, 80, arcade.color.YELLOW)
arcade.draw_point(220, 365, arcade.color.BLACK, 10)
arcade.draw_point(280, 365, arcade.color.BLACK, 10)
arcade.draw_arc_outline(250, 320, 50, 50, arcade.color.BLACK, 180, 360, 10)
arcade.draw_circle_filled(700, 500, 80, arcade.color.YELLOW_ORANGE)

arcade.run()
