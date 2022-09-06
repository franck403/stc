from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='stc',
    url='https://github.com/franck403/stc',
    author='Gilaxy04 GEOLOUP',
    author_email='franckiebbb@gmail.com',
    # Needed to actually package something
    packages=['stc'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='gilaxy04',
    description='text checker',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
