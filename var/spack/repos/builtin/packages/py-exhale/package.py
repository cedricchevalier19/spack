# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-exhale
#
# You can edit this file again by typing:
#
#     spack edit py-exhale
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyExhale(PythonPackage):
    """Automatic C++ library api documentation generation: breathe doxygen in and exhale it out."""

    homepage = "https://github.com/svenevs/exhale"
    url      = "https://github.com/svenevs/exhale/archive/v0.2.1.tar.gz"

    version('0.2.1', sha256='e834b097d3c12c1207f68e2b9cfc44c72023765f7de57aeb30badabbb3852bf5')
    version('0.2.0', sha256='129c89a4a033996bd95b7b3affc7c959b4612f5165f52ce53b9e1a75c232b9cb')
    version('0.1.8', sha256='500b44914ab3e9ab06cde1f9536ed1f2a1df199a6d6badf0ab5ab037a3bd9800')

    # Most python packages need py-setuptools only for build
    # sphinx needs this also for run.
    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('py-sphinx @1.6.1:', type=('build', 'run'))
    depends_on('py-six', type=('build', 'run'))
    depends_on('py-breathe', type=('build', 'run'))
    depends_on('py-lxml', type=('build', 'run'))
    depends_on('py-beautifulsoup4', type=('build', 'run'))

