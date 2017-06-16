# Function

layerA = new Layer
layerB = new Layer
layerB.x = 300

x = 12

layerB.onClick ->
    layerA.rotation = layerA.rotation + 10
    x = x + 1 
    print x

#--------------------------------------------

layerC = new Layer
    x: 0
    y: 300
    width: 60
    height: 60
    backgroundColor: "lightblue"
layerD = new Layer
    x: 300
    y: 300
    width: 60
    height: 60
    backgroundColor: "lightgreen"

ac = (layer, num) ->
    layer.rotation = layer.rotation + num
    layer.width = layer.width + num
    layer.height = layer.height + num
layerD.onClick ->
	ac(layerC, 5)