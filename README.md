<a href='https://github.com/WenjieDu/PyGrinder'><img src='https://pypots.com/figs/pypots_logos/PyGrinder_logo_FFBG.svg?sanitize=true' width='375' align='right' /></a>

<h2 align="center">Welcome to PyGrinder</h2>

**<p align='center'>a Python toolkit for grinding data beans into the incomplete</p>**

<p align='center'>
    <a href='https://github.com/WenjieDu/PyGrinder'>
        <img alt='Python version' src='https://img.shields.io/badge/python-v3-E97040?logo=python&logoColor=white'>
    </a>
    <a href="https://github.com/WenjieDu/PyGrinder/releases">
        <img alt="the latest release version" src="https://img.shields.io/github/v/release/wenjiedu/PyGrinder?color=EE781F&include_prereleases&label=Release&logo=github&logoColor=white">
    </a>
    <a href="https://github.com/WenjieDu/PyGrinder/blob/main/LICENSE">
        <img alt="GPL-v3 license" src="https://img.shields.io/badge/License-GPL--v3-E9BB41?logo=opensourceinitiative&logoColor=white">
    </a>
    <a  href='https://github.com/WenjieDu/PyGrinder/actions/workflows/testing_ci.yml'>
        <img alt='GitHub Testing' src='https://img.shields.io/github/actions/workflow/status/wenjiedu/PyGrinder/testing_ci.yml?logo=github&color=C8D8E1&label=CI'>
    </a>
    <a href="https://codeclimate.com/github/WenjieDu/PyGrinder">
        <img alt="Code Climate maintainability" src="https://img.shields.io/codeclimate/maintainability-percentage/WenjieDu/PyGrinder?color=3C7699&label=Maintainability&logo=codeclimate">
    </a>
    <a href='https://coveralls.io/github/WenjieDu/PyGrinder'>
        <img alt='Coveralls report' src='https://img.shields.io/coverallsCoverage/github/WenjieDu/PyGrinder?branch=main&logo=coveralls&color=75C1C4&label=Coverage'>
    </a>
    <a href="https://anaconda.org/conda-forge/PyGrinder">
        <img alt="Conda downloads" src="https://img.shields.io/endpoint?url=https://pypots.com/figs/downloads_badges/conda_pygrinder_downloads.json">
    </a>
    <a href='https://pepy.tech/project/PyGrinder'>
        <img alt='PyPI downloads' src='https://img.shields.io/endpoint?url=https://pypots.com/figs/downloads_badges/pypi_pygrinder_downloads.json'>
    </a>
</p>

<a href='https://github.com/WenjieDu/PyPOTS'><img src='https://pypots.com/figs/pypots_logos/PyPOTS_logo_FFBG.svg?sanitize=true' width='160' align='left' /></a>
PyGrinder is a part of [PyPOTS project](https://github.com/WenjieDu/PyPOTS) (a Python toolbox for data mining on
Partially-Observed Time Series), and was separated from PyPOTS for decoupling missingness-creating functionalities from
learning algorithms.

In data analysis and modeling, sometimes we may need to corrupt the original data to achieve our goal, for instance,
evaluating models' ability to reconstruct corrupted data or assessing the model's performance on only partially-observed
data. PyGrinder is such a tool to help you corrupt your data, which provides several patterns to create missing values
in the given data.

## ❖ Citing PyGrinder

The paper introducing PyPOTS project is available on arXiv at [this URL](https://arxiv.org/abs/2305.18811),
and we are pursuing to publish it in prestigious academic venues, e.g. JMLR (track for
[Machine Learning Open Source Software](https://www.jmlr.org/mloss/)). If you use PyGrinder in your work,
please cite PyPOTS project as below and 🌟star this repository to make others notice this library. 🤗 Thank you!

``` bibtex
@article{du2023PyPOTS,
title={{PyPOTS: A Python Toolbox for Data Mining on Partially-Observed Time Series}},
author={Wenjie Du},
year={2023},
eprint={2305.18811},
archivePrefix={arXiv},
primaryClass={cs.LG},
url={https://arxiv.org/abs/2305.18811},
doi={10.48550/arXiv.2305.18811},
}
```

or

> Wenjie Du. (2023).
> PyPOTS: A Python Toolbox for Data Mining on Partially-Observed Time Series.
> arXiv, abs/2305.18811. https://doi.org/10.48550/arXiv.2305.18811

<details>
<summary>🏠 Visits</summary>
<img align='left' src='https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FWenjieDu%2FPyGrinder&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Visits+since+May+2022&edge_flat=false'>
</details>
