# Set up pagination
page = new PageComponent
	height: Screen.height
	width: Screen.width
	scrollVertical: false
	contentInset:
		right: 20

# Add cards to page component
cardA.parent = page.content
cardA.x = 20

cardB.parent = page.content
cardB.x = cardA.maxX + 20

cardC.parent = page.content
cardC.x = cardB.maxX + 20

page.updateContent()

# Change the dots when the page changes
dots = [dotA, dotB, dotC]
page.on "change:currentPage", ->
	for dot, i in dots
		if i is page.currentPage.index-1
			dot.opacity = 1
		else
			dot.opacity = 0.4