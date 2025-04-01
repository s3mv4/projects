extends Node2D

@export var debris_scene: PackedScene
@export var grid_width = 5
var grid_size
var screen_size

func _on_debris_timer_timeout():
	screen_size = get_viewport_rect().size
	grid_size = screen_size.x / grid_width
	var debris = debris_scene.instantiate()
	debris.position = Vector2(randi() % grid_width * grid_size + grid_size / 2, 0)
	$Rocket.connect("scroll", debris, "scroll_rocket_vel")
	add_child(debris)


func _on_rocket_scroll(velocity):
	for child in get_children():
		if child.name == "Debris":
			print(child)
			child.scroll_rocket_vel(velocity)
