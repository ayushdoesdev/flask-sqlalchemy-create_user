from flask import Blueprint, request
from db_init import db, User
from schema_init import UserSchema

user_page = Blueprint('user_page', __name__, url_prefix="/users")


@user_page.route("/")
def list_user():
    users = db.session.execute(db.select(User).order_by(User.id)).scalars().all()
    user_schema = UserSchema(many=True)
    user_list = user_schema.dump(users)
    return user_list


@user_page.route("/create_schema", methods=['POST'])
def create_user_schema():
    if request.method == 'POST':
        try:
            user = UserSchema().load(request.form)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            return {
                "status": 400,
                "error": str(e)
            }
        return {
            "status": 200
        }
    return {
        "message": "Incorrect method"
    }


@user_page.route("/create", methods=['POST'])
def create_user():
    if request.method == 'POST':
        user = User(
            username = request.form['username'],
            email = request.form['email']
        )
        db.session.add(user)
        db.session.commit()
        return {
            "status": 200
        }
    return {
        "message": "Incorrect method"
    }