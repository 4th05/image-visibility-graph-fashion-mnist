# Image Visibility Graphs and Visibility Patches in Machine Learning

This repository contains the source code used for a comprehensive study on the viability of features extracted from Image Visibility Graphs (IVG) and Visibility Patches (VP) in different machine learning contexts.

## Overview

Visibility Graphs, originally designed to represent time-series data as graphs, have been adapted into Image Visibility Graphs and Visibility Patches for image processing. Despite their innovative application, the exploration of their use in machine learning tasks is lacking in existing literature.

This study aims to fill this gap by exploring and evaluating the potential of IVG and VP as robust features for diverse class identification tasks. The Fashion MNIST dataset, chosen for its balanced distribution and minimal preprocessing needs, provides a realistic context for this investigation.

The comprehensive methodology includes dataset loading, feature extraction using IVG and VP, dimensionality reduction via Scaling and PCA, and the application of machine learning algorithms. The study covers both supervised learning scenarios, using classifiers such as Random Forest (RF) and Support Vector Machine (SVM), and unsupervised learning scenarios, employing partition detection algorithms like k-means and Louvain.

## Repository Structure

The repository is organized as follows:

- `main.ipynb`: A Jupyter notebook that contains all the steps and analysis of the study, as reported in the corresponding article.
- `src`: This directory contains all relevant source code for the project, including the implementation of IVG, HIVG, and VP.

## Getting Started

You can clone this repository to your local machine to reproduce the results and modify the code. Make sure to install all necessary Python libraries, as imported in the `main.ipynb` notebook and the source code files in the `src` directory.

## Contact

For any questions or suggestions regarding this work, please contact the author at `athos.m.moraes@gmail.com`.

## Conclusion

Through this study, we discovered that features extracted from IVG and VP can effectively enhance the performance of supervised classification tasks. However, these features face challenges in distinctly classifying the categories within the Fashion MNIST dataset in unsupervised learning tasks. This calls for more in-depth research and potential enhancements to the techniques to optimize their use in diverse machine learning contexts.
