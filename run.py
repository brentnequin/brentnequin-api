from app import create_app, db

def run():

    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)

if __name__ == "__main__":
    run()