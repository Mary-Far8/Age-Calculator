# Age Calculator App

A simple desktop app built with Python's built-in `tkinter` GUI library that converts an age in years into months, days, and weeks.

## Features
- Enter an age in years
- Click "calculate age" to see the equivalent in months, days, and weeks
- Decorative image shown at the top

## How it works
- `age` (a `StringVar`) links the Entry box to a plain Python value.
- `calc()` converts the typed years into months (`*12`), days (`*365`), and weeks (`days // 7`), then shows all three in a popup.
- Uses `Pillow` (`PIL`) to load and resize the decorative image.

## ⚠️ Known issues — fix before running
1. **Hardcoded image path**, which will crash on any other machine:
```python
pil_image = Image.open(r"c:\Users\user\Downloads\unnamed (1).png")
```
Fix: put the image in this project folder (e.g. `age_image.png`) and change the line to:
```python
pil_image = Image.open("age_image.png")
```

2. **No input validation** — typing anything non-numeric (or leaving it empty) in the age box will crash the app when "calculate age" is clicked, since `int(the_age_value)` isn't wrapped in a try/except like the other apps in this portfolio.

## Requirements
- Python 3.x
- `tkinter` (included with most standard Python installations)
- `Pillow` — install with `pip install Pillow`

## Run it
```bash
python age_calculator_app.py
```

## Possible next steps
- Fix the hardcoded image path (see above)
- Add try/except input validation, matching the pattern used in the other calculator apps
- Account for leap years in the days calculation
