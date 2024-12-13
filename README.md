# README.md

## CiteByBigName

**CiteByBigName** is a small tools designed to help us find papers that cite a given paper (via DOI) and identify authors of those citing papers who are fellows of prestigious organizations such as IEEE, ACM, AAAS, and AAAI.

<del>When we want to boast about our achievements to others, we can use this as a tool, haha.</del>

### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/citebybigname.git
   cd citebybigname
   pip install -r requirements.txt
   ```
2. Run the script with the following command:
   ```bash
   python citebybigname.py -d <DOI> [-f <fellowship>] [--json]
   ```
   For example:
   ```bash
   python citebybigname.py -d 10.1234/56789 -f IEEE ACM
   ```

3. Output
    - Human-Readable Format:
        ```
        ---------------------------------
        CiteBy: Title of the Citing Paper
        BigName: Author Name
        Fellowship: {'IEEE_FELLOW', 'ACM_FELLOW'}
        Fellowship Info: [Fellowship Details]
        JSONL Format:
        ```
    - jsonl format (with `--json`)
        ```json
        {
            "citeby": {
                "title": "Title of the Citing Paper",
                "authors": ["Author Name"],
                "year": 2023,
                "venue": "Conference Name",
                "DOI": "10.1234/56789"
            },
            "bigname": {
                "name": "Author Name",
                "fellow": ["IEEE_FELLOW", "ACM_FELLOW"],
                "fellow_info": [Fellowship Details]
            }
        }
        {
            "citeby": {
                "title": "Title of the Citing Paper",
                "authors": ["Author Name"],
                "year": 2023,
                "venue": "Conference Name",
                "DOI": "10.1234/56789"
            },
            "bigname": {
                "name": "Author Name",
                "fellow": ["IEEE_FELLOW", "ACM_FELLOW"],
                "fellow_info": [Fellowship Details]
            }
        }
        ```

### Acknowledgments

[Semantic Scholar](https://api.semanticscholar.org/api-docs/#tag/Paper-Data): 

Thanks to Semantic Scholar for providing a free and powerful API for academic research.

[Academic Awards Repository](https://github.com/xiaohk/academic-awards)

Thanks to xiaohk for maintaining the repository containing lists of fellows from IEEE, ACM, AAAS, and AAAI.