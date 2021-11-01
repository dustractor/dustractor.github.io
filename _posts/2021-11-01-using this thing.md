I'm trying to make some sort of a vim-plugin based system for posting to a github repo and letting jekyll do all the work.

So far, the friction has been always to have to name the file with the date-title and that's the last thing you want to do every time you decide to start typing some thoughts.

The solution is -- as usual -- the roundaboutiest af way possible since I use windows:

I have a shortcut on my desktop.  It points to a .vbs script that points to a .cmd script that points to a .py script that uses python's tkinter interface to the tcl scripting language, just to put up a gui with a single text field for entry of the title of the post.

Yes, you read that correctly, because this is windows, we had to get visual fucking basic involved.

This visual basic script saved in a file 'newpost.vbs':

    CreateObject("Wscript.Shell").Run "newpost.cmd",0,True

'newpost.cmd':

    @echo off
    pythonw newpost.py

'newpost.py':


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

---

But wait, there's more.

## That was just to get the text editor open for the file I am currently editing.


When I save this file, vim will (automatically do some stuff) post the shit online where github will (automatically do some stuff) and then in theory, it is available online as a nicely formatted document, hopefully viewable after having refreshed the page twenty or thirty times.

The relevant lines for ye olde vimrc:

    fun! DoAutoCommitGithubSite()
        echom "AUTOCOMMIT"
        call system(expand("~")."\\Documents\\username.github.io\\autocommit.cmd")
    endfun

    aug AutoCommitGithubSite
        au!
        au BufWritePost ~/Documents/username.github.io/*.md call DoAutoCommitGithubSite()
    aug END

(Reminder that the asterisk in a path in an autocommand can expand to multiple levels of folders deep.)

Oh and that 'autocommit.cmd' script is part of this whole contraption. Can't forget that:

    git add index.md _posts/*.md img/*.*
    git commit -m auto-foo
    git push
    


