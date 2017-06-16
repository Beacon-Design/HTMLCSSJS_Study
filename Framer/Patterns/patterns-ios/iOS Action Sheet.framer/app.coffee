# Flow
flow = new FlowComponent
	backgroundColor: "#1199EE"

# Initialize screen
flow.showNext(screenA)

# On screen click show actionSheet
more.onClick (event, layer) ->	
	flow.showOverlayBottom(actionSheet)

# Hide actionSheet when clicked
actionSheet.onClick (event, layer) ->
	flow.showPrevious()

