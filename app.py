from flask import Flask, render_template
import lyricsgenius, re

app = Flask(__name__)

@app.route('/')
def home():
    genius = lyricsgenius.Genius("LfRP3xS3m-0nF7XX_6UleJPWQxRA6_mv1XW55MnnS4AKZBqp2nwQp6gOnn_zi_GA")
    #song = genius.search_song("Money Trees", "Kendrick Lamar", get_full_info=False)
    #if genius != None:
        #title = song.title
        #artist = song.artist
        #lyrics = re.sub(r'^.*?(\[.*)', r'\1', song.lyrics, flags=re.DOTALL)
    #else:
        #title = "not found"
        #artist = "not found"
        #lyrics = "not found"
    #return(render_template("index.html", title=title, artist=artist, lyrics=lyrics))
    return(render_template("index.html"))

if __name__ == '__main__':
    app.run(debug=True)