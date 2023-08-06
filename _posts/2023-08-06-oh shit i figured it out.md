So the vbs script just needed the full path lol.

Here it is from the top:

I want to edit in vim.

I don't want to have to name the file because that involves formatting the date correctly as well as formatting the slug without any bad characters.

So I have a python file that does that part, touches the file, and then tells vim to open it.

Python on windows is such a frickin mess now that we're stuck using anaconda.  So we have to have a virtual environment activated. Gone are the days when python on windows just meant installing it from python.org and using it.  You must setup your environment correctly and make sure your shell has the conda environment activated.

So I went to an anaconda console and did a ``pip install -U nuitka`` and crossed my fingers. Nuitka wheel built okay.

Then I told nuitka to turn my 'newpost.py' script into an executable: ``python -m nuitka newpost.py`` succeeded, and thankfully it produced not only the newpost.exe but also the newpost.bat which would be required to run the exe with the environment variables set up correctly to point to the anaconda python.

Double clicking the newpost.bat did indeed run the newpost.exe which did indeed pop up the tkinter simpledialog needed to input a title for the post slug.  I thought I would just deal with the old stupid cmd.exe but then I tried one last time with the visual basic script so that windows shell would run the batch file (invisibly) instead of windows command prompt (in a console).

I guess the only thing that changed from windows 10 to 11 was that the vbs script needed the full path.  It used to work like this:

    CreateObject("Wscript.Shell").Run "newpost.cmd",0,True

but now it works like this:

    CreateObject("Wscript.Shell").Run "c:\Users\user\Documents\GitHub\dustractor.github.io\newpost.cmd",0,True

Cool. Now all I have to do is re-do the vim autocommand to autocommit after I save one of these things and it'll be back to normal.
