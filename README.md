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
