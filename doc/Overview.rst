Overview
========

How Plot Serializer sees diagrams
---------------------------------

Plot Serializer uses its own data model for representing scientific diagrams.
It is strongly inspired by the `matplotlib figure anatomy <https://matplotlib.org/stable/gallery/showcase/anatomy.html)>`_.

``Plot`` is equivalent to Figure in matplotlib.
It contains one or more ``Axis`` objects ("subplots"), which in turn contain one or more ``Trace`` objects (lines, scatters, etc.).
