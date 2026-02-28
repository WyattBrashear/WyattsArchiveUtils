print("hello world")
"""
!EOF
---
!DIRECTORY|source_dir
!PATH|source_dir/runfile
!FILE_PAYLOAD|1476
"""
python3 meow.py
"""
!EOF
---
!DIRECTORY|source_dir/directory
!PATH|source_dir/directory/hello
!FILE_PAYLOAD|3829
"""
This is a text file for data testing in WAM
"""
!EOF
---
