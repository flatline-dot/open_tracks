import app.create_app as app


def test_check_con():
    application = app.App()
    app.StartPage.check_con()
    assert app.comports_status['COM2']['active']
