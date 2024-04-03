from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/teksts")
def te():
    return render_template("teksts.html")

@app.route("/saraksts")
def saraksts():
    saraksts = ["Anna", "Katls", "Kartupelis"]
    bildes = ["https://artprojectsforkids.org/wp-content/uploads/2022/05/How-to-Draw-a-Girl.jpg","https://dans.lv/imgs/1gb-nami%C5%86%C5%A1-mini-roku-mazg%C4%81%C5%A1anas-pot-miniat%C5%ABras_1-image/143144.jpg","https://stemgeneration.org/wp-content/uploads/2018/03/Potato_Battery_Main.jpg"]
    kopejais_saraksts = [["Anna", "https://artprojectsforkids.org/wp-content/uploads/2022/05/How-to-Draw-a-Girl.jpg"], ["Katls", "https://dans.lv/imgs/1gb-nami%C5%86%C5%A1-mini-roku-mazg%C4%81%C5%A1anas-pot-miniat%C5%ABras_1-image/143144.jpg"], ["Kartupelis", "https://stemgeneration.org/wp-content/uploads/2018/03/Potato_Battery_Main.jpg"]]
    return render_template("saraksts.html", vardi = saraksts, bildes = bildes, garums = len(saraksts))


if __name__ == '__main__':
    app.run(port = 5000)

print("Sveiki!")