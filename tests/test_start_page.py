import app.create_app as app
from time import sleep


def test_check_con():
    application = app.App()
    
    app.StartPage.check_con()
    app.StartPage.psi_mode()
    
    assert app.comports_status['COM2']['active']
    assert app.comports_status['COM2']['psi_mode']
    assert app.comports_status['COM2']['serial_instance'].port == "COM2"
    sleep(0.5)
    app.StartPage.default_set()
    assert not app.comports_status['COM2']['psi_mode']
