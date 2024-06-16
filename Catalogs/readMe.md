### Explanation of Catalog Data and Folder Organization
`./_DocumentLabeler` contains the `./_DocumentLabeler/DocumentLabeler` folder for importing non-annotated (only bounding boxes and transcripts without any labels --see Table 1b below) data directly into the DocumentLabeler tool for further processing.  
The folder `./_DocumentLabeler/PICK` contains content processed with the PICK model. Users can utilize their own models, and we suggest incorporating their custom models into this `./_DocumentLabeler/` folder as `./_DocumentLabeler/Model_Name/.`  
`./_images` contains the JPG images of each page with bounding box objects (e.g., words, images, etc.). _ori images are the original images, and _ann images have the bounding boxes. Please note that these bounding boxes are not labeled, as seen in the sample below.  
The `_images` folder also contains TXT files for each page. The structure of the text data is as follows:  
<table style="width:100%; text-align:center;">
  <tr>
    <td style="width:33.33%; text-align:center;"><img src="./Sample/McMasterCarr/_images/mcmaster-125_3378_10_ori.jpg" alt="Original Image" style="width:100%; margin: auto;"></td>
    <td style="width:33.33%; text-align:center;"><img src="./Sample/McMasterCarr/_images/mcmaster-125_3378_10_annoverlay.png" alt="Image with Bounding Boxes" style="width:100%; margin: auto;"></td>
    <td style="width:33.33%; text-align:center;"><img src="https://github.com/bankh/CatalogBank/assets/9688867/4d0fa4ea-5c2c-4286-b465-a65837edc3c5" alt="Screenshot of TXT File" style="width:100%; margin: auto;"></td>
  </tr>
  <tr>
    <td style="text-align:center;"><strong>a) Original Image from pdf without a Bounding Box</strong></td>
    <td style="text-align:center;"><strong>b) Image with Bounding Boxes (no label, only transcripts)</strong></td>
    <td style="text-align:center;"><strong>c) The content of .txt files for the coordinates of the bounding boxes and transcripts</strong></td>
  </tr>
</table>
The first column contains the transcript, and the other four numbers are the coordinates of the bounding box. The last column contains the label. In the example above, since we don't have a label yet, it is highlighted by default.  
`./_pdfs` consists of the individual pdf pages of the catalogs in case the users would like to utilize their own tools on these pages.  
