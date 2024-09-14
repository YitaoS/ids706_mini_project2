from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()

setup(
    name='my_python_project',
    version='0.1',
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    extras_require={
        'dev': [
            'flake8',
            'black',
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
