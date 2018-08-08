from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home_page():
    likes_same_sport=False
    arr=["Messi","Neymar","Ter Stegen","Cavani","Griezman","Pogba"]
    if likes_same_sport:
        return render_template("index.html", player_list=arr,likes_same_sport=likes_same_sport)
    return render_template("index.html",likes_same_sport=likes_same_sport)

if __name__ == '__main__':
   app.run(debug = True)
