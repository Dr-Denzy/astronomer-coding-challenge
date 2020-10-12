from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='Astronomer.io Coding Challenge',
    version='1.0.0',
    description='Astronomer.io job interview programming challenge.',
    long_description=readme(),
    python_requires='>=3.8',
    license='MIT',
    author='Dennis Akpenyi',
    author_email='dennisakpenyi@gmail.com',
    packages=find_packages(exclude=['tests*']),
)