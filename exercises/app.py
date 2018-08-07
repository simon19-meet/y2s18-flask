from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    player_list=["Messi","Neymar","Ter Stegen","Cavani","Griezman","Pogba"]
    for i in player_list:
        print(i)
    return render_template("index.html")

if __name__ == '__main__':
   app.run(debug = True)