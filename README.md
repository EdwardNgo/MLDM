<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!-- <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">Text Classification for newspaper</h3>

  <p align="center">
    Project for "Introduction to Machine Learning and Data Mining" at HUST.
    <!-- <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
  </p> -->
</p>






### Built With

* [React](https://reactjs.org/)
* [Python3](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)



<!-- GETTING STARTED -->
## Getting Started


Make sure you have python3 installed on your computer. Recommended to install on Ubuntu.

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* **Detectron2**

Requirment
-   CUDA=10.1
-   Pytorch >= 1.7.0

How to install CUDA 10.1 can be found here: https://developer.nvidia.com/cuda-10.1-download-archive-base

How to install Pytorch can be found here: https://pytorch.org/

After installed above package, follow the instructions below to install detectron2:

```
$   pip install cython pyyaml==5.1
$   pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu100/index.html

```
After installed detectron2, run:

```
$   pip install -r requirments.txt
```

### Installation

1. Clone the repo
```sh
git clone https://github.com/Wild-Rift/Document-Layout-Analysis.git
```

2. Run demo 

```sh
streamlit run virtualize.py
```
