# oq-haz-example
An example workout for hazard calculation using OpenQuake to generate a hazard map. This example is based on Grand Inversion ERF model for Hikurangi-interface. 

## Setup conda environment

```
cd gmcm-haz-sensitivity
conda env create -f environment.yml
```
The environment.yml file uses SSH keys to install NSHM repositories. To set them up click [here](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account). Alternatively replace
```
- git+ssh://git@github.com/GNS-Science/oq-engine.git@gm-sensitivity-tests
```
with
```
- git+http://github.com/GNS-Science/oq-engine.git@gm-sensitivity-tests
```
and enter your GitHub username and pass key.



## Quick Description

Hik-interface-ERF  contains files for source model
gmm contains files for ground motion models
...
job file is hazmapjob-grin-hik-MSR_LW.ini
...

## Command  

oq engine --run hazmapjob-grin-hik-MSR_LW.ini --exports csv


