Pilotshoe
---------

This shoe aims to assist the blind is safely and independently navigating to any location. I am not blind, therfore, I made two assumptions when starting this project:

1. Just as a person with sight needs assistance when walking to a new location, walking navigation would be beneficial to a blind person. Even for known locations, it could provide an useful reference.
2. A blind person needs a way of knowing what objects are around them in order to prevent collisions.

Pilotshoe attempts to address these statements in two ways. First, Pilotshoe uses the Dragonboard's onboard GPS unit to provide auditory navigation to the user via headphones. In this implementation, GPS data is sent back to the phone via bluetooth since the Dragonboard 410c does not have a cellular connection. In another implementation, I could add auditory and cellular connection right into the device and make these devices as standalone units with no need of a cellphone. Secondly, the Pilotshoe has a servo with a rotating ultrasonic sensor that can detech up to 4.5 meters away mounted on the tip of a shoe. Hence the "shoe" part of the name. These sensor acts as a sort of radar to map out the distance objects are away from the user which allows the user to get a sense of thier environment and avoid collisions.

This system is by no means perfect, but I think it's a cool concept that could be improved upon.

This folder has a `main.py` which is triggered on login by the `.bashrc` script, and the script `post_ip` is put inside of `/etc/network/if-up.d/` and made executable (notice it isn't ending in .sh) and will post the device's IP address as soon as connected to wifi. This is for debugging (ssh) purposes.
