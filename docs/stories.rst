Stories
==================================================================

As a tool developer I want to access the L1 and L2 metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I want to easily access L1 metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Access test attributes
::::::::::::::::::::::

name
----

Examples::

    test.name

path
----

Path to the test execution directory. Defaults to the object name.

Examples::

    test.path

test
----

Examples::

    test.test

Explore available tests
:::::::::::::::::::::::

List all available tests
------------------------

Examples::

    Test.search()

Select tests by filter
----------------------

Examples::

    Test.search(artifact='pull-request')

I want to easily access L2 metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Access additional attributes:
::::::::::::::::::::::::::::::

Artifacts for which testset is executed
---------------------------------------

Examples::

    testset.gate

Gates for which the testset is relevant
---------------------------------------

Examples::

    testset.artifact

Short testset description
-------------------------

Examples::

    testset.summary

Explore available testsets
::::::::::::::::::::::::::

List all available testsets
---------------------------

Examples::

    TestSet.search()

Select testsets by filter
-------------------------

Examples::

    TestSet.search(name='/testsets/smoke')

Access test steps
:::::::::::::::::

discover
--------

Examples::

    testset.discover

execute
-------

Default implementation is 'shell'.

Examples::

    testset.execute

finish
------

Examples::

    testset.finish

prepare
-------

Examples::

    testset.prepare

provision
---------

Examples::

    testset.provision

report
------

Examples::

    testset.report

As a user I want to have an intuitive command line interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I want to execute tests easily
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default should cover the most common use case
:::::::::::::::::::::::::::::::::::::::::::::

Run all relevant tests on the default environment. Default environment should be something safe which should not modify user environment. Perhaps something like 'x86_64 virtual machine from the testing farm'?

Examples::

    tmt run

Select or adjust the discover step
::::::::::::::::::::::::::::::::::

Defines which tests should be executed.

Examples::

    tmt run discover
    tmt run discover --how=fmf
    tmt run discover --how=fmf --repo=url
    tmt run discover --how=list
    tmt run discover --how=shell
    tmt run discover --how=nitrate

Select or adjust the execute step
:::::::::::::::::::::::::::::::::

Specification of the testing framework which should execute tests.

Examples::

    tmt run execute
    tmt run execute --how=shell
    tmt run execute --how=beakerlib
    tmt run execute --how=restraint

Select tests for execution
::::::::::::::::::::::::::

Examples::

    tmt run test NAME
    tmt run test --filter=FILTER
    tmt run test --grep=REGEXP
    tmt run testset NAME2 test NAME1

Select testsets for execution
:::::::::::::::::::::::::::::

Examples::

    tmt run testset NAME
    tmt run testset --filter=FILTER
    tmt run testset --grep=REGEXP

Select or adjust the finish step
::::::::::::::::::::::::::::::::

Additional actions to be performed after the test execution has been completed. Counterpart of the prepare step useful for various cleanup actions.

Examples::

    tmt run finish

Store test step status, keep machines running
:::::::::::::::::::::::::::::::::::::::::::::

Examples::

    tmt run --keep provision prepare
    tmt run --keep discover execute
    tmt run --keep execute
    tmt run --keep execute

Select or adjust the prepare step
:::::::::::::::::::::::::::::::::

Additional configuration of the provisioned environment needed for testing.

Examples::

    tmt run prepare
    tmt run prepare --how=ansible
    tmt run prepare --how=ansible --playbook=server.yaml

Select or adjust the provision step
:::::::::::::::::::::::::::::::::::

Describes what environment is needed for testing and how it should provisioned.

Examples::

    tmt run provision
    tmt run provision --how=testing-farm
    tmt run provision --how=testing-farm --memory-min=8GB
    tmt run provision --how=openstack
    tmt run provision --how=container
    tmt run provision --how=podman
    tmt run provision --how=docker
    tmt run provision --how=podman --image=fedora:rawhide
    tmt run provision --how=beaker --distro=rhel-8
    tmt run provision --how=beaker --arch=s390x
    tmt run provision --how=local
    tmt run provision --how=qemu
    tmt run provision --how=vagrant

