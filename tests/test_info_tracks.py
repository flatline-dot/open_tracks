import sys
#sys.path.append('C:\\Users\\stolypinskij_gv\\source\\repos\\flatline-dot\\open_track')
#print(sys.path)
from ..app import create_app
from time import sleep



def test_read_info_tracks():
    app.App()
    app.StartPage.check_con()

    request = app.commands['check_request']
    com = app.comports_status['COM2']['serial_instance']

    com.write(request)

    response = app.InfoTracks.info_tracks_read(com)
    print(response)
    assert len(response) >= 1924
    assert response[-1] == 3 and response[-2] == 16
    assert response[-3] != 16
    assert not com.in_waiting
