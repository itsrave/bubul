from bu.finder import LinkFinder
from bu.finder import ImageFinder
import signal
import time


class GracefulKiller:
    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.kill_now = True


if __name__ == '__main__':
    killer = GracefulKiller()
    while True:
        c = LinkFinder()
        c.start()
        if killer.kill_now:
            c.save()
            break

    print("I was killed gracefully :)")
