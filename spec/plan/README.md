# L2 Metadata

Fedora CI Metadata Specification


## Motivation

Specification of CI pipeline, trying to be CI agnostic and user friendly.
Here are the main points which motivated this effort:

* Additional metadata for test execution needed, stored on various places
* The tests.yml file defined by Standard Test Interface is limited
* Human readable configuration for gating (replace gating.yaml)
* Multiple gates in the release pipeline (pull request, build, update/errata)
* Clearly separate testing steps (discover, provision, prepare, execute, report)
* Support multiple tools implementing individual testing steps


## Artifacts

Specifies the artifact to be tested. Currently defined artifacts:

* `pull-request` ... code check (static analysis, conventions...)
* `build` ... functional testing of rpm build from koji or brew
* `update` ... one or more builds grouped in an update/erratum

Based on the artifact it is possible to detect some environment
constraints such as architecture or base compose.


## Testsets

For each artifact it is possible to define one or more testsets.
Each testset represents group of tests with a unique identifier.
The `summary` attribute can be used to describe testset purpose.

    /test:
        /pull-request:
            /pep:
                summary: All code must comply with the PEP8 style guide
            /lint:
                summary: Run pylint to catch common problems (no gating)
        /build:
            /smoke:
                summary: Basic smoke test (Tier1)
            /features:
                summary: Verify important features


## Gates

Multiple gates can be defined in the process of releasing a change.
Currently we define the following gates:

* merge-pull-request ... block merging a pull request into a git branch
* add-build-to-update ... attaching a build to an erratum / bodhi update
* add-build-to-compose ... block adding a build to a compose
* release-update ... block releasing an erratum / bodhi update

Each testset can define one or more gates it should be blocking.
Here is an example of configuring multiple gates

    /test:
        /pull-request:
            /pep:
                summary: All code must comply with the PEP8 style guide
                # Do not allow ugly code to be merged into master
                gate:
                    - merge-pull-request
            /lint:
                summary: Run pylint to catch common problems (no gating)
        /build:
            /smoke:
                summary: Basic smoke test (Tier1)
                # Basic smoke test is used by three gates
                gate:
                    - merge-pull-request
                    - add-build-to-update
                    - add-build-to-compose
            /features:
                summary: Verify important features
        /update:
            # This enables the 'release-update' gate for all three testsets
            gate:
                - release-update
            /basic:
                summary: Run all Tier1, Tier2 and Tier3 tests
            /security:
                summary: Security tests (extra job to get quick results)
            /integration:
                summary: Integration tests with related components


## Hierarchy

There are several levels of test execution data configuration:

* default ... global default settings (common for most instances)
* detect ... detect from previous steps output (e.g. distro from build)
* define ... allow to override value by explicit user configuration

Let's demonstrate these on a simple example with a distribution compose (C) and the amount of memory (M):

* CI system is configured by `default` to use compose `C1` installed on machines with `M1` GB of memory.
* When inspecting an artifact CI can `detect` that for this particular build target, compose `C2` is a much better choice, and memory is fine as it is.
* User can still explicitly `define` in the configuration that at least `M2` GB of memory is needed for successful test execution which overrides both default and detected values.


## Steps

There are several separate steps defined for the test execution.
Clearly separating testing stages gives users control over their individual aspects.
Each step makes it clear what and how can be influenced for that particular stage of the process.
This approach also allows to run only selected steps when desired.
For example run `discover` only to see which tests will be executed or skip `provision` and `prepare` when quickly testing on localhost.
Each step can be supported by multiple implementations.
Special keyword `how` defines which implementation should be used.

### Discover

Gather information about the test cases which are supposed to be run.
This includes list of test cases with corresponding L1 metadata.
From the test case metadata constraints for test enviroment can be detected:

* Architectures supported
* Disk and memory constraints
* Product relevancy
* Environment variables

Examples of metadata storage:

* `list` ... Manual list of test cases
* `fmf` ... Flexible Metadata Format filter
* `tcms` ... Test Case Management System

Example config:

    discover:
        how: 'fmf'
        filter: 'tier: 1'

### Provision

Describes what environment is needed for testing and how it should provisioned.
Provides a generic and extensible way to write down essential hardware requirements.
For example one consistent way how to specify "at least 2 GB of RAM" for all supported provisioners.

* Possible grouping of test cases based on test case relevancy
* Might fail if cannot provision according to the constraints

Examples of provisioning implementation:

* `localhost` ... run directly on the local machine
* `openstack` ... create vm in using OpenStack
* `beaker` ... reserve machine using Beaker
* `podman` ... create a container using podman
* `qemu-kvm` ... run a vm using qemu-kvm

Example config:

    provision:
        memory:
            min: '1 GB'
        arch:
            - 'x86_64'

### Prepare

Additional configuration of the provisioned environment needed for testing.

* Install artifact (customizable according to user needs)
    * Conflicts between rpms
    * Optionally add debuginfo
    * Install with devel module
* Additional setup possible if needed
    * Inject arbitrary commands
    * Before/after artifact installation

Examples of preparation implementation:

* `shell` ... execute arbitratry shell commands to set up the system
* `ansible` ... apply ansible playbook to get the desired final state

Example prepare config using the `ansible` implementation:

    prepare:
        how: ansible
        roles:
            - nginxinc.nginx
        playbooks:
            - common.yml
            - rhel7.yml

One or more playbooks can be provided as a list under the `playbooks` attribute.
Each of them will be applied using `ansible-playbook` in the given order.
Optional attribute `roles` can be used to enable additional roles.
Role can be either an ansible galaxy role name, git url or a path to file with detailed requirements.


### Execute

Specification of the testing framework which should execute tests.

* Execute discovered tests on provisioned boxes
* With optional support for parallelization

Examples of execution implementation:

* `shell` ... execute arbitratry shell commands, check exit code (default)
* `beakerlib` ... run beakerlib tests, check the journal for test results
* `restraint` ... use the [restraint][restraint] harness to execute beakerlib tests

Example config:

    execute:
        how: beakerlib
        isolate: true

Optional boolean attribute `isolate` can be used to request a clean test environment for each test.

The `shell` implementation is the default one.
Thus you can omit the `how` keyword and just define the `script` to be run.
This is how a minimal smoke test for the `fmf` command line can look like:

    execute:
        script: fmf --help

You can also include several commands as a list.
Executor will run commands one-by-one and check exit code of each:

    execute:
        script:
            - dnf -y install httpd curl
            - systemctl start httpd
            - echo foo > /var/www/html/index.html
            - curl http://localhost/ | grep foo

Finally, providing a multi-line shell script is also supported:

    execute:
        script: |
            dnf -y install httpd curl
            systemctl start httpd
            echo foo > /var/www/html/index.html
            curl http://localhost/ | grep foo

In that case executor will store given script into a file and execute.


### Report

Adjusting notifications about the test progress and results.

* `email` ... send email notification
* `irc` ... notify on irc chat

Example config:

    report:
        email:
            - email@address.org

### Finish

Additional actions to be performed after the test execution has been completed.
Counterpart of the `prepare` step useful for various cleanup actions.

Example config:

    finish:
        how: shell
        command: upload-logs.sh

[restraint]: https://restraint.readthedocs.io/
