# Colin's DeePMD-kit Tutorial

# Table of Contents
- [About](#About)
  * [How DeePMD- kit works](#how-DeePMD-kit-works)
  * [License and Credits](#license-and-credits)
- [Installation](#Installation)
  * [Create instance of Linux to use DeePMD-kit](#create-instance-of-linux-to-use-deepmd-kit)
  * [Download using Conda](#download-using-conda)
  * [Install CPU version of DeePMD-kit](#install-cpu-version-of-deepmd-kit)
  * [Install python interface with TensorFlow](#install-python-interface-with-tensorflow)
  * [Install DeePMD-kit's python interface](#install-deepmd-kit's-python-interface)
  * [Install the C++ Interface](#install-the-c++-interface)
  * [Install LAMMPS DeePMD-kit module](#install-lammps-deepmd-kit-module)
   + [How to retrieve LAMMPS and install it](#how-to-retrieve-lammps-and-install-it)
- [Use the DeePMD-kit](#use-the-deepmd-kit)
  * [Running an Example Simulation](#running-an-example-simulation)
   + [Prepare Model](#prepare-model)
   + [Train Model](#train-model)
   + [Freeze Model](#freeze-model)
   + [Use model to run simulation with native MD code](#use-model-to-run-simulation-with-native-md-code)
   + [Use model with LAMMPS to run simulation](#use-model-with-lammps-to-run-simulation)
- [Pitfalls/Troubleshooting](#pitfalls-and-troubleshooting)
  * [Linux OS](#linux-os)
  * [Installing C++ Interface](#installing-c++-interface)
  * [MD: cannot make user in DeePMD-kit](#md-cannot-make-user-in-deepmd-kit)
  * [Tensorflow Installation](#tensorflow-installation)
- [More information on DeePMD-kit](#more-information-on-deepmd-kit)
  
  
# About


## How DeePMD kit works

The DeePMD-kit is a package written in Python and C++ designed to make it easier to build deep learning based representation of potential energy and force fields. Deep learning models trained from the DeePMD-kit can be used to perform more accurate simulations at less computational cost. It is interfaced with TensorFlow, which is a commonly used deep learning framework, which makes the training process automatic and efficient. Additionally, the DeePMD-kit is interfaced with LAMMPS and the i-PI, high performance classical molecular dynamics and quantum MD packages, but I only have provided description of the DeePMD-kit's capabilities with just LAMMPS. Trained potential energy and force field models can then be used to perform diferent purposes for efficient molecular simulations. 

## License and Credits
None of this kit nor its code are mine, and if you use the DeePMD-kit you can use the citation below. The project DeePMD-kit is licensed under GNU LGPLv3.0.

Han Wang, Linfeng Zhang, Jiequn Han, and Weinan E. "DeePMD-kit: A deep learning package for many-body potential energy representation and molecular dynamics." Computer Physics Communications 228 (2018): 178-184.


# Installation

These following instructions will direct you to install all necessary components for DeePMD-kit and LAMMPS when starting completely from scratch. 

## Create instance of Linux to use DeePMD-kit 

DeePMD- kit is native to Linux, so you are required to run it there. If you already have an instance of Linux, skip this step. If you are using a Windows PC, there is a tutorial on how to set up an instance of Linux in the troubleshooting section [here](#linux-os). If you follow those instructions exactly you will be able to use Ubuntu to get started with the DeePMD-kit. 

## Download using Conda

To install the DeePMD-kit, you must first install Anaconda or Miniconda. If storage space on your instance of Linux is an issue, use Miniconda. If you already have a conda distribution, skip this step. 

The main difference between the two is that Miniconda just ships the repository management system- which allows you to download and use DeePMD-kit. Installing miniconda gives you just the management system without any further packages. Anaconda on the other hand is a more thorough distribution with some built in packages. 

If you are brand new to conda or Python, you may want to choose Anaconda. It offers the convenience of having Python and over 150 scientific packages automatically installed at once; if you can spare the time (a few minutes) and disk space (~ 3 GB) and do not want to install any packages you want to use individually. 

Choose Miniconda if you don't mind installing each package you want individually and just want fast access to Python and the conda commands. You can still sort out any other programs and packages later. Some find Anaconda to be bloated.  

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

**Note:** here is where one pitfall may occur in installing tensorflow. If the installation and verification does not work, refer [here](#tensorflow-installation)

## Install DeePMD-kit's python interface

First, clone the DeePMD-kit source code into some workspace where you want to clone it to. 

`cd /some/workspace`

`git clone --recursive https://github.com/deepmodeling/deepmd-kit.git deepmd-kit -b devel`

You can record the location of the source with `deepmd_source_dir`

`cd deepmd-kit`
`deepmd_source_dir = pwd` 

Then execute

`pip install .`

To test the installation, you may execute

`dp -h`

This, if the installation is successful, will bring up a small help menu that describes a few commands for the DeePMD-kit. 

## Install the C++ Interface

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

This is where I suppose the most pitfalls in installation occur. Refer to the help [here](#installing-c++-interface). 

## Install LAMMPS DeePMD-kit module

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

## Running an example simulation

We can train a deep neural network which is used to represent the interatomic interactions, or Deep Potential. I will refer to the deep neural network as a **model**. 

### Prepare Model

To train the deep neural network, or model, we need to provide the simulation box, atom coordinate, atom force, system energy, and virial. The snapshot of the system that contains this information is called a **frame**. 

Time is measured in picoseconds (ps), length in Angstrom (Å), energy in electronvolt (eV), force in electronvolt per Angstrom (eV/Å), and pressure in Bar. 

The frames of the system are stored in two formats: `.raw` files of plain text, and data sets of `numpy` binary data. 
The default files that provide box, coordinate, force, energy, and virial are `box.raw`, `coord.raw`, `force.raw`, `energy.raw`, and `virial.raw`, respectively. Use these file names!

From what I have gathered myself, I can not find example files of these `.raw` types in the deepmd-kit files. However, these files are not used directly by the training program. Instead, the training program uses three sets, which are generated by the `.raw` files. You can convert these to the set files using the script at `deepmd-kit/source/data/raw/raw_to_set.sh`. For the water example this has been done already. If you have the six necessary raw files, your command prompt will look like this:

`$ ls 
box.raw  coord.raw  energy.raw  force.raw  type.raw  virial.raw
$ $deepmd_source_dir/data/raw/raw_to_set.sh 2000
nframe is 6000
nline per set is 2000
will make 3 sets
making set 0 ...
making set 1 ...
making set 2 ...
$ ls 
box.raw  coord.raw  energy.raw  force.raw  set.000  set.001  set.002  type.raw  virial.raw`

This will generate three sets, `set.000` and `set.001` which are used as training sets, and `set.002`, which is the testing set. The path containing `set.*` and `type.raw` we will refer to as a system. 

You may create your own raw type files: create a file by navigating to the water example folder and using the command `cat force.raw`. It would look something like this:

`-0.724  2.039 -0.951  0.841 -0.464  0.363
 6.737  1.554 -5.587 -2.803  0.062  2.222
-1.968 -0.163  1.020 -0.225 -0.789  0.343`

This contains 3 frams with each fram having the forces of two atoms. Each line provides the 3 force components of 2 atoms in 1 frame. The first three numbers are the 3 force components of the first atom, while the second three numbers are the 3 force components of the second atom. `coord.raw` is organized the same way, and in `box.raw`, the 9 components of the box vectors are provided on each line, and `virial.raw` is organized similarly, with the 9 components of the virial tensor provided on each line. Thus, each raw file should have the same number of lines. 

The `type.raw` is formatted like this:

`$ cat type.raw
0 1`

This would be for a system of two atoms, with the types being represented by integers. 


### Train Model

There is an example given with the kit in `deepmd-kit/examples/water/train/`. The file is `water_se_a.json` is the .json format parameter file that controls the training. It consists of three parts: the model, learning rate, and loss and training. The model section specifies how the deep potential model is built.

You can invoke the training by:

` $ dp train water_se_a.json`

The training will then occur with displaying the error of the model being tested every `disp_freq` batches with `numb_test` frames from the last set in the system. The results are output to `disp_file`. 

The outputs that are generated and shown in the command prompt display: first column shows the number of batches. Second and third columns show the loss function evaluated by `numb_test` frames chosen randomly from the test set and evaluated by the current training batch. The fourth and fifth columns display the RMS energy error (normalized by number of atoms) evaluated by `numb_test` frames randomly chosen from the test set and that evaluated by the current training batch, respectively.

Checkpoints are written to files every `save_freq` batches. You could also start from the checkpoint named `load_ckpt` if `restart` is set to `true`. 

### Freeze Model

Now that the model has been trained, we take the trained model can be frozen and dumped to a database, which is in the format `graph.pb`. To freeze a model, you can enter this into the command prompt, provided you are in the folder where the model is trained:

`$ dp freeze -o graph.pb`

### Use model to run simulation with native MD code

Now that the model has been frozen, there are many ways to use it, with the most straightforward test being the native MD code. This can be done by:

`$ dp test -m graph.pb -s /path/to/system -n 30`

Of course, `/path/to/system/` is signaled by `-s` and in this case refers to the directory containing the set files and `type.raw`. `-m` gives the tested model, which in our case is `graph.pb`. 

### Use model with LAMMPS to run simulation

The support of DeePMD for LAMMPS is implemented as a new "pair style," the standard command in LAMMPS, so it only requires a very small change to the input script file for LAMMPS simulations. In principle, according to the creators of DeePMD, the model trained by the kit can be called in any MD package during MD simulation. Only serial MD simulations are supported with the model. The current release of DeePMD-kit provides support for LAMMPS.

It is very simple to run a LAMMPS simulation with the trained model. You just need to specify the neural network in the LAMMPS input file:

`pair_style   deepmd graph.pb
pair_coeff
`
The command `deepmd` in the input file calls the DeePMD model to compute the atomic interactions in the MD simulations. The parameter `graph.pb` is the file containing the frozen model. `pair.coeff` should be left blank.


# Pitfalls and Troubleshooting

## Linux OS

If you are starting completely from scratch and want to run DeepMD-kit from a Windows PC, here is a video tutorial detailing how to use Oracle VirtualBox to set up and run a usable Ubuntu instance from your Windows PC. 

[YouTube Tutorial- How to Install Ubuntu on VirtualBox in Windows](https://www.youtube.com/watch?v=QbmRXJJKsvs)

In all, installing the DeepMD kit, LAMMPS, and all the components necessary to run them will take up roughly ~14 GB of disk space. Therefore, allocating at least **minimum 15 GB** of disk space to your Ubuntu VirtualBox virtual hard drive is necessary to run DeePMD-kit and LAMMPS. However, adding more is much better. Feel free to allocate as much disk space as you may see fit- however many GB you may decide to allocate- it is not all allocated at once, but rather it is allocated accordingly by how much space you have so far used in Ubuntu, so do not worry about allocating too much disk space and having it depleted from your main hard drive immediately. 

## Installing C++ Interface

This is where I ran into the most difficulty in installation. The most confusing step is where to define the "tensorflow_root" to be in the step `cmake -DTENSORFLOW_ROOT=$tensorflow_root -DCMAKE_INSTALL_PREFIX=$deepmd_root ..`. There is a thorough forum thread [here](https://github.com/deepmodeling/deepmd-kit/issues/10) that 

## MD: cannot make user in DeePMD-kit

Sometimes an issue may arise when trying to make user during the `cmake` process. Some unnecessary files may be produced in the `build` folder. To the best of my knowledge this problem can be fixed by navigating there and clearing those files:

`cd build
rm -r *`

And then retry the `cmake` process.

## Tensorflow Installation

You may run into a pitfall during the installation of tensorflow. I experienced trouble during this step, and was able to successfully install tensorflow using a different process. The original DeePMD-kit documentation leaves little instruction on how to accomplish this. While the installation steps may be straightforward, in case you are unfamiliar with Ubuntu and Linux and referred here, follow these steps.

`sudo apt-get install python3`

`sudo apt-get install python3-pip`

`pip install tensorflow`

Then, to verify the installation you can quickly create a small python file which utilizes tensorflow: Create a test file such as "tensor.py" and write these lines into it:


# More information on DeePMD-kit

Some further pitfalls of the package that may be problematic are that it only provides CPU implementation of the descriptor computation. This computation is parallelized by OpenMP. During the evaluation of energy, force, and virial in MD simulations, this computation is not parallelized. According to the authors of this paper, support will be provided in the future for parallel computation of descriptors via CPU multicore and GPU multithreading mechanisms. 


Most of the information I used for this brief tutorial was taken from "DeePMD-kit: A deep learning package for many-body potential energy representation and molecular dynamics" by Han Wang of the Institute of Applied Physics and Computational Mechanics in Beijing, among a few others from Princeton University. This paper can be accessed [here](https://arxiv.org/pdf/1712.03641.pdf). While I personally would probably not be able to attest to the validity and robustness of the research, but it appears to be a pretty good and thorough resource on the DeePMD-kit package. 











