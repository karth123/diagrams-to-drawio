import sys
import pydot
import xml.etree.ElementTree as ET
import json
import re

def dot_to_mxgraph(dot_file_content):
    graph = dot_file_content
    mx_file = ET.Element('mxfile',{
        "host": "app.diagrams.net", "agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0", "etag":"FpzXfj3-j3l9qCAOajA5", "version":"24.4.15", "type":"device"
    })
    diagram = ET.SubElement(mx_file,'diagram',{
        "name": "Page-1",
        "id": "v7eHjkcJA2HYL1TbYpuy"
    })
    mx_graph_model = ET.SubElement(diagram,'mxGraphModel', {
            "dx": "1575", "dy": "924", "grid": "1", "gridSize": "10", "guides": "1",
            "tooltips": "1", "connect": "1", "arrows": "1", "fold": "1", "page": "1",
            "pageScale": "1", "pageWidth": "1169", "pageHeight": "827", "math": "0", "shadow": "0"
        })
    root = ET.SubElement(mx_graph_model, 'root')
    mx_cell_0 = ET.SubElement(root, 'mxCell', id="0")
    mx_cell_1 = ET.SubElement(root, 'mxCell', id="1", parent="0")

    # Nodes
    new_url_base = "https://github.com/karth123/diagrams_natviz/blob/master/resources/"
    for object in graph['objects']:
        if 'pos' in object:
            old_image_url = object['image']
            # Split the file path by the "resources" word
            split_path = old_image_url.split("resources")
            append_path = split_path[1].replace("\\", "/").strip("/")

            mx_cell = ET.SubElement(root, 'mxCell', {
                "id": object['name'],
                "value": object['label'],
                "style": f"shape=image;image={new_url_base}{append_path}?raw=True",
                # "style": f"shape=image;image={object['image']}",
                "vertex": "1",
                "parent": "1"
            })

            position = object['pos']
            x, y = re.split(pattern=',', string=position)

            mx_geometry = ET.SubElement(mx_cell, 'mxGeometry', {
                "x": x,
                "y": y,
                "width": "70",
                "height": "95",
                "as": "geometry"
            })
        
    # Edges

    for edge in graph['edges']:
        mx_cell = ET.SubElement(root, 'mxCell',{
                                "id": f"edge{edge['_gvid']+1}",
                                "style": "edgeStyle=orthogonalEdgeStyle;",
                                "edge": "1",
                                "parent": "1",
                                "source": graph['objects'][edge['tail']]["name"],
                                "target": graph['objects'][edge['head']]["name"],

        })
        mx_geometry = ET.SubElement(mx_cell, 'mx_Geometry',{
            "relative":"1",
            "as": "geometry"
        })
        array = ET.SubElement(mx_geometry, 'Array', {
            "as": "points"
        })
        edge_points = edge['pos'].split(' ')[1:-1]
        unique_edge_points = []
        seen = set()
        for point in edge_points:
            if point not in seen:
                unique_edge_points.append(point)
                seen.add(point)
        for point in unique_edge_points:
            x, y = point.split(',')
            ET.SubElement(array, 'mxPoint', {
                "x": x,
                "y": y
            })
    return (ET.tostring(mx_file, encoding='unicode'))


def test_dot_to_mxgraph(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    xml_output = dot_to_mxgraph(data)
    
    # Print the XML output for verification
    return xml_output
    
    # You can add more verification logic here, such as checking specific elements in the output XML



