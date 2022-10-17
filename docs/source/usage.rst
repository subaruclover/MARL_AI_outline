Usage
=====

.. _installation:

Installation
------------

To use Marl, first install it using pip:

.. code-block:: console

   (.venv) $ pip install marl

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``marl.get_random_ingredients()`` function:

.. autofunction:: marl.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`marl.get_random_ingredients`
will raise an exception.

.. autoexception:: marl.InvalidKindError

For example:

>>> import marl
>>> marl.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

