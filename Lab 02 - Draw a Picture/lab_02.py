import arcade

arcade.open_window(800, 600, "Play Minecraft NOW")
arcade.set_background_color(arcade.color.BLUE_GREEN)
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(160, 245, 300, 50, arcade.color.AMETHYST)
arcade.draw_lrtb_rectangle_filled(60, 200, 200, 50, arcade.color.AFRICAN_VIOLET)
arcade.draw_triangle_filled(75, 77, 94, 28, 24, 80, arcade.color.AUROMETALSAURUS)
arcade.draw_lrtb_rectangle_filled(267, 600, 560, 180, arcade.color.CARNATION_PINK)
arcade.draw_lrtb_rectangle_filled(120, 450, 456, 189, arcade.color.DARK_PASTEL_RED)
arcade.draw_triangle_filled(125, 87, 154, 68, 74, 180, arcade.color.BISTRE)
arcade.draw_lrtb_rectangle_filled(20, 45, 30, 20, arcade.color.AMETHYST)
arcade.draw_lrtb_rectangle_filled(60, 200, 200, 50, arcade.color.AFRICAN_VIOLET)
arcade.draw_triangle_filled(75, 77, 104, 78, 24, 80, arcade.color.AUROMETALSAURUS)
arcade.draw_lrtb_rectangle_filled(267, 600, 560, 380, arcade.color.CARNATION_PINK)
arcade.draw_lrtb_rectangle_filled(320, 950, 456, 419, arcade.color.GRANNY_SMITH_APPLE)

arcade.run()