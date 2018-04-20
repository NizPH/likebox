# Installation

* Copy the software to the desired location.
* Check that Python >= 3.5 is installed or [install it](https://www.raspberrypi.org/documentation/linux/software/python.md).
* Check that pip is installed or [install it](https://www.raspberrypi.org/documentation/linux/software/python.md).
* Run `pip install -r requirements.txt` from the software directory to install all Python dependancies.
* Create a symbolic link in the systemd services directory if you need to install the software as a service. From directory `/etc/systemd/system/multi-user.target.wants/` enter `ln -s /{installation_directory}/software/likebox.service likebox.service`
* Restart the PI.

