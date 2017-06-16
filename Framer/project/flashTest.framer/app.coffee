
layerBlue = new Layer
layerBlue.backgroundColor = "#00AAFF"


layerA = new Layer
layerA.backgroundColor = "#F5F5F5"
# layerA.visible = false
# Set multiple states at once 
layerA.states =
	stateX:
		backgroundColor: "#F5F5F5"
		opacity: 0
		animationOptions: 
			curve: Bezier.easeIn
			time: 0.5
			delay: 1
	stateA:
		backgroundColor: "#F5F5F5"
		opacity: 0
		animationOptions: 
			curve: Bezier.easeIn
			time: 0.5
	stateB:
		backgroundColor: "#F5F5F5"
		opacity: 1
		animationOptions:
			curve: Bezier.easeOut
			time: 0.5
 
animation1 = layerA.animate("stateX")
animation2 = layerA.animate("stateB")
animation3 = layerA.animate("stateA")
animation4 = layerA.animate("stateB")

animation1.start()
animation1.on Events.AnimationEnd, animation2.start
animation2.on Events.AnimationEnd, animation3.start
animation3.on Events.AnimationEnd, animation4.start

 
 
 
 
 
 
 
 
 
#  layerA.animate("stateA")

 
# On a click, go back and forth between states. 
# layerA.onTap ->
#     layerA.stateCycle("stateA", "stateB")