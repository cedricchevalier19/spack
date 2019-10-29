# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# TODO: Use gyp/ninja build system to have a faster compilation.

import glob
from os import makedirs

from llnl.util.filesystem import install_tree, join_path
from spack.build_systems.makefile import MakefilePackage
from spack.directives import version, variant, depends_on


class Nss(MakefilePackage):
    """Network Security Services (NSS) is a set of libraries designed to support
    cross-platform development of security-enabled client and server
    applications."""

    homepage = "https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS"

    version(
        '3.46.1',
        url=
        "https://ftp.Mozilla.org/pub/security/nss/releases/NSS_3_46_1_RTM/src/nss-3.46.1.tar.gz",
        sha256=
        '3bf7e0ed7db98803f134c527c436cc68415ff17257d34bd75de14e9a09d13651',
        when='~nspr')

    version(
        '3.46.1',
        url=
        "https://ftp.mozilla.org/pub/security/nss/releases/NSS_3_46_1_RTM/src/nss-3.46.1-with-nspr-4.21.tar.gz",
        sha256=
        '5ec5a4e4247eb60b8c15d5151e5b5ce6c14a751e4f2158c9435f498bd5c547f4',
        when='+nspr')

    variant("nspr", default=True, description="Enable internal nspr")

    # Compile instructions from Linux From Scratch:
    # see http://www.linuxfromscratch.org/blfs/view/cvs/postlfs/nss.html
    # patch('nss-3.46.1-standalone-1.patch')

    parallel = False
    depends_on('zlib')
    depends_on('nspr', when='~nspr')
    depends_on('sqlite@3:')

    build_directory = "nss"

    @property
    def build_targets(self):
        args = [
            'nss_build_all', 'USE_SYSTEM_ZLIB=1', 'NSS_ENABLE_WERROR=0',
            'USE_64=1', 'BUILD_OPT=1'
        ]
        args.append('NSS_USE_SYSTEM_SQLITE=1')
        if self.spec.satisfies('~nspr'):
            args.append('NSPR_INCLUDE_DIR={}/nspr'.format(
                self.spec['nspr'].prefix.include))
        return args

    def install(self, spec, prefix):
        makedirs(prefix.bin, exist_ok=True)
        makedirs(prefix.libraries, exist_ok=True)
        makedirs(prefix.include, exist_ok=True)
        base_path = 'dist'
        install_tree(join_path(base_path, 'public/dbm'),
                     prefix.include,
                     symlinks=False)
        install_tree(join_path(base_path, 'public/nss'),
                     prefix.include,
                     symlinks=False)
        compile_dir = glob.glob(join_path(base_path, '*.OBJ'))[0]
        print("Install from {}".format(compile_dir))
        install_tree(join_path(compile_dir, 'include'),
                     prefix.include,
                     symlinks=False)
        install_tree(join_path(compile_dir, 'lib'),
                     prefix.libraries,
                     symlinks=False)
        install_tree(join_path(compile_dir, 'bin'), prefix.bin, symlinks=False)
