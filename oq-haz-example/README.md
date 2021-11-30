# oq-haz-example
An example workout for hazard calculation using OpenQuake to generate a hazard map. This example is based on Grand Inversion ERF model for Hikurangi-interface. 

## Setup conda environment

```
cd gmcm-haz-sensitivity
conda env create -f environment.yml
```

## Quick Description

```
***Hik-interface-ERF*** contains files for source model

_gmm_ contains files for ground motion models

job file is _hazmapjob-grin-hik-MSR_LW.ini_
```

## Command  
```
oq engine --run hazmapjob-grin-hik-MSR_LW.ini --exports csv
```

