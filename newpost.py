import pathlib,datetime,re,subprocess
import tkinter as tk
from tkinter import simpledialog

badchars= re.compile(r'[^A-Za-z0-9_. ]+|^\.|\.$|^ | $|^$')
badnames= re.compile(r'(aux|com[1-9]|con|lpt[1-9]|prn)(\.|$)')

def safe_name(s):
    name= badchars.sub('_', s)
    if badnames.match(name):
        name= '_'+name
    return name


root = tk.Tk()
root.withdraw()
_input = simpledialog.askstring(title="Post Title",prompt="Choose a title.")
slug = safe_name(_input)
t = datetime.date.today()
y = t.year
m = t.month
d = t.day
fname = f"{y}-{m:02}-{d:02}-{slug}.md"
targetdir = "_posts"
p = pathlib.Path(targetdir) / fname
p.touch()
subprocess.run(["c:\\Program Files\\Vim\\vim82\\gvim.exe",p])
