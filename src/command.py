from subprocess import call

import msgfunc as prnt

def refresh_all( xresources, wallpaper):
    prnt.prnt( '-n', 'Refreshing i3 and xrdb and setting wallpaper')
    call( ['xrdb', xresources])
    call( ['i3-msg', 'restart'])
    prnt.prnt( '-s', 'Done!')
