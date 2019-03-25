
import subprocess

def capture(command):
    proc = subprocess.Popen(command,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    out,err = proc.communicate()
    return out, err, proc.returncode

def test_song_url_missing():
    command = ['python3','uperation','sing','manifest','--song-url','song_url']
    out,err, exitcode = capture(command)
    assert exitcode == 2
    return

def test_study_id_missing():
    command = ['python3','uperation','sing','manifest','--study','study_id']
    out,err, exitcode = capture(command)
    assert exitcode == 2
    return

def test_study_wrong_study_song_url():
    command = ['python3','uperation','sing','manifest','--song-url','song_url','--study','study_id']
    out,err, exitcode = capture(command)
    assert exitcode == 1
    return