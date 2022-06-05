
# WhatsApp-Wisher

WhatsApp wishing bot using python


## Libraries

First you need to run this command

```bash
  pip install pyautogui
```

```bash
  pip install webbrowser
```

```bash
  pip install time
```
## Usage/Examples

```python
import os
import webbrowser as wb
import pyautogui as pg
import time

def browser():
    wb.open("http://web.whatsapp.com/")

def search():
    for i in range(1):
        pg.write("Good morning")
        time.sleep(0)
        pg.press("enter")

browser()
search()
```


## Run

To run this project run the command

```bash
  python3 main.py
```

## Authors

- [@alokdubey01](https://github.com/alokdubey01)


## License

[MIT](https://github.com/alokdubey01/WhatsApp-Wisher/blob/main/LICENSE)

