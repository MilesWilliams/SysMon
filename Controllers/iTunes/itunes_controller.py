import subprocess

artist = subprocess.getoutput("osascript -e 'tell application \"iTunes\" to artist of current track as string'")
track = subprocess.getoutput("osascript -e 'tell application \"iTunes\" to name of current track as string'")
state = subprocess.getoutput("osascript -e 'tell application \"iTunes\" to player state as string'")
currentvolume = subprocess.getoutput("osascript -e 'tell application \"iTunes\" to sound volume as integer'")


class ItunesController(object):

    def status(self):
        if state == "playing":
            print ("Itunes is: %s" % state)
            print ("Currently playing: '%s' by '%s'" % (track, artist))
        else:
            print ("Itunes it not playing, type 'itunes play' to start playing music")

    def play(self):
        if state == "paused":
            print ("Playing iTunes")
            subprocess.getoutput("osascript -e 'tell application \"iTunes\" to play'")
            print ("Currently playing: '%s' by '%s'" % (track, artist))
        else:
            print ("Itunes is currently playing")

    def pause(self):
        if(state == "playing"):
            print ("Pausing iTunes")
            subprocess.getoutput("osascript -e 'tell application \"iTunes\" to pause'")
            print ("iTunes paused")
        else:
            print ("iTunes is currently paused")

    def nsong(self):
        print("Skipping to next song")
        subprocess.getoutput("osascript -e 'tell application \"iTunes\" to next track'")
        print ("Currently playing: '%s' by '%s'" % (track, artist))

    def psong(self):
        print("Rewinding to previous song")
        subprocess.getoutput("osascript -e 'tell application \"iTunes\" to previous track'")
        self.status()

    def iquit(self):
        print ("Quitting iTunes")
        subprocess.getoutput("osascript -e 'tell application \"iTunes\" to quit'")

test = ItunesController()
test.nsong()
