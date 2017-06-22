import webbrowser

class Movieclass():
    def __init__(self, mtitle, mstoryline, mimg, myoutube):
        self.title = mtitle
        self.story = mstoryline
        self.poster_image_url = mimg
        self.trailer_youtube_url = myoutube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
