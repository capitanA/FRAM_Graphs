from Model_Fram import Fram
from Scenario_Fram import SceneEvent
from tkinter import filedialog
# import GMatch4py as gm
import networkx
import ipdb
import tkinter as tks


class Start:
    def __init__(self):

        self.graphs = []
        self.counter = 1

    def model_upload(self):
        fram_upload.model_upload(root, 40)

    def scene_upload(self):

        events = SceneEvent()

        filename_scene = filedialog.askopenfilename(initialdir="/", title="Select the file for Scenario")
        if filename_scene.endswith('.csv'):
            filetype = 'csv'
            with open(filename_scene, newline='') as csv_file:
                events.scene_upload(fram_upload, csv_file, filetype, self.graphs, self.counter)
        elif filename_scene.endswith('.xml'):
            filetype = 'xml'
            events.scene_upload(fram_upload, filename_scene, filetype, self.graphs, self.counter)
        self.counter = +1

    def compare_graphs(self):
        ged = gm.GraphEditDistance(1, 1, 1, 1)
        result = ged.compare([self.graphs[0], self.graphs[1]], None)
        print(result)


if __name__ == "__main__":
    fram_upload = Fram()
    start = Start()
    root = tk.Tk()
    root.geometry("300x300")

    upload_icon = tk.PhotoImage(file="./Images/upload.png")
    BUTTON_MODEL = tk.Button(root, cursor="plus",
                             compound=tk.LEFT,
                             image=upload_icon,
                             padx=15,
                             text="     Model",
                             font=("Helvetica", 15),
                             fg="black",
                             height=38,
                             width=114,
                             command=start.model_upload,
                             anchor="w")

    BUTTON_SCENE = tk.Button(root, cursor="plus",
                             compound=tk.LEFT,
                             image=upload_icon,
                             padx=15,
                             text="     Scenario",
                             font=("Helvetica", 15),
                             fg="black",
                             height=38,
                             width=114,
                             command=start.scene_upload,
                             anchor="w")
    BUTTON_compare_graph = tk.Button(root, cursor="plus",
                                     compound=tk.LEFT,
                                     image=upload_icon,
                                     padx=15,
                                     text=" Compare Graphs",
                                     font=("Helvetica", 15),
                                     fg="black",
                                     height=38,
                                     width=114,
                                     command=start.compare_graphs,
                                     anchor="w")
    BUTTON_MODEL.pack(anchor="w")
    BUTTON_SCENE.pack(anchor="w")
    BUTTON_compare_graph.pack(anchor="w")

    tk.mainloop()
