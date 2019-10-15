
Metadata Specification
======================

This is Metadata Specification which defines that all data needed
for test execution in the CI system are stored as a plain text
information in Flexible Metadata Format under version control in
the git repository close to the test code or source code. FMF uses
YAML to store data in a concise human and machine readable way
plus adds a few nice features like virtual hierarchy, inheritance
and elasticity to minimize data duplication and maintenance. There
are two levels of metadata defined:

**L1 Metadata**

These are test metadata closely related to individual test cases
for which it make sense to store them directly with the test code.
Examples of such metadata are summary, description, duration or
tags. See Level 1 Metadata section for more detailed information
and list of already defined attributes.

**L2 Metadata**

These metadata contain information for execution of multiple test
cases such as how the environment for testing should be prepared,
which set of test cases is relevant for testing specific artifact
or which frameworks should be used for execution. See Level 2
Metadata section for detailed specification.

.. toctree::
    :maxdepth: 2

    specs/l1
    specs/l2
