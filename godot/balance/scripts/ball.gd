extends RigidBody2D

var reset_position = false
var sprite_width = 0
var sprite_height = 0

func _ready():
	sprite_width = $Sprite2D.texture.get_width() * $Sprite2D.scale.x
	sprite_height = $Sprite2D.texture.get_height() * $Sprite2D.scale.y


func _physics_process(delta):
	if (position.y >= get_viewport_rect().size.y / 2 + sprite_height): #or 
		#position.x <= get_viewport_rect().size.x / 2 * -1 - sprite_width or 
		#position.x >= get_viewport_rect().size.x / 2 + sprite_width):
		reset_position = true

func _integrate_forces(state):
	if reset_position:
		var transform = state.transform
		transform.origin = Vector2(0, 0)
		state.transform = transform
		state.linear_velocity = Vector2.ZERO
		state.angular_velocity = 0.0
		reset_position = false
