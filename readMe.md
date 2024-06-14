Supplementary material for the paper(s)
 - __Part 1:__ [`CatalogBank: A Structured and Interoperable Catalog Dataset with a Semi-Automatic Annotation Tool DocumentLabeler for Engineering System Design`](ADD LINK OF THE PAPER HERE)  
 __Abstract:__ In the realm of document engineering and Natural Language Processing (NLP), the integration of digitally born catalogs into product design processes presents a novel avenue for enhancing information extraction and interoperability. This paper introduces CatalogBank, a dataset developed to bridge the gap between textual descriptions and other data modalities related to engineering design catalogs. We utilized existing information extraction methodologies to extract product information from PDF-based catalogs to use in downstream tasks to generate a baseline metric. Our approach not only supports the potential automation of design workflows but also overcomes the limitations of manual data entry and non-standard metadata structures that have historically impeded the seamless integration of textual and other data modalities. Through the use of DocumentLabeler, an open-source annotation tool adapted for our dataset, we demonstrated the potential of CatalogBank in supporting diverse document-based tasks such as layout analysis and knowledge extraction. Our findings suggest that CatalogBank can contribute to document engineering and NLP by providing a robust dataset for training models capable of understanding and processing complex document formats with relatively less effort using the semi-automated annotation tool DocumentLabeler.

 - Part 2: **In preparation**

 ### Table of Content
    1. [Folder Structure](#folder-structure)
    2. [Catalogs](#catalogs)
    3. [Geometries](#geometries)
    4. [Graph](#graphs)
    5. [Images](#images)
    6. [Request Full Dataset Access](#request-full-dataset-access)

__Note:__ The content relevant to DocumentLabeler is in a separate repository. Please click the [link](https://www.github.com/bankh/DocumentLabeler) to access the repository.

 ### __1. Folder Structure__
 ```
 CatalogBank/
   ├── Catalogs/
   │    ├── Thorlabs/
   │    │   └── OptoMechanics_v21
   │    │       ├── _DocumentLabeler
   │    │       ├── _pdfs        
   │    │       ├── _images
   │    │       └── readMe.md       
   │    ├── McMasterCarr/
   │    │   (SAME structure as Thorlabs/OptoMechanics_v21)
   │    │   
   │    │   ...
   │    │   
   │    ├── Company X/
   │    │   (SAME AS Thorlabs)
   │    ├── Tools/
   │    └── readMe.md
   ├── Geometries/
   │    (Will be available in the future as Part 2 of CatalogBank)
   ├── Images/
   │    (Will be available in the future as Part 2 of CatalogBank)
   ├── Graphs/
   │    (Will be available in the future as Part 2 of CatalogBank)
   ├── Tools/
   │    └── readMe.md
   └── readMe.md
 ```
### __2. Catalogs/__: 
    Contains subfolders for each catalog source (e.g., Thorlabs, Grainger, Newark, Tools). Each subfolder can have its own [readMe.md](./Catalogs/readMe.md) file to describe the contents and any specifics related to that catalog.  

### __3. Geometry/__: 
    Stores files related to geometric data. Include a [readMe.md](./Geometry/readMe.md) file to describe the types of geometries, their format, and a data library.  

### __4. Image/__: 
    Contains image files. A [readMe.md](./Image/readMe.md) file should explain the image data, their format, and a data library.  

### __5. Graph/__: 
    Stores graphical data or visualizations. The [readMe.md](./Graph/readMe.md) file should provide details about these graphs.  

### __6. Tools/__: 
    Contains scripts or tools related to processing the data in CatalogBank. The [readMe.md](./Tools/readMe.md) file should describe each tool and its purpose.  

### __readMe.md__: 
    The main readMe file at the root of the repository should provide an overview of the entire CatalogBank, including a description of each subfolder and instructions for users. Each main sub-folders has its own readMe files to elaborate on the details of the associated folder.  

### Request Full Dataset Access
In this repository, the shared content is partial (10-50 pages per catalog). In order to request access to the full dataset for educational purposes ({}@{}.edu email address is required), please fill out the following [Google Form](https://your-google-form-link).

Once your request is approved, you will receive an email with access instructions.

### Cite
Please cite associated paper (and the respective papers of the methods used) if you use this dataset in your own work:

__Part 1:__ [`CatalogBank: A Structured and Interoperable Catalog Dataset with a Semi-Automatic Annotation Tool DocumentLabeler for Engineering System Design`](ADD LINK OF THE PAPER HERE)  
```
@article{,
    author = {Bank, H.S. and Herber, D.R.},
    title = "{}",
    conference = {ACM Document Engineering},
    volume = {},
    number = {},
    pages = {},
    year = {2024},
    month = {August},
    issn = {},
    doi = {},
    url = {},
    eprint = {},
}
```
__Part 2:__
```
@article{,
    author = {Bank, H.S. and Herber, D.R.},
    title = "{}",
    journal = {},
    volume = {},
    number = {},
    pages = {},
    year = {},
    month = {},
    issn = {},
    doi = {},
    url = {},
    eprint = {},
}
```

