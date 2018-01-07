Bellkor Algorithm
=================

All the Bellkor Module functionality can be viewed in the sections below:

Bellkor Algorithm
-----------------

Contains all the model functionality:

.. autoclass:: Bellkor.Algorithm.BellkorAlgorithm
    :members:

Base Model
----------

Contains all the Base Classes - used as the foundation for other items:

.. autoclass:: Bellkor.Base.BaseObject.Model
    :members:
    
.. autoclass:: Bellkor.Base.Generic.Generic
    :members:

Parameters:
-----------

Contains all the Model parameters / internal representations:

.. autoclass:: Bellkor.Parameters.Gradients.Gradients
    :members:
    
.. autoclass:: Bellkor.Parameters.LearningRates.LearningRates
    :members:
    
.. autoclass:: Bellkor.Parameters.Parameters.Parameters
    :members:
    
.. autoclass:: Bellkor.Parameters.Resgularisation.RegularisationRates
    :members:
    
.. autoclass:: Bellkor.Parameters.RowSettings.RowSettings
    :members:

Utils
-----

.. autofunction:: Bellkor.Utils.Decorators.test_method

.. autofunction:: Bellkor.Utils.Decorators.timeit

.. autofunction:: Bellkor.Utils.Decorators.timeit_debug

.. autoclass:: Bellkor.Utils.Exceptions.ModelValidationException
    :members:
    
.. autoclass:: Bellkor.Utils.Exceptions.ModelIterationException
    :members:
    
.. autoclass:: Bellkor.Utils.Exceptions.ModelRunException
    :members:
