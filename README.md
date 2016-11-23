# Seamonsters Robot Code Template

Code for the JellyFISH!

There's a lot of extra code here. The `seamonsters` library is now permenantly being kept in the `SeamonstersTemplate` repository. And any robot code not tied to the 2016 competition (like the Project Stingray code) will be moved to the `SeamonstersDev` repository. We won't be updating this repository much any more, other than cleanup.

Deploy with `./deploy.sh` or `.\deploy.bat` (Windows). Test with `./test.sh` or
`.\test.bat` (Windows).

## Directory Structure

- `seamonsters/`: The seamonsters library code. It has its own documentation, in
    `seamonsters/docs/_build/html/index.html` (you can view it online
    [here](https://rawgit.com/Seamonsters-2605/CompetitionBot2016/seamonsters-template/seamonsters/docs/_build/html/index.html))
- `GRIP/`: GRIP files used in competition for image recognition.
- `Shooter/`: Code for the flywheels, intake motor, and "ShootController", which
    allows control of both.
- `tests/`: Created and used by pyfrc for tests.
- `robot.py`: The final robot, used in the 2016 competition and updated slightly
    since then.
- `stingray.py`: Project Stingray robot code.
- `stingray/`: Modules for the Project Stingray bot.
- `Vision.py`: Simple code that gets the center of the target from GRIP (when it
    works).
- `testBot.py`: Robot that is modified for testing various things.
- `holoBot.py`: Simple bot used for testing holonomic drives.
- `bTest.py`: Very simple bot that spins a single motor - used for testing
    Blender simulation.
- `deploy.bat` and `deploy.sh`: Windows and *nix versions of scripts for
    deploying code to robot.
- `fastdeploy.bat` and `fastdeploy.sh`: Deploy code without testing it.
- `test.bat` and `test.sh`: Scripts for testing robot code without needing an
    actual robot to deploy to.
