from setuptools import setup, find_packages

setup(
    name='filetree-visualizer',
    version='0.1.0',
    author='Your Name',
    description='Convert folders to tree views and build file structures from trees.',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'filetree=treevisualizer.cli:main_cli',  # command = module:function
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
