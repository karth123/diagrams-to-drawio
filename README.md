# diagrams-to-drawio
This is a python script which can be used to convert cloud architecture diagrams generated by the diagrams python library into .drawio files which can be opened in the draw.io visual editor.

## Limitations

- Currently the script supports only diagrams library cloud architecture diagrams which uses Graphviz under the hood. Other type of graphviz diagrams where the edges are not orthogonal splines are not currently supported
- Another issue is that edge handling from the png rendered by diagrams to drawio is imperfect because of the way Graphviz lays out orthogonal splines in contrast to drawio
- Another limitation is the lack of support for clustering or grouping.

## How to use the script

Since the diagrams library is hosted locally while .drawio files are meant to be opened in the online visual editor, there will be an issue with icon rendering if the script is used out of the box. You need to host the icons to be remotely accessible while at the same time being able to maintain the file routing which the diagrams library uses because of how it imports the icons inside python code.

The best way to do this which I have discovered is to use the icons hosted by mingrammer in the diagrams repository or fork the repository on Github and use your own url base.

```python
# dot_to_mxgraph.py line 26

new_url_base = <add_your_url_base>
```

Replace `add_your_url_base` with the url_base of your hosted icons. Example: `https://github.com/mingrammer/diagrams/tree/master/resources/`

This script adds the query parameter `?raw=True` to render the raw content from GitHub. You can remove the parameter in line 37:  dot_to_mxgraph.py if you don't need it.

Once you configure the script to render icons properly, you can run the script after confirming you have the necessary requirements (The requirements for the diagrams library is sufficient)

The script will receive and execute python code. You can modify the script to read a python file which you have edited. You need to provide a file name to the script, and access to the diagrams python code

Run the script `diagrams_to_drawio.py` after writing the diagrams python code and providing access to it in the script.

## Writing the diagrams python code

The diagrams library renders python code into cloud architecture diagrams. You may follow the steps laid out in the example documentation in the diagrams library but this line of code is a must

```python
with Diagram('<Title of cloud architecture>', show=False, outformat=['png', 'dot'],file):
```

You need to specify the output format as dot or it will default to only png. Without the dot file, the script cannot run.

The project consists of two scripts, `dot_to_mxgraph.py` and `diagrams_to_drawio.py` . Both need to be in the root directory of the project and so does the Diagrams python file.

## Expected output

If all goes well, you should expect a png file of the cloud architecture to be generated in the root directory, along with a .dot file and a .drawio file of the same file name.

The .drawio file can be opened in the online visual editor draw.io
