# <b>Directory Files Reorganize</b>

## <b>Objective</b> 

<p>The software objective is to reorganize images, documents, executables, compressed files and of media in a directory,
separating them in specific folders for each file type.</p>
<p>I believe the logic of that project is simple, I was want to practice my Python develop skills, DRY and do a 
clean code, I tried to make a simple code for every one who to have basic knowledge at developing can do read, 
understand my code and contribute if they see anything can be improved.</p>

## <b>Functionalities</b>
<p>First, you can execute the software in project directory on executable file named: <b>"directory_files_reorganize.exe"</b></p>
<p>The below image is software main window, opened after execute:</p>
<img src="resources/main_window.png">

### Buttons
<li><b>Choose a directory to reorganize:</b> This button do open folder event, where you can choose the directory to 
reorganize;</li>

<i>Function: chooseDirectoryToReorganize()</i>

<li><b>Reorganize:</b> After choose a folder, this button be available to interact, onclick reorganize every file 
in directory to specific folder of him type;</li>

<i>Function: reorganizeFiles()</i>

<li><b>Rollback:</b> After reorganize successful, this button be available to interact, onclick rollback
the moving that have been does, putting the files back in original directory;</li>

<i>Function: rollbackMoves()</i>
