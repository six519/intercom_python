import intercom

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="intercom_python",
    version="1.0.3",
    description="A not official python bindings to Intercom API",
    author="Ferdinand Silva",
    author_email="ferdinandsilva@ferdinandsilva.com",
    packages=['intercom'],
    install_requires=['requests'],
    url="https://github.com/six519/intercom_python",
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'License :: Freeware',
    ),
    download_url="https://github.com/six519/intercom_python",
)