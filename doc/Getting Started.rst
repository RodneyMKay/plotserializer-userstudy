Getting Started
===============

Installation
------------
Install Plot Serializer by running

.. code-block:: python

    pip install plot-serializer


Serializing your first plot
---------------------------
We will serialize an example matplotlib plot that we have created as follows:

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt

    np.random.seed(19680801)

    X = np.round(np.linspace(0.5, 3.5, 100), 3)
    Y1 = 3 + np.cos(X)
    Y2 = 1 + np.cos(1 + X / 0.75) / 2
    Y3 = np.round(np.random.uniform(Y1, Y2, len(X)), 3)

    fig1 = plt.figure(figsize=(7.5, 7.5))
    ax = fig1.add_axes([0.2, 0.17, 0.68, 0.7], aspect=1)

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


We create a ``Serializer`` object with the figure:

.. code-block:: python

    from plot_serializer.serializer import Serializer

    s = Serializer(fig1)

Optionally, we add some metadata:

.. code-block:: python

    s.plot.id = plotids.figure_ids[0]
    s.plot.axes[0].xunit = "second"
    s.plot.axes[0].yunit = "meter"
    s.add_custom_metadata({"date_created": "11.08.2023"}, s.plot)

and then export to a JSON string:

.. code-block:: python

    json_object = s.to_json()

Finally, we can save the JSON string into a file:

.. code-block:: python

    with open("test_plot.json", "w+") as outfile:
        outfile.write(json_object)


Deserializing a plot from JSON
------------------------------

To deserialize the plot from a JSON file created with the ``Serializer``, we run

.. code-block:: python

    from plot_serializer.deserializer import Deserializer

    ds = Deserializer()
    fig = ds.json_to_matplotlib("test_plot.json")

    fig.show()