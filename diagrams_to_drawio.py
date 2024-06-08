import os
import graphviz
from dot_to_mxgraph import test_dot_to_mxgraph

def render_diagram_file_to_drawio_file(file, file_name):
    # Step 1: Read and execute the Python file content
    try:
            exec(file)
    except Exception as e:
        print(f"An error occurred while executing the file: {e}")
        return

    # Step 2: Read the .dot file content
    dot_file_path = f"{file_name}.dot"
    try:
        with open(dot_file_path, 'r') as file:
            dot_content = file.read()
    except Exception as e:
        print(f"An error occurred while reading the .dot file: {e}")
        return

    # Step 3: Render the .dot file to JSON format
    try:
        dot = graphviz.Source(dot_content, filename=file_name)
        json_file_path = dot.render(format='json0', filename=file_name).replace('\\', '/')
        print(f"JSON file created at: {json_file_path}")
    except Exception as e:
        print(f"An error occurred while rendering the .dot file: {e}")
        return

    # Step 4: Convert the rendered JSON to draw.io format using test_dot_to_mxgraph
    try:
        drawio_output = test_dot_to_mxgraph(json_file_path)

        # Write drawio output to an XML file
        xml_file_path = f"{file_name}.drawio"
        with open(xml_file_path, 'w') as xml_file:
            xml_file.write(drawio_output)
        print(f"Draw.io output written to XML file: {xml_file_path}")
        
    except Exception as e:
        print(f"An error occurred while converting to draw.io format: {e}")

    # Step 5: Clean up files except XML(.drawio) and PNG
    extensions = ['json0','dot']
    try:
        for ext in extensions:
            os.remove(f"{file_name}.{ext}")
    except Exception as e:
        print(f"An error occurred during cleanup: {e}")


