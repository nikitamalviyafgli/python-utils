# upgrade pip or any package
python -m pip install --upgrade pip
# install package
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -U pytesseract
# install requirements
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -U -r requirements.txt
# upgrade package
python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade Pillow --user

# create venv
python3 -m venv ~/py36
# or
python -m venv c:\path\to\py36
  
# activate
source ~/py36/bin/activate


# for conda trusted host
conda config --set ssl_verify no
# conda create new env
conda create -n uw36 python=3.6
# install package using conda
conda install -c conda-forge opencv=3.2.0
# create conda env at a location
conda create --prefix E:\Anaconda\env_name python=3.8
# update conda
conda update -n base -c defaults conda
# install requirements.txt using conda 
conda install --force-reinstall -y -q --name py37 -c conda-forge --file requirements.txt
# delete conda env
conda env remove -n env_name
# remove env
conda remove --name env_name --all
