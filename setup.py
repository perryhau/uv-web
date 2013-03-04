import os
import glob
from distutils.core import setup, Extension

SOURCE_FILES = [os.path.join('http-parser', 'http_parser.c')] + \
               glob.glob(os.path.join('uv-web', '*.c'))

uvweb_extension = Extension(
    'uvweb',
    sources       = SOURCE_FILES,
    libraries     = ['uv','rt'],
    include_dirs  = ['http-parser','/home/johan/open-source/libuv/libuv-0.8/include'],
    define_macros = [('WANT_SENDFILE', '1'),
                     ('WANT_SIGINT_HANDLING', '1')],
    extra_compile_args = ['-fno-strict-aliasing', '-Wall',
                          '-Wextra', '-Wno-unused', '-g', '-fPIC']#,'-DDEBUG_DEV'
)

setup(
    name         = 'uvweb',
    author       = 'Jone Xiong',
    author_email = 'xiongjianhong@gmail.com',
    license      = '2-clause BSD',
    url          = 'https://github.com/JoneXiong/uv-web',
    description  = 'A screamingly fast Python WSGI server written in C.',
    version      = '1.2',
    classifiers  = ['Development Status :: 4 - Beta',
                    'License :: OSI Approved :: BSD License',
                    'Programming Language :: C',
                    'Programming Language :: Python',
                    'Topic :: Internet :: WWW/HTTP :: WSGI :: Server :: Libuv'],
    ext_modules  = [uvweb_extension]
)