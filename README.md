# br8ness

**br8ness** is a simple brightness tool for linux. It will automatically detect the application that is currently in focus and adjust the brightness accordingly to all your connected monitors.

In our example, the brightness will be set to **180%** when the application in focus is in the environment variable **BR8NESS_LIST_OF_PROCESS**. Otherwise, it will be set to **100%**.

## Installation

**Clone** the **repository**, and **install** the **libraries** listed in ***requirements.txt***

```bash
python3 -m pip install -r requirements.txt
```

In your environment variables, add the following:

```bash
# Each processus name must be separated by a comma
BR8NESS_LIST_OF_PROCESS='processus_name_1,processus_name_2,processus_name_3'
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


You could also start it manually, in the background, by doing the following:

```bash
nohup python3 br8ness.py &
```

## Contributing

Feel free to contribute to this project, I'm open to suggestions and improvements.
