
Metadata Specification
======================

This specification defines a way how to store all metadata needed
for test execution in plain text files close to the test code or
source code. Files are stored under version control directly in
the git repository.

Flexible Metadata Format is used to store data in a concise human
and machine readable way plus adds a few nice features like
virtual hierarchy, inheritance and elasticity to minimize data
duplication and maintenance.

There are several metadata levels defined:

**L0 Metadata: Core**

The base level specification defines core attributes such as
``summary`` and ``description``` which are common and can be used
across all metadata levels.

.. toctree::
    :maxdepth: 2

    spec/core

**L1 Metadata: Tests**

These are test metadata closely related to individual test cases
for which it make sense to store them directly with the test code.
Examples of such metadata are ``duration`` or ``tags``.

.. toctree::
    :maxdepth: 2

    spec/tests

**L2 Metadata: Plans**

Level 2 metadata contain information for execution of multiple
test cases such as how the environment for testing should be
prepared, which set of test cases is relevant for testing specific
artifact or which frameworks should be used for execution.

.. toctree::
    :maxdepth: 2

    spec/plans

**L3 Metadata: Stories**

For tracking user stories or features Level 3 metadata are used.
Stories can be linked to other objects. In this way it is possible
to easily track implementation, test and documentation coverage.

.. toctree::
    :maxdepth: 2

    spec/stories
