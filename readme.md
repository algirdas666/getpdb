Program Database File Downloader
================================
Utility for downloading Microsoft public symbol server Program Database
files (.pdb) written in Python.

Created to replace other laughably bad standalone approaches to this.

Usage
-----
```
getpdb.py <PE-file> [<PDB-output>]
```

To download a public symbol server PDB file for a given PE file, supply
its name as the first argument and it will be downloaded to the current
directory. Optionally, specify the name yourself and it will be
downloaded there.

Requirements
------------
This script requires at least Python 3.6 and the `pefile` and
`requests` libraries.
```
pip install pefile requests
```

License
-------
This script is licensed under the terms of the GNU General Public License v3.0.