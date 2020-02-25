.. islelib documentation master file, created by
   sphinx-quickstart on Mon Oct  1 00:18:03 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

IsleConsumer
============

.. toctree::
   :maxdepth: 2
   :caption: Contents:

IsleConsumer is Illuscio's python consumer microservice template. It builds on top of the
`islelib`_ template for python libraries. This documentation will focus on the
differences between the two templates rather than re-iterating the base features
inherited from `islelib`_.

Table of Contents
=================

* :ref:`basic-usage`
* :ref:`setting-up`
* :ref:`writing`
* :ref:`deploying`

.. _basic-usage:

Basic Usage
===========

>>> python service
INFO: STARTING UP 'isleconsumer'

IsleConsumer comes with a number of pre-built quality-of-life macros for developers so
they can code more and manage less, most of which are accessed through ``make``
commands.

.. _setting-up:

Setting up your Service
=======================

Setting up a service follows the same steps as setting up a library in ``islelib``
with a few small notes:

   * You service will inherit the name passed to ``make name``. The main package of your
     service will always be ``service`` do not change the package name, as some of the
     service framework relies on it.

   * ``make test`` will pull and spin up a RabbitMQ docker image to test against.
     Although this might violate the idealized philosophy of unittests, because a
     consumer service is so tightly tied with message handling, it is the opinion of
     this library's author that running tests against an actual instance of the leads to
     greater confidence in the test results, and saves time having to mock RabbitMQ's
     API.

.. _writing:

Writing Your Service
====================

Linting, Testing and Basic documentation are all handled identically to `islelib`_.

Services are based off of `spanconsumer`_ ``SpanConsumer`` objects. It is suggested you be
familiar with it and the libraries it is built to work with:

   * `grahamcracker`_
   * `marshamllow`_
   * `dataclasses`_
   * `typing`_
   * `aio_pika`_

**Isleservice requires python 3.7 or later.**

Set up the processors and startup / shutdown tasks of your service, then your service is
ready to go!

.. _deploying:

Deploying Your Service
======================

Service containers are built through `Azure Devops`_ just as islelib libraries are.
Azure Pipelines can be configured to use `Dockerhub`_ or any dockerhub-compatible API
(illuscio uses `Azure Container Registry`_).

On Azure define the following variables in a library-group, then link the group to your
service's pipeline:

   * **CONTAINER_REGISTRY_ID**: Your dockerhub/registry user ID
   * **CONTAINER_REGISTRY_PASSWORD**: Your dockerhub/registry user password
   * **CONTAINER_REGISTRY_URL**: Your dockerhub/registry base url

Azure will automatically build a new image of your service and update your registry with
it. It will add both tags for the latest version and update the ``latest`` tag to the
newest build.

.. warning::

   **SECURITY NOTE:** Dockerhub will default to a public repo when pushing a
   new service for the first time. To avoid this, create a private repo *before*
   executing your first build.

   The default for azure container registry is private, so no action needs to be taken
   before a build.

.. note::

   For more information on the Azure build process this template uses, see the
   `remote build pipeline templates repo`_.


Dockerfile Template
===================

The dockerfile included in this template uses a multi-stage build process, allowing
users to pass the following environmental variables in for the build:

   * **PIP_INDEX_URL**: First pypi index to use during pip install.
   * **PIP_EXTRA_INDEX_URL**: Second pypi index to use during pip install.

Because one or both of these variables may contain login information for private
indexes, they are used in the build container, which is then discarded. Services
are installed into a virtual environment, which is then copied to the output
container for the actual service to build.

The base image used for services in ``python:3.8-slim``, into which the required
dependencies for building wheels are added. After build, the entire virtual environment
is copied into our service container, and used to run the service.


.. web links:
.. _islelib: https://illuscio-dev-islelib-py.readthedocs-hosted.com/en/latest/
.. _responder: https://github.com/kennethreitz/responder
.. _typing: https://docs.python.org/3/library/typing.html
.. _dataclasses: https://docs.python.org/3/library/dataclasses.html
.. _Azure Devops: https://azure.microsoft.com/en-us/services/devops/
.. _grahamcracker: https://github.com/illuscio-dev/grahamcracker-py
.. _marshamllow: https://marshmallow.readthedocs.io/en/3.0/
.. _readthedocs: https://readthedocs.com/
.. _spanreed:
.. _sphinx: http://www.sphinx-doc.org/en/master/
.. _swagger: https://swagger.io/solutions/api-design/
.. _Dockerhub: https://hub.docker.com/
.. _Azure Container Registry: https://azure.microsoft.com/en-us/services/container-registry/
.. _aio_pika: https://aio-pika.readthedocs.io/en/latest/
.. _remote build pipeline templates repo: https://github.com/illuscio-dev/azure-pipelines-templates
.. _spanconsumer: https://github.com/illuscio-dev/spanconsumer-py
