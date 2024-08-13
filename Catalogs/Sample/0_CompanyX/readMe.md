### A Template of Catalog for Company X (Sample Company):
`./_DocumentLabeler` has the `./_DocumentLabeler/DocumentLabeler` folder to import non-annotated data directly to the DocumentLabeler tool for further processing. The users can import other folders to DocumentLabeler as well.  

`./_images` has the jpg images of each page with bounding boxed objects (e.g., words, images, etc.). `_ori` images are original images, and `_ann` ones are with the bounding boxes. Please remark that these bounding boxes are not labeled.  

The `_images` folder has .txt files for each page. The structure of the text data content is as follows:
```
NAVIGATE	464	124	620	157	default
CATALOG	445	162	595	194	default
...

```
The first column contains the transcript, and the other four numbers are the coordinates of the bounding box. The last column contains the label. Since we don't have a label yet, it is highlighted by default.

`./_pdfs` consists of the individual pdf pages of the catalogs.
