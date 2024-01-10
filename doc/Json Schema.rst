The complete Json Schema of PlotSerializer
==========================================

This is the complete Json-Schema definition for the data format plot-serializer is using:

.. code-block:: json

    {
        "$defs": {
            "Axis": {
                "properties": {
                    "label": {
                        "anyOf": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "default": null,
                        "title": "Label"
                    },
                    "scale": {
                        "anyOf": [
                            {
                                "const": "linear"
                            },
                            {
                                "const": "logarithmic"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "default": null,
                        "title": "Scale"
                    }
                },
                "title": "Axis",
                "type": "object"
            },
            "Bar": {
                "properties": {
                    "name": {
                        "title": "Name",
                        "type": "string"
                    },
                    "height": {
                        "title": "Height",
                        "type": "number"
                    },
                    "color": {
                        "title": "Color",
                        "type": "string"
                    }
                },
                "required": [
                    "name",
                    "height",
                    "color"
                ],
                "title": "Bar",
                "type": "object"
            },
            "BarPlot": {
                "properties": {
                    "type": {
                        "const": "bar",
                        "title": "Type"
                    },
                    "title": {
                        "anyOf": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "default": null,
                        "title": "Title"
                    },
                    "y_axis": {
                        "$ref": "#/$defs/Axis"
                    },
                    "bars": {
                        "items": {
                            "$ref": "#/$defs/Bar"
                        },
                        "title": "Bars",
                        "type": "array"
                    }
                },
                "required": [
                    "type",
                    "y_axis",
                    "bars"
                ],
                "title": "BarPlot",
                "type": "object"
            },
            "Line": {
                "properties": {
                    "color": {
                        "anyOf": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "default": null,
                        "title": "Color"
                    },
                    "thickness": {
                        "anyOf": [
                            {
                                "type": "number"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "default": null,
                        "title": "Thickness"
                    },
                    "linestyle": {
                        "anyOf": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "default": null,
                        "title": "Linestyle"
                    },
                    "label": {
                        "anyOf": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "default": null,
                        "title": "Label"
                    },
                    "datapoints": {
                        "items": {
                            "$ref": "#/$defs/Vec2F"
                        },
                        "title": "Datapoints",
                        "type": "array"
                    }
                },
                "required": [
                    "datapoints"
                ],
                "title": "Line",
                "type": "object"
            },
            "PiePlot": {
                "properties": {
                    "type": {
                        "const": "pie",
                        "title": "Type"
                    },
                    "title": {
                        "anyOf": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "default": null,
                        "title": "Title"
                    },
                    "slices": {
                        "items": {
                            "$ref": "#/$defs/Slice"
                        },
                        "title": "Slices",
                        "type": "array"
                    }
                },
                "required": [
                    "type",
                    "slices"
                ],
                "title": "PiePlot",
                "type": "object"
            },
            "Plot2D": {
                "properties": {
                    "type": {
                        "const": "2d",
                        "title": "Type"
                    },
                    "title": {
                        "anyOf": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "default": null,
                        "title": "Title"
                    },
                    "x_axis": {
                        "$ref": "#/$defs/Axis"
                    },
                    "y_axis": {
                        "$ref": "#/$defs/Axis"
                    },
                    "lines": {
                        "items": {
                            "$ref": "#/$defs/Line"
                        },
                        "title": "Lines",
                        "type": "array"
                    },
                    "points": {
                        "items": {
                            "$ref": "#/$defs/Point2D"
                        },
                        "title": "Points",
                        "type": "array"
                    }
                },
                "required": [
                    "type",
                    "x_axis",
                    "y_axis",
                    "lines",
                    "points"
                ],
                "title": "Plot2D",
                "type": "object"
            },
            "Point2D": {
                "properties": {
                    "position": {
                        "$ref": "#/$defs/Vec2F"
                    },
                    "color": {
                        "anyOf": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "default": null,
                        "title": "Color"
                    },
                    "size": {
                        "anyOf": [
                            {
                                "type": "number"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "default": null,
                        "title": "Size"
                    }
                },
                "required": [
                    "position"
                ],
                "title": "Point2D",
                "type": "object"
            },
            "Slice": {
                "properties": {
                    "size": {
                        "title": "Size",
                        "type": "number"
                    },
                    "radius": {
                        "anyOf": [
                            {
                                "type": "number"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "default": null,
                        "title": "Radius"
                    },
                    "offset": {
                        "anyOf": [
                            {
                                "type": "number"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "default": null,
                        "title": "Offset"
                    },
                    "name": {
                        "anyOf": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "default": null,
                        "title": "Name"
                    },
                    "color": {
                        "anyOf": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "default": null,
                        "title": "Color"
                    }
                },
                "required": [
                    "size"
                ],
                "title": "Slice",
                "type": "object"
            },
            "Vec2F": {
                "properties": {
                    "x": {
                        "title": "X",
                        "type": "number"
                    },
                    "y": {
                        "title": "Y",
                        "type": "number"
                    }
                },
                "required": [
                    "x",
                    "y"
                ],
                "title": "Vec2F",
                "type": "object"
            }
        },
        "properties": {
            "title": {
                "anyOf": [
                    {
                        "type": "string"
                    },
                    {
                        "type": "null"
                    }
                ],
                "default": null,
                "title": "Title"
            },
            "plots": {
                "default": [],
                "items": {
                    "discriminator": {
                        "mapping": {
                            "2d": "#/$defs/Plot2D",
                            "bar": "#/$defs/BarPlot",
                            "pie": "#/$defs/PiePlot"
                        },
                        "propertyName": "type"
                    },
                    "oneOf": [
                        {
                            "$ref": "#/$defs/PiePlot"
                        },
                        {
                            "$ref": "#/$defs/Plot2D"
                        },
                        {
                            "$ref": "#/$defs/BarPlot"
                        }
                    ]
                },
                "title": "Plots",
                "type": "array"
            },
            "metadata": {
                "additionalProperties": {
                    "anyOf": [
                        {
                            "type": "integer"
                        },
                        {
                            "type": "number"
                        },
                        {
                            "type": "string"
                        }
                    ]
                },
                "default": {},
                "title": "Metadata",
                "type": "object"
            }
        },
        "title": "Figure",
        "type": "object"
    }