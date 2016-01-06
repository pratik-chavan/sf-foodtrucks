#!flask/bin/python
from app import app
if __name__ == '__main__':
    app.run()
    if not app.debug and os.environ.get('HEROKU') is None:
        import logging
        from logging.handlers import RotatingFileHandler
        file_handler = RotatingFileHandler('tmp/sanfran-food-trucks.log', 'a', 1 * 1024 * 1024, 10)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('sanfran-food-trucks startup')

    if os.environ.get('HEROKU') is not None:
        import logging
        stream_handler = logging.StreamHandler()
        app.logger.addHandler(stream_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('sanfran-food-trucks startup')
