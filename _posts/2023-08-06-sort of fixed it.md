Something changed between windows 10 and 11 that broke my convoluted setup for using this thing.

Problem: Jekyll wants you to name your posts with the date plus the slug and I can't be bothered to do all that. I can however be bothered enough to try to make a script that does.  The python scripting part was easy but then there's another problem.

Problem 2: You can't just double-click a python file.  You can make a batch file do it though.  Now there's a new problem.

Problem 3: The batch file opens a stupid extra cmd prompt window.  You can solve that by making a fucking visual basic script to run the command as a ??? powershell object ??? using wshell or something.  But then there's a new problem.

Problem 4: You have to make a shortcut to point to the vbs file.  But that no longer works on windows 11 and the error message is totally unhelpful, so...

---

I scrapped all that and decided to try using nuitka to turn the python script into an executable so I can double click that, and...

It makes a batch file to run the exe because you have to set up the environment variables to point to anaconda python (because the windows-app-store version of python is garbage that must be avoided at all costs.)

So I'm back where I started. I have a double-clickable thing I can put on my desktop that names the file apropriately for jekyll to use it.  I just have to deal with an extra command prompt window.  Hmm, maybe I will look into using vbs again... ugh

just in case I ever need to do that I'm keeping this here:

    -CreateObject("Wscript.Shell").Run "newpost.cmd",0,True

