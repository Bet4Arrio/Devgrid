from app import app, db
import os 
if __name__ == "__main__":
    if not os.path.isfile('app/registration.db'):
        db.create_all()
    app.run()
