# Analysis of calcium imaging

<img src="../qcbCollaboratory_logo.png" height="50"/>

In this problem, we will practice a number of common methodologies for the analysis of calcium traces. Differently to the other projects proposed in this Hackathon, this project is more educational and aims at giving hands-on practice with Python and Jupyter Notebooks. Using videos of fluorescent calcium-indicator Oregon Green (OGB-1) in endothelial cells, we will practice:

1. a simple method to segment cells;
2. extract fluorescence time series of a set of cells;
3. and estimate their calcium concentration and other population statistics.

As extra activities, participants may also use this dataset to learn how to automate pipelines for image processing and create videos such as [this one](https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-017-01741-8/MediaObjects/41467_2017_1741_MOESM4_ESM.mp4) using a few lines of code in Python.


<img src="resources/notch1_vid_natcomm.gif" width="600" />

The dataset used in this problem was kindly provided by [Dr. Julia Mack](https://www.linkedin.com/in/julia-mack-0790a52/) from the [Arispe Lab](https://arispelab.mcdb.ucla.edu/), and was used in [their recent publication on Nature Communications](https://www.nature.com/articles/s41467-017-01741-8).

### Primary goal

From the discussions in the Hackathon, we will publish a notebook which will provide an example of how to extract and analyse calcium dynamics form a video. This notebook will be available publicly to everyone, and other people from the QCBio community will be able to use it as an additional resource for this kind of analysis.


### Technical challenges

* Handling images and videos with python

* Dealing with photobleaching and estimating calcium concentration

* Applying regression on a set of time series

* Extracting statistics based on a set of cells

* [extra] Automating a pipeline using parallel processing

* [extra] Creating animations based on data


### Dataset

The data is provided [here](./Dataset.md). It consists of two h5files that contain: one with the calcium traces from four samples, and the other with measurements of Fmax-Fmin ([see paper](https://www.nature.com/articles/s41467-017-01741-8) for more details).


<br />


## Track 1 - Segmenting and separating cells

#### Guideline

1. Let's start by downloading the file ```Notch1KD_JMackNatComm2017_samples.hdf5```. Import the h5 file into your Python environment (*hint:* h5py). You should have access to 4 samples, called ```sample1```, ```sample2```, ```sample3``` and ```sample4```. Each sample is a 1024x1024 video of 600 seconds. Choose one of them and use this sample to figure out how to identify and index the cells, then apply your solution to the other files.

2. Plot a few frames of your video. Using shape
    * *Optional:* Often the file you have access to is not in a video format. Create a video of it using [this script](./resources/make_video_raw.py).
    * *Optional:* Add comment lines to the script, explaining what each line does.


3. Find the average fluorescence of the whole video as a function of time. Plot it and interpret what is happening.

4. Use operations from libraries [scikit-image](http://scikit-image.org/) and [OpenCV](https://opencv-python-tutroals.readthedocs.io/en/latest/index.html) to separate each cell. There are many ways to do it, the easiest way is to identify the region around each nucleus and use it to segment the image. We share below the steps to achieve that.

    * Select specific frames an try some filters on it. For instance, try using a median blur and thresholding it. Use this first step to get some feeling of how these tools affect the images.

    * Use filters and thresholds to turn the regions close to each of the nuclei into "blobs" (see example below).

    <p align="center"><img src="resources/blobs_example.png" height="150" /></p>

    * Use blob detection techniques. *Hint:* Take a look at scikit-image's ```measure.label()``` function.

    * Post-process your results.

5. You should now have set of subregions of your image where you can find each cell. This is called a **mask**. Write a small code that, given the ID of a cell, it plots the average fluorescence in the corresponding region as a function of time.

6. Export your results using NumPy's ```savetxt()``` function. We recommend that you use an array of shape ```(Ncells,600)```, where Ncells represents the number of cells found by your code.

7. *Optional*: On top of a plot with one of your frames, use matplotlib's ```text()``` function to show what is the id of each of your cells (see below an example).



#### Resources

* For blob detection:
  * [Blob detection on Learn OpenCV](https://www.learnopencv.com/blob-detection-using-opencv-python-c/), Satya Mallick's website dedicated to sharing ideas and tutorials on computer vision.
  * Scikit-image's [page on blob detection](http://scikit-image.org/docs/dev/auto_examples/features_detection/plot_blob.html)
  * [Here's an example](https://www.youtube.com/watch?v=4DynOyNN_FI&t=2s) of what you can accomplish with such techniques.




## Track 2 - Removing photobleaching and estimating calcium concentration

#### Guideline

1. In point 3 of Track 1 we visualized the average fluorescence as a function of time. The drop in the basal line is called [photo bleaching](https://en.wikipedia.org/wiki/Photobleaching). Find a way to fix it and plot the new average fluorescence.

2. Use the mask obtained in point 5 from Track 1 to examine the fluorescence of each cell. If you decided to go directly to Track 2, you can download a sample of mask [here](./Dataset.md). Is there still residual photobleaching? If yes, correct it per cell.

3. Let's start by downloading the file ```Notch1KD_JMackNatComm2017_fmaxfmin.hdf5```. Import the h5 file into your Python environment. This gives you the measures of Fmax and Fmin for each sample.

4. Estimate the Fmax and Fmin per sample (**or** per cell). Note that Fmax and Fmin are taken after the whole experiment, and should be corrected for photobleaching too.

5. To convert from fluorescence to calcium concentration, use the formula below (Kd=170nM is the [dissociation constant](https://en.wikipedia.org/wiki/Dissociation_constant) of OGB-1):

<p align="center"><img src="https://latex.codecogs.com/gif.latex?%5Cdpi%7B300%7D%20%5Cfn_phv%20%5BCa%5E%7B2&plus;%7D%5D%20%3D%20K_d%20%5C%2C%20%5Cdfrac%7BF%20-%20F_%7Bmin%7D%7D%7BF_%7Bmax%7D%20-%20F%7D" height="40" /></p>

6. Plot the distribution of average calcium distribution for each slide.


#### Resources

* [Chemical calcium indicators](http://www.sciencedirect.com/science/article/pii/S104620230800159X), Methods 2008 by Paredes, Etzler, Watts, Zheng & Lechleiter

* [More about the formula used in the quantification of calcium](https://www.embl.de/eamnet/html/calcium/quantifying1.htm), by EAMNET.

* [How to calculate moving average](https://stackoverflow.com/questions/14313510/how-to-calculate-moving-average-using-numpy) using numpy.



<br /><br />

## Extra 1 - Automate the pipeline

#### Challenge

Create a single Python module that applied the pipeline on a set of these images. Given enough memory, many of these computations can be performed in parallel.


## Extra 2 - create a video!

#### Challenge

Matplotlib has an [animation module](https://matplotlib.org/api/animation_api.html). Creates a video as
[this one](https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-017-01741-8/MediaObjects/41467_2017_1741_MOESM4_ESM.mp4) based on your work.
