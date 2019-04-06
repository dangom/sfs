# sfs

-----

**Table of Contents**

* [Purpose](#purpose)
* [Installation](#installation)
* [License](#license)

## Purpose

SFS is a tool to compute signal fluctuation sensitivity from an fMRI dataset, as described in:

DeDora DJ, Nedic S, Katti P, Arnab S, Wald LL, Takahashi A, Van Dijk KRA, Strey HH and Mujica-Parodi LR (2016) 
Signal Fluctuation Sensitivity: An Improved Metric for Optimizing Detection of Resting-State fMRI Networks. 
Front. Neurosci. 10:180. doi: 10.3389/fnins.2016.00180

Currently a WIP. The tool works, but I still have to make sure that results are correct.


## Installation

<!-- sfs is distributed on [PyPI](https://pypi.org) as a universal -->
<!-- wheel and is available on Linux/macOS and Windows and supports -->
<!-- Python 3.6+ and PyPy. -->

Clone this repository and:

```bash
$ python setup.py develop
```

## Usage

```python
from sfs.metrics import signal_fluctuation_sensitivity
from nilearn import image

img = image.load_img("my/fmri/dataset.nii.gz")
sfs = signal_fluctuation_sensitivity(img)
```

## License

sfs is distributed under the terms of the
[MIT License](https://choosealicense.com/licenses/mit).
