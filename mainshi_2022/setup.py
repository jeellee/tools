import io
import sys

import setuptools


def has_environment_marker_support():
    """
    Tests that setuptools has support for PEP-426 environment marker support.
    The first known release to support it is 0.7 (and the earliest on PyPI seems to be 0.7.2
    so we're using that), see: http://pythonhosted.org/setuptools/history.html#id142
    References:
    * https://wheel.readthedocs.org/en/latest/index.html#defining-conditional-dependencies
    * https://www.python.org/dev/peps/pep-0426/#environment-markers
    """
    import pkg_resources
    try:
        v = pkg_resources.parse_version(setuptools.__version__)
        return v >= pkg_resources.parse_version('0.7.2')
    except Exception as exc:
        sys.stderr.write("Could not tests setuptool's version: %s\n" % exc)
        return False


def get_long_description():
    with io.open('README.rst', encoding='utf-8') as f:
        with io.open('CHANGELOG.rst', encoding='utf-8') as g:
            return "%s\n\n%s" % (f.read(), g.read())


def main():
    setuptools.setup(
        name='tox',
        install_requires=['py>=1.4.17',
                          'pluggy>=0.3.0,<1.0',
                          'six',
                          'virtualenv>=1.11.2'],
    )


if __name__ == '__main__':
    main()
