# Deep-Learning-MD: Installation(s) Tutorial

# Table of Contents
- [SIESTA Installation](#SIESTA-Installation)

# SIESTA Installation

First, open the Linux terminal in the home directory. Then, clone the SIESTA repository from GitLab:

`git clone https://gitlab.com/siesta-project/siesta.git`

You may need to install a few dependencies first:

`sudo apt install git gfortran make`

Then, navigate to the siesta directory to compile an executable file:

`cd siesta-4.1-b2/`

`cd Obj/

`sh ../Src/obj_setup.sh`

`cp gfortran.make arch.make`

`make`

There will then be a lot of output messages in the terminal, and if successful, you will have a working SIESTA executable.

Running
