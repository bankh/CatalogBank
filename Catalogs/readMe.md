### The Folder Structure and its Explanation in Catalog:
`./_DocumentLabeler` contains the `./_DocumentLabeler/DocumentLabeler` folder for importing non-annotated data directly into the DocumentLabeler tool for further processing. Users can also import other folders into DocumentLabeler.
The folder `./_DocumentLabeler/PICK` contains content processed with the PICK model. Users can utilize their own models and incorporate them into this `./_DocumentLabeler/` folder as `./_DocumentLabeler/Model/`.

`./_images` contains the JPG images of each page with bounding box objects (e.g., words, images, etc.). _ori images are the original images, and _ann images have the bounding boxes. Please note that these bounding boxes are not labeled as seen in the sample below.
The `_images` folder also contains TXT files for each page. The structure of the text data is as follows:

```
...
NAVIGATE  464  124  620  157  default
CATALOG   445  162  595  194  default
...
```
The first column contains the transcript, and the other four numbers are the coordinates of the bounding box. The last column contains the label. In the example above, since we don't have a label yet, it is highlighted by default.

`./_pdfs` consists of the individual pdf pages of the catalogs.
