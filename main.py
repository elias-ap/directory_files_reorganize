import shutil
import os
import customtkinter as ttk
from tkinter import messagebox as mb


def chooseDirectoryToReorganize():
    global reorganized_directory_path
    reorganized_directory_path = ttk.filedialog.askdirectory()
    if os.path.isdir(reorganized_directory_path):
        move_files_button.configure(state='normal')


def createFolderIfNotExists():
    # CHECK IF HAVE A FOLDER WITH SAME NAME AS PRE CHOOSEN DESTINATION FOLDER
    for folder in destination_folder_list:
        if os.path.isdir(f'{reorganized_directory_path}/{folder}'):
            pass

        # IF NOT HAVE, CREATE TO PUT REORGANIZED FILES
        else:
            os.mkdir(f'{reorganized_directory_path}/{folder}')


def checkIfHaveFilesToReorganize(folder_files):
    for list in extensions_list:
        for extension in list:
            for file in folder_files:
                if extension in file:
                    return True


def moveFile(file, folder):
    try:
        shutil.move(f'{reorganized_directory_path}/{file}',
                    f'{reorganized_directory_path}/{destination_folder_list[folder]}')
        rollback_moves_button.configure(state='normal')
        move_files_button.configure(state='disabled')
    except shutil.Error:
        mb.showwarning('Error', f"""
        That {file} already exists in destination path:\n'
        {reorganized_directory_path}/{destination_folder_list[folder]}\n
        Rollbacking moves..
        """)
        rollbackMoves()


def reorganizeFiles():
    createFolderIfNotExists()
    directory_files = os.listdir(reorganized_directory_path)
    if checkIfHaveFilesToReorganize(directory_files):
        for file in directory_files:
            file_name, extension = os.path.splitext(file.lower())
            for extensions in extensions_list:
                if extension in extensions:
                    folder = extensions_list.index(extensions)
                    moveFile(file, folder)

        mb.showinfo('Successful', 'The choosed directory have been reorganized')
    else:
        mb.showinfo(message="Don't have files to reorganize in choosed folder")
        move_files_button.configure(state='disabled')


def rollbackMoves():
    for folder in destination_folder_list:
        folder_path = f'{reorganized_directory_path}/{folder}'
        folder_files = os.listdir(folder_path)
        for file in folder_files:
            shutil.move(f'{folder_path}/{file}', f'{reorganized_directory_path}')

    rollback_moves_button.configure(state='disabled')
    move_files_button.configure(state='disabled')


destination_folder_list = ['Images', 'Compressed', 'Documents', 'Executables', 'Media']
image_extension = ['.png', '.jpeg', '.ico', '.jfif']
compacted_extension = ['.zip', '.rar']
docs_extension = ['.docx', '.pdf', '.txt', '.doc(2)!']
executable_extension = ['.exe', '.bat', '.msi']
media_extension = ['.mp3', '.mp4', '.avi', '.mkv', '.wmv']
extensions_list = [image_extension, compacted_extension, docs_extension, executable_extension, media_extension]

# MAIN WINDOW CONFIGURATION
ttk.set_appearance_mode('dark')
window = ttk.CTk()
window.title('')
window.geometry('200x150')
window.eval('tk::PlaceWindow . center')
window.maxsize(200, 150)

# BUTTONS
choose_folder_button = ttk.CTkButton(window, text='Choose directory to reorganize', command=lambda: chooseDirectoryToReorganize())
choose_folder_button.pack(side='bottom', pady=10)

move_files_button = ttk.CTkButton(window, text='Reorganize', command=lambda: reorganizeFiles())
move_files_button.pack(side='bottom', pady=10)
move_files_button.configure(state='disabled')

rollback_moves_button = ttk.CTkButton(window, text='Rollback', command=lambda: rollbackMoves())
rollback_moves_button.pack(side='bottom', pady=10, before=choose_folder_button)
rollback_moves_button.configure(state='disabled')

window.mainloop()


