from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/about")
def about():
    return "Computer Science"

@app.route("/miscellaneous")
def miscellaneous():
    return jsonify({
        "favorite_animals":"cats",
        "last_update_date":"11/5/2026 AD",
        "current_skills":["Python","Flask","JavaScript","SQL"],
        "not_favorite_#":11
    })

characters = [
    {"id":1, "name":"John", "skill":['diplomacy']},
    {"id":2, "name":"Luke", "skill":['root']}
]
@app.route("/characters")
def characters():
    skill = request.args.get("skill")
    if skill:
        return jsonify([c for c in characters if skill in c["skill"]])
    return jsonify(characters)

# type myself later
app.route("/ideas", methods=["POST"])
def add_idea():
    data = request.get_json()
    ideas.append(data["text"])
    return jsonify(ideas), 201

@app.route("/ideas")
def get_ideas():
    return jsonify(ideas)
# done    

if __name__ == "__main__":
    app.run(debug=True)