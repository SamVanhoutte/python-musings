# The NLTK (natural language toolkit) introduction

## Installation
To install NLTK, use the pip3 command:
```bash
pip3 install nltk
```

The NL Toolkit requires several dictionaries to be download (punkt being the most common one).  For that, the following snippet can be executed once in your python tool.  This will open a dialog box where several collections or dictionaries can be downloaded.  The SSL code ignores the SSL validation warning that blocks the download.

```python
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download()
```

