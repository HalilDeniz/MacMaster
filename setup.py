from setuptools import setup, find_packages

setup(
    name='MacMaster: Advanced Network Interface Management and Monitoring',
    version='1.0.0',
    author='Halil İbrahim Deniz',
    author_email='halildeniz313@gmail.com',
    description='A versatile MAC Address Changer tool for network anonymity and testing.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/HalilDeniz/MacMaster',
    packages=find_packages(),
    install_requires=[
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'macmaster=macmaster.macmaster:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
