#! /usr/bin/env python

"""
2015-03-06
Deltares
Arno Kockx

To create this file the original version of the CSDMS BMI Python Language Binding (file bmi.py) from https://github.com/csdms/bmi-python/blob/master/bmi/bmi.py was extended so that it can be used in OpenDA.

The following changes were made:
1. All grid information functions have been merged into the Bmi class, so that different variables within the same model can have different grids.
2. Added function get_grid_type to get the grid type for a given variable.
3. Added function save_state to ask the model to save its state to disk.
4. Added comments. Where the original version of the CSDMS BMI Python Language Binding was ambiguous, the information from http://csdms.colorado.edu/wiki/BMI_Description and common sense were used to fill in most of the gaps.
"""

from abc import ABCMeta, abstractmethod


class BmiGridType(object):
    """
    Enumeration with grid types.
    """

    UNKNOWN = 0
    UNIFORM = 1
    RECTILINEAR = 2
    STRUCTURED = 3
    UNSTRUCTURED = 4


class Bmi(object):
    """
    Interface (abstract base class) for a model that implements the CSDMS BMI (Basic Model Interface).
    """

    __metaclass__ = ABCMeta

    """
    Model Control Functions
    """

    @abstractmethod
    def initialize(self, filename):
        """
        Initialize the model.

        Input parameters:
        File filename: path and name of the configuration file for the model.
        """
        raise NotImplementedError

    @abstractmethod
    def update(self):
        """
        Update the model to the next time step.
        """
        raise NotImplementedError

    @abstractmethod
    def update_until(self, time):
        """
        Update the model until the given time.

        Input parameters:
        double time: time in the units and epoch returned by the function get_time_units.
        """
        raise NotImplementedError

    @abstractmethod
    def update_frac(self, time_frac):
        """
        ???

        Input parameters:
        double time_frac: ???
        """
        raise NotImplementedError

    @abstractmethod
    def save_state(self, destination_directory):
        """
        Ask the model to write its complete internal current state to one or more state files in the given directory.
        Afterwards the given directory should only contain the state files and nothing else.

        Input parameters:
        File destination_directory: the directory in which the state files should be written.
        """
        raise NotImplementedError

    @abstractmethod
    def finalize(self):
        """
        Finalize the model.
        """
        raise NotImplementedError

    """
    Model Information Functions
    """

    @abstractmethod
    def get_component_name(self):
        """
        Return value:
        String: identifier of the model.
        """
        raise NotImplementedError

    @abstractmethod
    def get_input_var_names(self):
        """
        Return value:
        List of String objects: identifiers of all input variables of the model.
        """
        raise NotImplementedError

    @abstractmethod
    def get_output_var_names(self):
        """
        Return value:
        List of String objects: identifiers of all output variables of the model.
        """
        raise NotImplementedError

    """
    Variable Information Functions
    """

    @abstractmethod
    def get_var_type(self, long_var_name):
        """
        Input parameters:
        String long_var_name: identifier of a variable in the model.

        Return value:
        String: data type of the values of the given variable, e.g. Numpy datatype string.
        """
        raise NotImplementedError

    @abstractmethod
    def get_var_units(self, long_var_name):
        """
        Input parameters:
        String long_var_name: identifier of a variable in the model.

        Return value:
        String: unit of the values of the given variable. Return a string formatted using the UDUNITS standard from Unidata.
        """
        raise NotImplementedError

    @abstractmethod
    def get_var_rank(self, long_var_name):
        """
        Input parameters:
        String long_var_name: identifier of a variable in the model.

        Return value:
        Integer: number of dimensions of the given variable.
        """
        raise NotImplementedError

    @abstractmethod
    def get_var_size(self, long_var_name):
        """
        Input parameters:
        String long_var_name: identifier of a variable in the model.

        Return value:
        Integer: total number of values contained in the given variable, e.g. gridCellCount.
        """
        raise NotImplementedError

    @abstractmethod
    def get_var_nbytes(self, long_var_name):
        """
        Input parameters:
        String long_var_name: identifier of a variable in the model.

        Return value:
        ???: ???
        """
        raise NotImplementedError

    @abstractmethod
    def get_start_time(self):
        """
        Return value:
        double: start time of the model in the units and epoch returned by the function get_time_units.
        """
        raise NotImplementedError

    @abstractmethod
    def get_current_time(self):
        """
        Return value:
        double: current time of the model in the units and epoch returned by the function get_time_units.
        """
        raise NotImplementedError

    @abstractmethod
    def get_end_time(self):
        """
        Return value:
        double: end time of the model in the units and epoch returned by the function get_time_units.
        """
        raise NotImplementedError

    @abstractmethod
    def get_time_step(self):
        """
        Return value:
        double: duration of one time step of the model in the units returned by the function get_time_units.
        """
        raise NotImplementedError

    @abstractmethod
    def get_time_units(self):
        """
        Return value:
        String: unit and epoch of time in the model. Return a string formatted using the UDUNITS standard from Unidata.
        """
        raise NotImplementedError

    """
    Variable Getter and Setter Functions
    """

    @abstractmethod
    def get_value(self, long_var_name):
        """
        Input parameters:
        String long_var_name: identifier of a variable in the model.

        Return value:
        Numpy array of values in the data type returned by the function get_var_type: all values of the given variable.
        """
        raise NotImplementedError

    @abstractmethod
    def get_value_at_indices(self, long_var_name, inds):
        """
        Input parameters:
        String long_var_name: identifier of a variable in the model.
        List of Lists of integers inds: each nested List contains one index for each dimension of the given variable,
                                        i.e. each nested List indicates one element in the multi-dimensional variable array,
                                        e.g. [[0, 0, 0], [0, 0, 1], [0, 15, 19], [0, 15, 20], [0, 15, 21]] indicates 5 elements in a 3D grid.

        Return value:
        Numpy array of values in the data type returned by the function get_var_type: one value for each of the indicated elements.
        """
        raise NotImplementedError

    @abstractmethod
    def set_value(self, long_var_name, src):
        """
        Input parameters:
        String long_var_name: identifier of a variable in the model.
        Numpy array of values src: all values to set for the given variable.
        """
        raise NotImplementedError

    @abstractmethod
    def set_value_at_indices(self, long_var_name, inds, src):
        """
        Input parameters:
        String long_var_name: identifier of a variable in the model.
        List of Lists of integers inds: each nested List contains one index for each dimension of the given variable,
                                        i.e. each nested List indicates one element in the multi-dimensional variable array,
                                        e.g. [[0, 0], [0, 1], [15, 19], [15, 20], [15, 21]] indicates 5 elements in a 2D grid.
        Numpy array of values src: one value to set for each of the indicated elements.
        """
        raise NotImplementedError

    """
    Grid Information Functions
    """

    @abstractmethod
    def get_grid_type(self, long_var_name):
        """
        Input parameters:
        String long_var_name: identifier of a variable in the model.

        Return value:
        BmiGridType type of the grid geometry of the given variable.
        """
        raise NotImplementedError

    @abstractmethod
    def get_grid_shape(self, long_var_name):
        """
        Only return something for variables with a uniform, rectilinear or structured grid. Otherwise raise ValueError.

        Input parameters:
        String long_var_name: identifier of a variable in the model.

        Return value:
        List of integers: the sizes of the dimensions of the given variable, e.g. [500, 400] for a 2D grid with 500x400 grid cells.
        """
        raise NotImplementedError

    @abstractmethod
    def get_grid_spacing(self, long_var_name):
        """
        Only return something for variables with a uniform grid. Otherwise raise ValueError.

        Input parameters:
        String long_var_name: identifier of a variable in the model.

        Return value:
        List of doubles: the size of a grid cell for each of the dimensions of the given variable, e.g. [width, height] for a 2D grid cell.
        """
        raise NotImplementedError

    @abstractmethod
    def get_grid_origin(self, long_var_name):
        """
        Only return something for variables with a uniform grid. Otherwise raise ValueError.

        Input parameters:
        String long_var_name: identifier of a variable in the model.

        Return value:
        List of doubles: the coordinate of the grid origin for each of the dimensions of the given variable. For a 2D grid this must be the lower left corner of the grid.
        """
        raise NotImplementedError

    @abstractmethod
    def get_grid_x(self, long_var_name):
        """
        Only return something for variables with a rectilinear, structured or unstructured grid. Otherwise raise ValueError.

        Input parameters:
        String long_var_name: identifier of a variable in the model.

        Return value:
        Numpy array of doubles: x coordinate of grid cell center for each grid cell, in the same order as the values returned by function get_value.
                         For a rectilinear grid: x coordinate of column center for each column.
        """
        raise NotImplementedError

    @abstractmethod
    def get_grid_y(self, long_var_name):
        """
        Only return something for variables with a rectilinear, structured or unstructured grid. Otherwise raise ValueError.

        Input parameters:
        String long_var_name: identifier of a variable in the model.

        Return value:
        Numpy array of doubles: y coordinate of grid cell center for each grid cell, in the same order as the values returned by function get_value.
                         For a rectilinear grid: y coordinate of row center for each row.
        """
        raise NotImplementedError

    @abstractmethod
    def get_grid_z(self, long_var_name):
        """
        Only return something for variables with a rectilinear, structured or unstructured grid. Otherwise raise ValueError.

        Input parameters:
        String long_var_name: identifier of a variable in the model.

        Return value:
        Numpy array of doubles: z coordinate of grid cell center for each grid cell, in the same order as the values returned by function get_value.
                         For a rectilinear grid: z coordinate of layer center for each layer.
        """
        raise NotImplementedError

    @abstractmethod
    def get_grid_connectivity(self, long_var_name):
        """
        Only return something for variables with an unstructured grid. Otherwise raise ValueError.

        Input parameters:
        String long_var_name: identifier of a variable in the model.

        Return value:
        ???
        """
        raise NotImplementedError

    @abstractmethod
    def get_grid_offset(self, long_var_name):
        """
        Only return something for variables with an unstructured grid. Otherwise raise ValueError.

        Input parameters:
        String long_var_name: identifier of a variable in the model.

        Return value:
        ???
        """
        raise NotImplementedError
