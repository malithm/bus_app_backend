@app.route("/")
def hello_world():
    return "Welcome to API"

@app.route("/users")
def users_list():
    users = User.query.all()
    return jsonify(users_schema.dump(users))

@app.route("/user", methods=["POST"])
def create_user():
    print("route....", request)
    username = request.json.get("username", "")
    email = request.json.get("email", "")
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user)

@app.route("/user/<int:user_id>", methods=["GET"])
def user_detail(user_id):
    user = User.query.get(user_id)
    return user_schema.jsonify(user)

@app.route("/user/<int:user_id>", methods=["PATCH"])
def update_user(user_id):
    username = request.json.get("username", "")
    email = request.json.get("email", "")
    user = User.query.get(user_id)
    user.username = username
    user.email = email
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user)

@app.route("/user/<int:user_id>/", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)