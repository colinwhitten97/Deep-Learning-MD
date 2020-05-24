# DeepMD-kit- Colin's tutorial so far

# Table of Contents
- [About](#About)
  * [How DeePMD- kit works](#how-DeePMD-kit-works)
  * [License and Credits](#license-and-credits)
- [Installation](#Installation)
- [Running Simulations](#running-simulations)
- [Pitfalls/Troubleshooting](#pitfalls/troubleshooting)
  
  
# About
<!-- toc -->

## How DeePMD kit works

Here is where I will give a more comprehensive report on DeepMD-kit and specifically its potential usefulness to the lab- or researchers in general

## License and Credits
None of this kit nor its code are mine, and if you use the DeePMD-kit you can use the citation below. The project DeePMD-kit is licensed under GNU LGPLv3.0.

Han Wang, Linfeng Zhang, Jiequn Han, and Weinan E. "DeePMD-kit: A deep learning package for many-body potential energy representation and molecular dynamics." Computer Physics Communications 228 (2018): 178-184.


# Installation

These following instructions will direct you to install all necessary components for DeePMD-kit and LAMMPS when starting completely from scratch. 

## Create instance of Linux to use DeePMD-kit 

DeePMD- kit is native to Linux, so you are required to run it there. If you already have an instance of Linux, skip this step. If you are using a Windows PC, there is a tutorial on how to set up an instance of Linux in the troubleshooting section **here**. 

## Download using Conda

To install the DeePMD-kit, you must first install Anaconda or Miniconda. If storage space on your instance of Linux is an issue, use Miniconda. If you already have conda, skip this step. 

Instructions on installing Miniconda [here.](https://www.youtube.com/watch?v=Ye4epph6Gzo) 

## Install CPU version of DeePMD-kit
From here on I will only focus on the CPU version of this kit. If I find out that the GPU version may also be necessary, then I will include it. 

Open the terminal in Linux, and begin the installation. 
To install the CPU version via Conda: virtu

`conda install deepmd-kit=*=*cpu lammps-dp=*=*cpu -c deepmodeling`

## Install python interface with TensorFlow

First, check and ensure that you have python and the compiler on your machine:

`python3 --version`

`gcc --version`

`pip3 --version`

`virtualenv -- version`

If you are missing any of these above packages and if you are using a local machine, install them using `sudo apt install`.  

It is recommended to create a virtual environment in order to isolate package installation from the system. In doing so, in the future when doing work with DeePMD-kit or TensorFlow, it will be necessary to activate the virtual environment. 

create a new virtual environment:

`virtualenv --system-site-packages -p python3 ./venv`

Here is how you activate the virtual environment, and this is the command you will use anytime you want to activate the virtual environment:

`source ./venv/bin/activate`

When the virtual environment is active, your shell prompt is prefixed with `(venv)`

Whenever you are done using DeePMD-kit or TensorFlow, make sure to exit the virtual environment later by `deactivate`. 

Upgrade pip if necessary:
`pip install --upgrade pip`

Now, go forward with installing TensorFlow:

`pip install --upgrade tensorflow`

Verify the install:

`python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"`

TensorFlow should now be installed.

**Note:** here is where one pitfall may occur in installing tensorflow. If the installation and verification does not work, refer [here](

## Install DeePMD-kit's python interface

First, clone the DeePMD-kit source code

`cd /some/workspace`

`git clone --recursive https://github.com/deepmodeling/deepmd-kit.git deepmd-kit -b devel`

You can record the location of the source with `deepmd_source_dir`

`cd deepmd-kit`
`deepmd_source_dir = pwd` 

Then execute

`pip install .`

To test the installation, you may execute

`dp -h`

## Install the C++ Interface IMPORTANT

`cd deepmd-kit/source
mkdir build
cd build`

To install DeePMD-kit into path `$deepmd_root` then execute cmake

`cmake -DTENSORFLOW_ROOT=$tensorflow_root -DCMAKE_INSTALL_PREFIX=$deepmd_root ..`

You may have to first install cmake with `sudo apt install cmake`

The GPU and CUDA tool-kit may be necessary here...

`cmake -DUSE_CUDA_TOOLKIT=true -DTENSORFLOW_ROOT=$tensorflow_root -DCMAKE_INSTALL_PREFIX=$deepmd_root ..`

If the cmake has executed successfully, then run 

`make
make install`

If it works fine, then there should be the following executables and libraries installed in `$deepmd_root/bin` and `$deepmd_root/lib`

`$ ls $deepmd_root/bin
dp_ipi
$ ls $deepmd_root/lib
libdeepmd_ipi.so  libdeepmd_op.so  libdeepmd.so`



## Install LAMMPS DeePMD-kit module ALSO IMPORTANT

The deepmd-kit also provides a module for running MD simulations with LAMMPS. You can make the DeePMD-kit module for LAMMPS

`cd $deepmd-kit/source/build
make lammps`

### How to retrieve LAMMPS and install it 

Uncompress the LAMMPS file `lammps-stable.tar.gz`. Here is where I will explain where and how to find LAMMPS, and how to install it so that it can be used with DeePMD-kit. 

`cd /some/workspace
tar xf lammps-stable.tar.gz`

`cd lammps-31Mar17/src/
cp -r $deepmd_source_dir/source/build/USER-DEEPMD .`

`make yes-user-deepmd
make mpi -j4`

This should end up with an executable `lmp_mpi` FIND MPI!


# Use the DeePMD-kit

## Running an example simulation?

### Prepare Model

### Train Model

### Freeze Model

### Use model to run simulation with native MD code

### Use model with LAMMPS to run simulation

# Pitfalls/ Troubleshooting

## Linux OS

If you are starting completely from scratch and want to run DeepMD-kit from a Windows PC, here is a video tutorial detailing how to use Oracle VirtualBox to set up and run a usable Ubuntu instance from your Windows PC. 

[YouTube Tutorial- How to Install Ubuntu on VirtualBox in Windows](https://www.youtube.com/watch?v=QbmRXJJKsvs)

In all, installing the DeepMD kit, LAMMPS, and all the components necessary to run them will take up roughly ~14 GB of disk space. Therefore, allocating at least **minimum 15 GB** of disk space to your Ubuntu VirtualBox virtual hard drive is necessary to run DeePMD-kit and LAMMPS. However, adding more is much better. Feel free to allocate as much disk space as you may see fit- however many GB you may decide to allocate- it is not all allocated at once, but rather it is allocated accordingly by how much space you have so far used in Ubuntu, so do not worry about allocating too much disk space and having it depleted from your main hard drive immediately. 

## MD: cannot make user in DeePMD-kit

One major pitfall I experienced in using LAMMPS with DeePMD-kit was "make user." 

## Tensorflow Installation

You may run into a pitfall during the installation of tensorflow. I experienced trouble during this step, and was able to successfully install tensorflow using a different process. The original DeePMD-kit documentation leaves little instruction on how to accomplish this. While the installation steps may be straightforward, in case you are unfamiliar with Ubuntu and Linux and referred here, follow these steps.

`sudo apt-get install python3`

`sudo apt-get install python3-pip`

`pip install tensorflow`

Then, to verify the installation you can quickly create a small python file which utilizes tensorflow: Create a test file such as "tensor.py" and write these lines into it:




# Colin's next plans for the tutorial?


- Try to make my own example for MD simulations with deepmd kit and give thorough detailed explanation of how it works

- Give detailed walkthrough for incorporating LAMMPS with DeePMD-kit 









