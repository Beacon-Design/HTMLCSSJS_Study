function onRun(context) {

	var doc = context.document;
	var page = doc.currentPage();
	var layers = page.children();
	var layerNumber = 0; 

	for (var i=0; i<layers.count(); i++) {
		var layer = layers[i];
		if (layer.isLocked()) {
			layer.setIsLocked(false);
			layerNumber++;
		}
	}
	doc.showMessage(layerNumber+" layer unlocked !")
}