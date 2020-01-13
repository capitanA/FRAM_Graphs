from Model_Fram import Fram
from Scenario_Fram import SceneEvent
from tkinter import filedialog
import gmatch4py as gm
import networkx
import ipdb
import tkinter as tk
from tkinter import messagebox

counter = 0


class Start:
    def __init__(self):

        self.graphs = []
        self.counter = 0
        self.scene_events = None
        self.hexagons = None

    def model_upload(self):
        self.hexagons = fram_upload.model_upload(root, 40)

    def scene_upload(self):
        self.counter += 1

        events = SceneEvent()

        filename_scene = filedialog.askopenfilename(initialdir="/", title="Select the file for Scenario")
        if filename_scene.endswith('.csv'):
            filetype = 'csv'
            with open(filename_scene, newline='') as csv_file:
                self.scene_events = events.scene_upload(fram_upload, csv_file, filetype, self.graphs, self.counter)
        elif filename_scene.endswith('.xml'):
            filetype = 'xml'
            self.scene_events = events.scene_upload(fram_upload, filename_scene, filetype, self.graphs, self.counter)
        # if counter == 2:
        #     ipdb.set_trace()
        # print(self.graphs[0])

    def compare_graphs(self):
        ged = gm.GraphEditDistance(1, 1, 1, 1)
        result = ged.compare([self.graphs[0], self.graphs[1]], None)
        result_lbl.config(text=result)

    def reset(self):
        self.counter = 0
        print(self.hexagons)
        if self.graphs or self.scene_events or self.hexagons:
            self.graphs.clear()
            self.scene_events.clear()
            self.hexagons.clear()
            result_lbl.config(text="")
            messagebox.showinfo(message="reset is done successfuly ")
        else:
            messagebox.showinfo(message="it is already reseted ")
        # if self.graphs:
        #     self.graphs.clear()
        # if self.scene_events:
        #     self.scene_events.clear()
        # if self.hexagons:
        #     self.hexagons.clear()
        # if result_lbl:
        #     result_lbl.config(text="")
        # messagebox.showinfo("model and scenario reseted successfuly ")
        # if not self.graphs and not self.scene_events and not self.hexagons:
        #     messagebox.showinfo("it is already reseted ")


if __name__ == "__main__":
    fram_upload = Fram()
    start = Start()
    root = tk.Tk()
    root.geometry("300x300")

    upload_icon = tk.PhotoImage(file="./Images/upload.png")
    reset_icon = tk.PhotoImage(file="./Images/reset.png")
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

    Reset_Button = tk.Button(root, cursor="plus",
                             compound=tk.LEFT,
                             image=reset_icon,
                             padx=15,
                             text=" Reset",
                             font=("Helvetica", 15),
                             fg="black",
                             height=38,
                             width=114,
                             command=start.reset,
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

    result_lbl = tk.Label(root)
    BUTTON_MODEL.pack(anchor="w")
    BUTTON_SCENE.pack(anchor="w")
    BUTTON_compare_graph.pack(anchor="w")
    result_lbl.pack(anchor="w")
    Reset_Button.pack(anchor="w")

    tk.mainloop()
