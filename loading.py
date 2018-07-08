from __future__ import print_function

import sys
import time

from pyspin.spin import Spin5, Spinner
def loading():
    # Choose a spin style.
    spin = Spinner(Spin5)
    print("Loading All Modules, Please wait ...")
    # Spin it now.
    for i in range(50):
        print(u"\r{0}".format(spin.next()), end="")
        sys.stdout.flush()
        time.sleep(0.1)

    print("Done :D ")