from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from models import User, db


class UserSchema(SQLAlchemyAutoSchema):

    full_name = fields.Method("get_full_name")

    class Meta:
        model = User
        load_instance = True    # allows deserialization
        include_fk = True       # To include foreign Key
        # fields = ["id", "username"]
        sqla_session = db.session

    
    def get_full_name(self, obj):
        return f"{obj.id} - {obj.username}"
