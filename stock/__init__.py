from flask import Flask

def create_app():
    app = Flask(__name__)

    from.views import main_views
    app.register_blueprint(main_views.bp)

    from .views import stock_views
    app.register_blueprint(stock_views.bp)

    return app
