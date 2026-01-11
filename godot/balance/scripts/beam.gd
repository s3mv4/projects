extends CharacterBody2D

var rotation_speed = 3

var dragging = false
var start_position = Vector2.ZERO
var start_rotation = 0.0

func _input(event):
	if (event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT) or (event is InputEventScreenTouch):
		if event.pressed:
			start_position = event.position
			start_rotation = rotation
			dragging = true
		else:
			dragging = false

	if (event is InputEventMouseMotion and dragging) or (event is InputEventScreenDrag):
		var horizontal_drag_distance = event.position.x - start_position.x
		rotation = clamp(start_rotation + horizontal_drag_distance * 0.0015, -0.785, 0.785)

func _process(delta):
	pass
