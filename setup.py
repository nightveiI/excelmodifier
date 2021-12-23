from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'excelmodifier package'
LONG_DESCRIPTION = 'the following packages are to be included to let this script function correctly for its purpose'

# Setting up
setup(
        name="excelmodifier", 
        version=VERSION,
        author="Jose Aguilar",
        author_email="<jhagui7464@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package', 'excel', 'data analysis'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: McAllen Valley Roofing Co.",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)