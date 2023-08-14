from flask import Flask, render_template, request, url_for
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://<user>:<password>@cluster0.vyape0e.mongodb.net/")
db = client["Fauna"]
collection_bird = db["Birds"]
collection_bird_categories = db['Bird_Categories']

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    
    bird_types = []
    
    #Get all Bird Categories
    birdTypes = collection_bird_categories.find()
    for type in birdTypes:
        bird_types.append(type)
    
    return render_template("index.html", bird_types = bird_types)

@app.route("/about", methods=['GET', 'POST'])
def about():
    
    return render_template("about.html")

@app.route("/faq", methods=['GET', 'POST'])
def faq():
    
    return render_template("faq.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    
    return render_template("contact.html")

@app.route("/birds", methods=['GET', 'POST'])
def getBirds():
    
    all_birds = []
    # Get all birds in the Bird Collection
    allBirds = collection_bird.find()
    for bird in allBirds:
        all_birds.append(bird)
            
    return render_template("birds.html", all_birds = all_birds)

@app.route("/birds/<birdname>", methods=['GET', 'POST'])
def getBirdTypes(birdname):

    birdType = []
    
    # Get all birds in the Bird Collection
    for bird in collection_bird.find({"Category": birdname}):
        birdType.append(bird)
        
    return render_template("bytype.html", all_birds = birdType)
    

@app.route("/insects", methods=['GET', 'POST'])
def getInsects():
    
    return render_template("insects.html")

@app.route("/mammals", methods=['GET', 'POST'])
def getMammals():
    
    return render_template("mammals.html")

@app.route("/reptiles", methods=['GET', 'POST'])
def getReptiles():
    
    return render_template("reptiles.html")

@app.route("/searchBirds", methods=['GET', 'POST'])
def searchBirds():
    
    # searchquery = request.args.get('search')
    searchquery = request.values.get("search")
    
    all_birds = []
    # Get all birds in the Bird Collection
    for bird in collection_bird.find({"$regex": searchquery}):
        all_birds.append(bird)
    
    return render_template("searchBird.html", all_birds = all_birds)

if __name__ == "__main__":
    app.run(debug=True)
