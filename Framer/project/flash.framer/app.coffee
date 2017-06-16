# 1. Show the "start" artboard, first.
flow = new FlowComponent
flow.showNext(overview)
flow.header = statusBar



back.placeBehind(statusBar)

# 2. Show "overview" when clicking on "start".
# start.onTap ->
# 	flow.showNext(overview)

# 3. Show the "menu" when clicking on the menu icon.
menuIcon.onTap ->
	flow.showOverlayLeft(menu)

flash = talkBGyou
talkBGme.visible = false

# flash = talkBGme
# talkBGyou.visible = false



# Flash
flash.states =
	stateX:
# 		backgroundColor: "#00AAFF"
		opacity: 1
		animationOptions: 
			curve: Bezier.easeIn
			time: 0.4
			delay: 0.8
	stateA:
# 		backgroundColor: "#00AAFF"
		opacity: 1
		animationOptions: 
			curve: Bezier.easeIn
			time: 0.4
	stateB:
# 		backgroundColor: "#00AAFF"
		opacity: 0
		animationOptions:
			curve: Bezier.easeOut
			time: 0.4
 
animation1 = flash.animate("stateX")
animation2 = flash.animate("stateB")
animation3 = flash.animate("stateA")
animation4 = flash.animate("stateB")

jorn.on Events.Tap, animation1.start
animation1.on Events.AnimationEnd, animation2.start
animation2.on Events.AnimationEnd, animation3.start
animation3.on Events.AnimationEnd, animation4.start

















# 4a. Show our chat with Jorn when clicking on his name.
jorn.onTap ->
	flow.showNext(chat)
	
	
jorn.on Events.Tap, (event) ->
	title.animate
		opacity: 0
		options:
			curve: Bezier.ease
			time: 0.2
	

# 4b. Return to previous artboard when clicking on the back arrows.
back.onTap ->
	flow.showPrevious()
	
	
back.on Events.Tap, (event) ->
	title.animate
		opacity: 1
		options: 
			curve: Bezier.easeIn
			time: 0.4
	
# Animation Chaining
# Talk1.animate
# 	backgroundColor: "lightblue"
# 	options: 
# 		curve: Bezier.ease
# 		time: 3
# Talk1.onAnimationEnd ->
# 	Talk1.animate
# 		backgroundColor: "gray"
# 		options: 
# 			curve: Bezier.ease
# 			time: 3