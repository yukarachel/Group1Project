How to install packages
* Open VS Code and create a virtual environment
* Run "pip3 install -r requirements.txt"
* If pylsl doesn't install because of an issue with conda, install miniconda here: https://docs.anaconda.com/miniconda/install/#quick-command-line-install
    * Then run conda install -c conda-forge liblsl
    * Find the dynamic library files in here "/Users/{username}/miniconda3/lib"
    * Copy the dynamic library files in ".venv/lib/python3.13/site-packages/pylsl/lib"
* Run the code