Select or adjust the report step
::::::::::::::::::::::::::::::::

Adjusting notifications about the test progress and results.

Examples::

    tmt run report
    tmt run report --email=email@example.com
    tmt run report --irc=room

Select multiple steps to be executed
::::::::::::::::::::::::::::::::::::

Run all test steps, customize some
----------------------------------

Examples::

    tmt run --all provision --how=container

Choose steps to be executed
---------------------------

Examples::

    tmt run provision prepare
    tmt run discover provision prepare

Run all steps until the given one
---------------------------------

Examples::

    tmt run --until prepare
    tmt run --until execute

Provide shortcuts for common scenarios
::::::::::::::::::::::::::::::::::::::

Examples::

    tmt run --container=fedora:rawhide
    tmt run --container=fedora:rawhide --cap-add=SYS_ADMIN

I want to comfortably work with stories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Show coverage overview
::::::::::::::::::::::

Documentation coverage
----------------------

Examples::

    tmt story coverage documenation

Implementation coverage
-----------------------

Examples::

    tmt story coverage implementation

General overview
----------------

Complete overview of the story coverage including implementation, testing and documentation status.

Examples::

    tmt story coverage

Test coverage
-------------

Examples::

    tmt story coverage test

I need to convert stories into a beautiful format
:::::::::::::::::::::::::::::::::::::::::::::::::

Export stories into html
------------------------

So that they can be quickly reviewed in a web browser. Optionally a simple python httpd server could be started to serve the page or pages.

Examples::

    tmt story export --html --server

Export stories into reStructuredText
------------------------------------

So that they can be included in tmt documentation.

Examples::

    tmt story export --rst

Search available stories
::::::::::::::::::::::::

Examples::

    tmt story --implemented
    tmt story --unimplemented
    tmt story --tested
    tmt story --untested
    tmt story --documented
    tmt story --undocumented

List available stories
::::::::::::::::::::::

Examples::

    tmt story ls

Show story details
::::::::::::::::::

Examples::

    tmt story show

I want to comfortably work with tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Convert old test metadata
:::::::::::::::::::::::::

Examples::

    tmt test convert

Test coverage overview
::::::::::::::::::::::

Show current status of test coverage. Alias for /stories/cli/story/coverage/test

Examples::

    tmt test coverage

Filter available tests
::::::::::::::::::::::

Examples::

    tmt test ls REGEXP
    tmt test ls --max-duration=5m
    tmt test ls --enabled
    tmt test ls --tier=1

Check against the L1 metadata specification
:::::::::::::::::::::::::::::::::::::::::::

Verify that test metadata are aligned with the specification, e.g. that all required attributes are present and that all attributes have correct type.

Examples::

    tmt test lint

List available tests
::::::::::::::::::::

Examples::

    tmt test ls

Show test metadata
::::::::::::::::::

Examples::

    tmt test show

I want to comfortably work with testsets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Filter available testsets
:::::::::::::::::::::::::

Examples::

    tmt testset ls REGEXP
    tmt testset show --artifact=pull-request

List available testsets
:::::::::::::::::::::::

Examples::

    tmt testset ls

Show testset configuration
::::::::::::::::::::::::::

Examples::

    tmt testset show

As a user I want to have essential documentation at hand
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A couple of examples should be included in the package for easy first experimenting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Examples should be stored under the /usr/share/doc directory.

Examples::

    cd /usr/share/doc/tmt/examples
    ls
    cd mini
    tmt test ls
    tmt testset ls
    tmt run

Main command and all its subcommands should provide --help
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All available options should be easily discoverable.

Examples::

    tmt --help
    tmt run --help
    tmt test convert --help

There should be a 'tmt' man page availabe in the package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Man page should contain brief introduction about the tool and a list of essential commands and options.

Examples::

    man tmt
