
+---------------------------------------+------------+------------+---------+
| Project                               | Created    | Updated    | Version |
+---------------------------------------+------------+------------+---------+
| Re-implementing the Bellkor Algorithm | 06/01/2018 | 07/01/2018 | 0.1.0   |
+---------------------------------------+------------+------------+---------+

Development
===========

Installing the Library
----------------------

The project has been built with Python 3.5.3 (64 bit), once installed open a command prompt and runt he following commands:

.. code-block:: python

    pip install . -U 

    OR

    pip install -e . [DEVELOPERS ONLY] - quick install / avoids having to install all the dependencies


Installing the development dependencies and retrieve the data:

.. code-block:: python
    
    pip install -e .[dev]


Installing the testing dependencies:

.. code-block:: python

    pip install -e .[test]

Installing the documentation dependencies / build documentation:

.. code-block:: python

    pip install -e .[docs]

Code Coverage
-------------

.. code-block:: python
    
    TODO

Contribution
------------

See the [Contribution](CONTRIBUTING.md) file.

Bump Version
------------

Easy bumping of a package version:

1.  ``` bumpversion --config-file .bumpversion.cfg major ``` - Example: 1.3.1 -> 2.0.0
2.  ``` bumpversion --config-file .bumpversion.cfg minor ``` - Example: 1.3.1 -> 1.4.0
3.  ``` bumpversion --config-file .bumpversion.cfg patch ``` - Example: 1.3.1 -> 1.3.2

Contribution
============

Found a bug? Have a new feature to suggest? Want to contribute changes to the codebase? Make sure to read this first.

Requesting a Feature
--------------------

To request new features that you would like to see via JIRA.

1.  Provide a clear and detailed explanation of the feature you want and why it is important to add. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset.

2.  Provide code snippets demonstrating the API you have in mind and illustrating the use cases of your feature. Of course, you do not need to write any real code at this point!

3.  If you are at all able, start writing some code. We always have more work to do than time to do it. If you can write some code, then that will speed the process along.

Pull Requests
-------------

Here's a quick guide:

1.  If your PR introduces a change in functionality, make sure you start by opening an issue on JIRA to discuss whether the modification should be done, and how to handle it. This will save you from having your PR closed down the road!

2.  Write the code. This is the hard part!

3.  Make sure any new function or class you introduce has proper docstrings. Make sure any code you touch still has up-to-date docstrings and documentation.

4.  Write tests. Your code should ideally have full unit test coverage. If you want to see your PR merged promptly, this is crucial.

5.  Run our test suite locally. It is easy: from the project folder, simply run ```pytest -c py.test.ini > pytest.log```

6.  Make sure all tests are passing

    *   We use PEP8 syntax conventions, but we are not dogmatic when it comes to line length. Make sure your lines stay reasonably sized. To make your life easier, we recommend running a PEP8 linter:
    *   Install PEP8 packages: ```pip install -e .[test]```
    *   Run a standalone PEP8 check: ```py.test --pep8 -m pep8 > pep8.log```
    *   You can automatically fix some PEP8 error by running: ```autopep8 -i -r .``` at the project level
    *   When committing, use appropriate, descriptive commit messages. Make sure that your branch history is not a string of "bug fix", "fix", "oops".
    *   All Pull Requests (PR's) need to be approved by another developer, embrace their feedback and update as required.

