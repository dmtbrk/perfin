from setuptools import setup, find_packages


setup(
    name='perfin',
    version='0.0.1',
    description='A personal finance app.',
    packages=find_packages(),
    python_requires='>=3.8, <4',
    install_requires=['pydantic'],
    entry_points={
        'console_scripts': [
            'perfin=perfin.__main__:main',
        ],
    },
)
