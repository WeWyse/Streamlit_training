# Introduction
Welcome to this training about Streamlit. You all find all materials and instructions in a dedicated Streamlit dashboard.

# Prerequisites
## Clone the project
Start by cloning the training repo from your terminal using
```bash
git clone https://pernod-ricard-data@dev.azure.com/pernod-ricard-data/PR.Data.Training/_git/PR.Data.Training.Streamlit
```
Navigate to the the root of the created folder with your terminal
```bash
cd PR.Data.Training.Streamlit
```

## Install Project Dependencies
It is adviced to clone create a dedicated Python environment fr each project you are working on. It allows you to use different versions of the same library for example.
<details>

<summary>Install Virtualenv</summary>

Check if it is already installed
```bash
which virtualenv
```

Install it if needed
```bash
pip install virtualenv
```
</details>
‎

Install a new virtual environment to keep your workspace clean
```bash
virtualenv --python=python3.8 venv
source venv/bin/activate
```
Verify you use the right venv with
```bash
which virtualenv
```
Install all the requirements
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

# Start the training
Once everything is all set, you can start the training switching to your dedicated branch with
```bash
git checkout -b name-surname-branch
```

Then, you will need to manually install the PR Python Toolbox with

```bash
pip install pr-python-toolbox==3.1.0 --index-url https://pernod-ricard-python-data:{PAT}@pkgs.dev.azure.com/pernod-ricard-data/_packaging/pernod-ricard-python-data/pypi/simple/
```
Make sure you replace the {PAT} with a valid PAT created from [here](https://dev.azure.com/pernod-ricard-data/_usersSettings/tokens)

Once the toolbox installed, you can start the training with

```bash
streamlit run app.py
```

This should launch a new web page but if not, you can access the dashboard at [this url](http://localhost:8501/).
