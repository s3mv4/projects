extends Node

@export var scroll_speed = 2
var default_scroll_speed
var bottom_position_y
var top_position_y

func _ready():
	default_scroll_speed = scroll_speed
	bottom_position_y = $TextureRect1.position.y + get_viewport().size.y + ($TextureRect1.size.y - get_viewport().size.y) / 2
	top_position_y = $TextureRect1.position.y - get_viewport().size.y - ($TextureRect1.size.y - get_viewport().size.y) / 2
	$TextureRect2.position.y = top_position_y
	$TextureRect2.flip_v = true

func _process(delta):
	$TextureRect1.position.y += scroll_speed
	$TextureRect2.position.y += scroll_speed
	if $TextureRect2.position.y >= bottom_position_y:
		$TextureRect2.position.y = top_position_y
	elif $TextureRect1.position.y >= bottom_position_y:
		$TextureRect1.position.y = top_position_y


func _on_rocket_scroll(velocity):
	scroll_speed = default_scroll_speed - velocity.y / 125
