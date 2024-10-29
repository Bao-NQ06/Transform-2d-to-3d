# Transform 2d image to 3d image using point cloud
This project demonstrates how to transform a **2D image into a 3D representation** using a **point cloud**. A **point cloud** is a collection of points in 3D space, where each point represents the **X, Y, Z** coordinates of the object or scene.
## Introduction
While 2D images represent visual information using **height and width** (X, Y), they lack **depth (Z)** information. Converting a 2D image into a **3D point cloud** allows us to add this depth dimension, making it useful for **3D visualizations**, **reconstructions**, and other computer vision tasks.

A **point cloud** generated from a 2D image assigns **pixel coordinates (X, Y)** and **intensity or depth values (Z)** to each point, creating a spatial map of the original image. 
## Installation
### Prerequisites
Ensure you have Python 3.7 or higher installed, along with pip to manage dependencies.

### Install Dependencies
1. Clone the repository:
```bash
git clone https://github.com/Bao-NQ06/Transform-2d-to-3d.git
cd Transform-2d-to-3d
```
2. Enviroment setup: Recommends creating a virtual environment and installing dependencies via pip. Use the following commands to set up your environment:
We also recommend using pytorch>=2.0 and cuda>=11.8, though lower versions of PyTorch and CUDA are supported.

* On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```
* On MacOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install Dependencies:
Make sure to install all dependencies listed in requirements.txt:
```bash
pip install -r requirements.txt
```
4. How to use:
* If you prefer visually through local webbapp for more convenient. Run:
```bash
streamlit run main.py
```
The program will run in your local host.
If you want to close the local webbapp. Press Ctrl + c in terminal.

* If you want to run step by step to understand the way its work. Run:
```bash
python transform_3d.py
```
* You can replace image path with your own image path for more experience


5. Deactivate the Virtual Environment: When you are done, deactivate the virtual environment by running:
```bash
deactivate
```
