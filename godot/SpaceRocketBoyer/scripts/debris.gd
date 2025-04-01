extends Area2D

@export var debris_velocity = 5
var default_velocity
var screen_size

func _ready():
	screen_size = get_viewport_rect().size
	default_velocity = debris_velocity
	var debris_types = [
		"asteroid1", "asteroid2", "coin", "dagger", "grapes"
	]
	
	var debris_weights = [
		5, 5, 1, 2, 2
	]
	
	var weighted_debris_types = []
	for i in range(debris_types.size()):
		for j in range(debris_weights[i]):
			weighted_debris_types.append(debris_types[i])
	
	$AnimatedSprite2D.play(weighted_debris_types[randi() % weighted_debris_types.size()])
	
	if $AnimatedSprite2D.animation == "asteroid1" or $AnimatedSprite2D.animation == "asteroid2":
		if randi() % 2:
			$AnimatedSprite2D/AnimationPlayer.play("rotate")
		else:
			$AnimatedSprite2D/AnimationPlayer.play_backwards("rotate")
	elif $AnimatedSprite2D.animation == "coin":
		$AnimatedSprite2D/AnimationPlayer.play("horizontal_spin")
	elif $AnimatedSprite2D.animation == "dagger":
		$AnimatedSprite2D/AnimationPlayer.play("vibrate")
	elif $AnimatedSprite2D.animation == "grapes":
		$AnimatedSprite2D/AnimationPlayer.play("wobble")

func _process(delta):
	position.y += debris_velocity
	if position.y >= screen_size.y:
		queue_free()


func _on_body_entered(body):
	if body.name == "Rocket":
		queue_free()

func scroll_rocket_vel(velocity):
	debris_velocity = default_velocity - velocity.y / 125
