# br8ness

**br8ness** is a simple brightness tool for linux. It will automatically detect the application that is currently in focus and adjust the brightness accordingly.

In our example, the brightness will be set to **180%** when the application in focus is whether **Terminator**, or **Visual Studio Code (Insiders)**, and **100%** otherwise.

## Installation

**Clone** the **repository**, and **install** the **libraries** listed in ***requirements.txt***

```bash
python3 -m pip install -r requirements.txt
```

## Usage

```bash
python3 br8ness.py
```

## Tips

Add it to your crontab to run on startup, by doing the following:

```bash
crontab -e

# This is an example, change the path to where you cloned the repository
@reboot /usr/bin/python3 ~/Documents/br8ness/src/br8ness.py
```

## Contributing

Feel free to contribute to this project, I'm open to suggestions and improvements.
