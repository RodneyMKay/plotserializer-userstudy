Getting Started
===============

Installation
------------
Install PlotSerializer by running

.. code-block:: bash

    pip install plot-serializer


Serializing your first plot
---------------------------
We will serialize an example matplotlib plot that we have created as follows:

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()

    np.random.seed(19680801)

    X = np.round(np.linspace(0.5, 3.5, 100), 3)
    Y1 = 3 + np.cos(X)
    Y2 = 1 + np.cos(1 + X / 0.75) / 2

    ax.set_xlim(0, 4)
    ax.set_ylim(0, 4)

    ax.tick_params(which="major", width=1.0, length=10, labelsize=14)
    ax.tick_params(which="minor", width=1.0, length=5, labelsize=10, labelcolor="0.25")

    ax.grid(linestyle="--", linewidth=0.5, color=".25", zorder=-10)

    ax.plot(X, Y1, c="C0", lw=2.5, label="Blue signal", zorder=10)
    ax.plot(X, Y2, c="C1", lw=2.5, label="Orange signal")

    ax.set_title("Example figure", fontsize=20, verticalalignment="bottom")
    ax.set_xlabel("TIME in s", fontsize=14)
    ax.set_ylabel("DISTANCE in m", fontsize=14)
    ax.legend(loc="upper right", fontsize=14)


Of particular interest are the two following lines:

.. code-block:: python

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()

To collect the data from the plot, we want to serialize, we first need to create a ``Collector`` object.
Specifically, since we're looking at matplotlib in this case, we need to create a ``MatplotlibCollector``.
The ``MatplotlibCollector`` also exposes a ``subplots()``-Method.
This way the ``Collector`` is able to capture everything you do with the returned objects.

In concrete terms, we replace the two lines above with the following code:

.. code-block:: python

    from plot_serializer.matplotlib.collector import MatplotlibCollector

    collector = MatplotlibCollector()
    fig, ax = plt.subplots()

Optionally, we can add some metadata to the resulting Json:

.. code-block:: python

    collector.add_custom_metadata("date_created", "10.01.2023")

Finally, get the resulting Json string, we can invoke the ``json()``-Method on the collector:

.. code-block:: python

    collector.json()

We can also write the plot to a file directly:

.. code-block:: python

    collector.write_json_file("test_plot.json")

Deserializing a plot from JSON
------------------------------

TODO
