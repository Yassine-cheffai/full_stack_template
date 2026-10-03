from sqladmin import Admin, ModelView

from db.schema import engine, User

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.first_name, User.last_name]

def setup_admin(app) -> None:
    """
    Set up admin interface
    """
    admin = Admin(app, engine)
    admin.add_view(UserAdmin)

