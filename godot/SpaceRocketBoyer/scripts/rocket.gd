extends CharacterBody2D

@export var speed = 0
@export var speed_cap = 1000
@export var acceleration = 20
@export var gravity = 500
@export var deceleration_rate = 1

var upper_border

var dragging = false
var start_position = Vector2.ZERO
var start_rotation = 0.0

var screen_size

signal scroll

func _ready():
	screen_size = get_viewport_rect().size
	upper_border = screen_size.y / 4
	$AnimatedSprite2D.animation = "idle"

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
		rotation = clamp(start_rotation + horizontal_drag_distance * 0.0025, -0.785, 0.785)


func _process(delta):
	if dragging == true:
		if speed <= speed_cap:
			speed += acceleration
		if $AnimatedSprite2D.animation != "accelerate":
			$AnimatedSprite2D.play("accelerate")
	elif speed > 0:
		speed -= acceleration * deceleration_rate
		if $AnimatedSprite2D.animation != "decelerate":
			$AnimatedSprite2D.play("decelerate")
	
	var direction = Vector2(0, -1).rotated(rotation)
	velocity = direction * speed
	velocity.y += gravity
	move_and_slide()
	position = position.clamp(Vector2(75, upper_border), Vector2(screen_size.x - 75, screen_size.y - 75))
	if position.y > upper_border:
		velocity = direction * speed
	else: 
		scroll.emit(direction * speed)
