# mmcif_pdbx

This repository houses the dictionaries used by the wwPDB for the
maintaining the archive.

There are two dictionaries in use at this time:

1. mmcif\_pdbx\_v5\_next.dic is the internal dictionary in use by the
wwPDB deposition system. This dictionary also contains extensions currently
under development.

2. mmcif\_pdbx\_v50.dic is the dictionary used to support the public archive. 

The dictionaries are created by appending the different components
(header, base, extensions) use the script `scripts/Build.sh` using as
an argument the basename of the dictionary
(e.g. mmcif\_pdbx\_v5_next).  A Makefile is provided at the top level
as well.

