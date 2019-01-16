# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class XcbUtilImage(AutotoolsPackage):
    """The XCB util modules provides a number of libraries which sit on top
    of libxcb, the core X protocol library, and some of the extension
    libraries. These experimental libraries provide convenience functions
    and interfaces which make the raw X protocol more usable. Some of the
    libraries also provide client-side code which is not strictly part of
    the X protocol but which have traditionally been provided by Xlib."""

    homepage = "https://xcb.freedesktop.org/"
    url      = "https://xcb.freedesktop.org/dist/xcb-util-image-0.4.0.tar.gz"

    version('0.4.0', '32c9c2f72ebd58a2b2e210f27fee86f7')

    depends_on('libxcb@1.4:')
    depends_on('xcb-util')

    depends_on('xproto@7.0.8:', type='build')
    depends_on('pkgconfig', type='build')
