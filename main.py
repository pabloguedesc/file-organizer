import os
import time
from utils.file_utils import *
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        pass

    @staticmethod
    def on_modified(event):
      # verificando existência do arquivo
        if os.path.isdir(event.src_path):
            return
        if is_code_file(event) == True:
            path_to_folder = create_folder("code")
            move_file(event, path_to_folder)
            return
        elif is_text_file(event) == True:
            path_to_folder = create_folder("text")
            move_file(event, path_to_folder)
            return
        elif is_pdf_file(event) == True:
            path_to_folder = create_folder("pdf")
            move_file(event, path_to_folder)
            return
        elif is_mp3_file(event) == True:
            path_to_folder = create_folder("audio")
            move_file(event, path_to_folder)
            return
        elif is_image_file(event) == True:
            path_to_folder = create_folder("images")
            move_file(event, path_to_folder)
            return
        elif is_video_file(event) == True:
            path_to_folder = create_folder("videos")
            move_file(event, path_to_folder)
            return
        elif is_doc_file(event) == True:
            path_to_folder = create_folder("word-documents")
            move_file(event, path_to_folder)
            return
        elif is_spreadsheet_file(event) == True:
            path_to_folder = create_folder("spreadsheets")
            move_file(event, path_to_folder)
            return
        elif is_presentation_file(event) == True:
            path_to_folder = create_folder("presentation-files")
            move_file(event, path_to_folder)
            return
        elif is_executable_file(event) == True:
            path_to_folder = create_folder("executable-files")
            move_file(event, path_to_folder)
            return

    @staticmethod
    def on_deleted(event):
        pass

    @staticmethod
    def on_moved(event):
        pass


file_change_handler = Handler()
observer = Observer()
os.chdir("C:\\Users\\pablo\\Downloads")
print(os.getcwd())
observer.schedule(file_change_handler, os.getcwd(), recursive=False,)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
