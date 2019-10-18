Examples
========

Below you can find some basic examples using the metadata which
have been already defined.

BeakerLib Tests
---------------

Three beakerlib tests, each in it's own directory:

main.fmf

    test: ./runtest.sh
    
    /one:
        path: /tests/one
    /two:
        path: /tests/two
    /three:
        path: /tests/three

fmf

    /one
    path: tests/one
    test: ./runtest.sh

    /two
    path: tests/two
    test: ./runtest.sh

    /three
    path: tests/three
    test: ./runtest.sh

Three Scripts
-------------

Three different script residing in a single directory:

main.fmf

    path: /tests
    
    /one:
        test: ./one
    /two:
        test: ./two
    /three:
        test: ./three

fmf

    /one
    path: /tests
    test: ./one

    /two
    path: /tests
    test: ./two

    /three
    path: /tests
    test: ./three

Virtual Tests
-------------

Thre virtual test cases based on a single test script:

main.fmf

    path: /tests/virtual
    
    /one:
        test: ./script --one
    /two:
        test: ./script --two
    /three:
        test: ./script --three

fmf

    /one
    path: /tests/virtual
    test: ./script --one

    /two
    path: /tests/virtual
    test: ./script --two

    /three
    path: /tests/virtual
    test: ./script --three
