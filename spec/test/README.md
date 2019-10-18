
L1 Metadata
===========

Fedora Test Metadata Specification


Requirements
------------

In order to use the [Flexible Metadata Format][fmf] effectively for the CI
testing we need to agree on the essential set of attributes to be used.
For each attribute we need to standardize:

* name ... clear, unique, well chosen
* type ... expected type: string, number, list, dictionary
* purpose ... description of the attribute purpose

Each attribute definition should contain at least one apt example of the
usage and user stories illustrating the motivation.


Attributes
----------

Here is the list of attributes proposed so far. Material for discussion.
Nothing final for now.

* [summary](/fedora-ci/metadata/blob/master/f/l1/summary.fmf)
* [description](/fedora-ci/metadata/blob/master/f/l1/description.fmf)
* [tags](/fedora-ci/metadata/blob/master/f/l1/tags.fmf)
* [test](/fedora-ci/metadata/blob/master/f/l1/test.fmf)
* [path](/fedora-ci/metadata/blob/master/f/l1/path.fmf)
* [environment](/fedora-ci/metadata/blob/master/f/l1/environment.fmf)
* [duration](/fedora-ci/metadata/blob/master/f/l1/duration.fmf)
* [relevancy](/fedora-ci/metadata/blob/master/f/l1/relevancy.fmf)
* [contact](/fedora-ci/metadata/blob/master/f/l1/contact.fmf)
* [component](/fedora-ci/metadata/blob/master/f/l1/component.fmf)
* [tier](/fedora-ci/metadata/blob/master/f/l1/tier.fmf)
* [provision](/fedora-ci/metadata/blob/master/f/l1/provision.fmf)
* [disabled](/fedora-ci/metadata/blob/master/f/l1/disabled.fmf)
* [result](/fedora-ci/metadata/blob/master/f/l1/result.fmf)

See [examples](/fedora-ci/metadata/blob/master/f/l1/examples.md) to learn
how "path" and "test" attributes can be used together.


Status
------

Each attribute has its current status defined in the following way:

* draft ... attribute definition has been proposed
* approved ... proposal has been discussed and approved
* production ... attribute is supported in the tooling

[fmf]: https://fedoraproject.org/wiki/Flexible_Metadata_Format
