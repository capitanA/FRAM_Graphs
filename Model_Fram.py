import xml.etree.ElementTree as ET
from tkinter import filedialog
from Fram_Shapes import *
from Helper import edge_detector
import networkx as nx
import ipdb


class Fram:
    def __init__(self):
        self.hexagons = list()

    def model_upload(self, root, r, flag_func_NO=False):
        self.G = nx.MultiGraph()
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file")
        # self.xfmv_path = root.filename
        xml_root = ET.parse(root.filename)
        xml_root = xml_root.getroot()
        for function in xml_root.iter("Function"):
            for element in function:
                if element.tag == "IDNr":

                    func_number = int(element.text)
                elif element.tag == "IDName":
                    func_name = element.text
            out_text = self.get_out_text(xml_root, func_number)

            """ if this flage is true the function should be shown with their numbers otherwise just name would be shown """
            if flag_func_NO:
                name = str(func_number) + " - " + func_name
            else:
                name = func_name
            id = func_number
            x = float(function.attrib["x"]) + 250
            y = float(function.attrib["y"]) + 150
            aspects = Aspects(outputs=Aspect(o_name="O", x=x, out_text=out_text, y=y, r=r),
                              controls=Aspect(o_name="C", x=x, y=y, r=r),
                              times=Aspect(o_name="T", x=x, y=y, r=r),
                              inputs=Aspect(o_name="I", x=x, y=y, r=r),
                              preconditions=Aspect(o_name="P", x=x, y=y, r=r),
                              resources=Aspect(o_name="R", x=x, y=y, r=r))

            # is_end = (aspects.outputs.out_text == 0)

            hexagon = Hexagon(id=id, name=name, x=x, y=y, hex_aspects=aspects, connected_aspects=[])
            self.hexagons.append(hexagon)
        for hexagon in self.hexagons:
            self.add_connectors(xml_root, hexagon)
        self.create_model_graph()
        return self.hexagons

    def create_model_graph(self):
        for hexagon in self.hexagons:

            self.G.add_node(hexagon.id, name=hexagon.name)
            for connected_aspect in hexagon.connected_aspects:
                aspect_in = connected_aspect.aspect_in.o_name
                edge_attributes = edge_detector(aspect_in)

                self.G.add_edge(hexagon.id, connected_aspect.hex_in_num, I=edge_attributes[0], P=edge_attributes[1],
                                T=edge_attributes[2],
                                C=edge_attributes[3], R=edge_attributes[4],
                                value=connected_aspect.text)
        # print(self.G.edges)
        self.hexagons.clear()

    def get_out_text(self, xml_root, func_number):
        # f_num = -1
        # out_text = ""
        res = []
        for o in xml_root.iter("Output"):
            f_num = -1
            out_text = ""
            for element in o:
                if element.tag == "IDName":
                    out_text = element.text
                if element.tag == "FunctionIDNr":
                    f_num = int(element.text)
                if f_num == func_number:
                    res.append(out_text)

        if res:
            return res
        else:
            return []

    def get_hexagon(self, id):
        for hexagon in self.hexagons:
            if hexagon.id == id:
                return hexagon

    def add_connectors(self, xml_root, hexagon):
        for item in ["Input", "Precondition", "Time", "Resource", "Control"]:
            for element in xml_root.iter(item):
                output_text = ""
                for items in element:
                    if items.tag == "IDName":
                        output_text = items.text
                    elif items.tag == "FunctionIDNr":
                        hex_in_number = items.text

                if output_text in hexagon.hex_aspects.outputs.out_text:
                    aspect_connector = AspectConnector(
                        aspect_in=getattr(self.get_hexagon(int(hex_in_number)).hex_aspects, item.lower() + "s"),
                        aspect_out=hexagon.hex_aspects.outputs, text=output_text,
                        hex_in_num=hex_in_number)
                    hexagon.connected_aspects.append(aspect_connector)
