from spear_disney import create_app


if __name__ == '__main__':
    spear_app = create_app()
    # spear_app.run(debug=spear_app.config.get('DEBUG'), threaded=spear_app.config.get('THREADED'),
    #               port=spear_app.config.get('PORT'), host=spear_app.config.get('HOST'))
    spear_app.run()
else:
    gunicorn_app = create_app()
