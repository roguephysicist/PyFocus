PyFocus
==================================

A proof-of-concept Python program for identifying the active AF points in RAW files.

![](http://i.imgur.com/TiZjYMA.gif)

Working with large RAW files is extremely slow. Therefore, the program first extracts the `JPG` preview file embedded within the RAW file and loads it into the buffer. This avoids the need to writing an intermediate image file to disk. Then, the active AF points are extracted from the RAW file metadata. The active and inactive points are drawn onto a semi-transparent overlay, which is then composited onto the original image. The combined image is finally saved to disk.

The final image is reduced in size to save space and speed up processing. Currently, processing time is around ~1 second per RAW image on my mid-level system.

I have only tried this for the Pentax K-50 with good results. The AF point information for this camera is stored in `PentaxK50.py`. I attempted to include this information in the most intuitive and standardized way possible.


Requirements
----------------------------------

* python 3
* `sys`, `io`
* [`exiftool`](https://smarnach.github.io/pyexiftool/)
* [`rawkit`](https://rawkit.readthedocs.io/en/latest/)
* [`pillow`](http://python-pillow.org)


TODO:
----------------------------------

* fix for portrait orientation
* consider aggdraw instead of pillow
* pass arrays to functions


License
------------------------------------

Copyright 2017 Sean M. Anderson.

PyFocus is free software made available under the BSD-3-Clause License. For details please see the LICENSE file.
