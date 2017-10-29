function onRun(context) {

	var doc = context.document;
	var page = doc.currentPage();

	var layerNumber = 0; 

	var selection = context.selection;

	
	for (var i=0; i<selection.count(); i++){
		var layer = selection[i];

		layer.setIsLocked(true);
		layerNumber++;
	}
	// doc.showMessage(layerNumber+" layer locked !")

	



}