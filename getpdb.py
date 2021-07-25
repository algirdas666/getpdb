#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pefile
import requests
from sys import argv

if __name__ == '__main__':
  
  argc = len(argv)
  if argc not in [2, 3]:
    print('getpdb <file> [<output>]')
    exit(2)
  
  pe = pefile.PE(argv[1])
  
  # This thing does not acknowledge non-RSDS debug directories.
	# Not that Microsoft ever uses anything else.
  try:
    dbg_entry = pe.DIRECTORY_ENTRY_DEBUG[0].entry
    name = dbg_entry.PdbFileName.decode('utf-8')
    name = name[:4+name.index('.pdb')] # pefile/msft's fault
    
    guid = "%x%x%x%s%x" % (
      dbg_entry.Signature_Data1,        # unsigned int
      dbg_entry.Signature_Data2,        # unsigned short
      dbg_entry.Signature_Data3,        # unsigned short
      dbg_entry.Signature_Data4.hex(),  # char[8]
      dbg_entry.Age                     # unsigned int
    )
    guid = guid.upper()
  
  except:
    print('nopdb' if 'DIRECTORY_ENTRY_DEBUG' in pe.__dict__ else 'nodbg')
    raise
  
  url = 'http://msdl.microsoft.com/download/symbols/%s/%s/%s' % (
    name,
    guid,
    name
  )
  with requests.get(url, stream=True) as d:
    d.raise_for_status() # files often don't exist
    with open(argv[2] if argc == 3 else name, 'wb') as out_file:
      for part in d.iter_content(chunk_size=4096):
        out_file.write(part)
  
  print('have')
