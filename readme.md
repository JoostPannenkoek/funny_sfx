# Random funny sound effect bullshi

## usage

Linux:

```bash
# make virtual env
python3 -m venv .venv

# get into that shit
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run script with default args in bg
nohup python funny_sfx.py >/dev/null 2>&1 &
```

Windows (cmd):
```cmd
# make virtual env
python -m venv .venv

# get into that shit
.venv\Scripts\activate.bat

# install dependencies
pip install -r requirements.txt

# run script with default args in bg
pythonw funny_sfx.py

```

## Argument Usage
```powershell
# play sound now
pythonw funny_sfx.py --now

# configure chance (every second a one in N chance to play rnd sound)
pythonw funny_sfx.py --chance 69420
```

## Configure for startup

Linux:

Add to crontab:
`@reboot /usr/bin/python3 /path/to/funny_sfx.py`

Windows:

Put a shortcut to:

`pythonw.exe funny_sfx.py`

inside:

`shell:startup`

This gives you invisible cross-platform random meme audio forever.
