# pdfjoin

## Overview

A simple Python tool to merge multiple PDF files in bulk, organized by subdirectories.  
Logs processing details and outputs merged files for each folder found under a target directory.  

## Description

`pdfjoin` is a command-line utility that allows you to merge PDF files contained in subdirectories under a given input directory.  
Each subdirectory's PDFs are sorted in natural order (descending), merged into a single PDF, and written to an output directory.  
The tool is especially useful for organizing and processing bulk-scanned documents, invoices, or chapters into unified PDFs.  

**Features:**
- Recursively detects subdirectories under an input folder
- Merges all `.pdf` files in each subdirectory
- Automatically creates output folders if they don't exist
- Outputs logs to a file for later auditing
- Sorts files using `natsort` for natural sorting (e.g., 1, 2, 10 instead of 1, 10, 2)

## Demo

```bash
input_dir/
├── clientA/
│   ├── 01.pdf
│   └── 02.pdf
└── clientB/
    ├── 03.pdf
    └── 01.pdf

# Outputs:
dist/
├── clientA/
│   └── merged.pdf
└── clientB/
    └── merged.pdf
```


## VS.

| Feature               | pdfjoin | Other Tools |
|----------------------|---------|-------------|
| CLI interface         | ✅       | ✅           |
| Merge by subfolders   | ✅       | ❌           |
| Logging               | ✅       | ❌           |
| Natural sort          | ✅       | ❌           |
| Fully offline         | ✅       | ❌ (some GUI tools require internet) |

## Requirement

- Python >= 3.7
- pip

### Dependencies

- [pypdf](https://pypi.org/project/pypdf/)  
- [natsort](https://pypi.org/project/natsort/)  
- [setuptools](https://pypi.org/project/setuptools/)  

## Usage

```python
from pdfjoin import pdf_join

pdf_join(
    input_dir='your/input/path/',
    output_dir='your/output/path/',             # optional, default is 'dist/'
    marged_file_name='merged.pdf',              # optional, default is 'merged.pdf'
    log_file_name='pdf-join.log'                # optional, default is 'pdf-join.log'
)
```

## Install

```bash
pip install pdfjoin
```

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)  

## Author

[pootaro.suzuki](https://github.com/dev-pootaro)  
