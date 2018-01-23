# Python Hackathon - Problem 1 dataset

<img src="../qcbCollaboratory_logo.png" height="50"/>

The dataset used in this problem was kindly provided by [Dr. Julia Mack](https://www.linkedin.com/in/julia-mack-0790a52/) from the [Arispe Lab](https://arispelab.mcdb.ucla.edu/), and was used in [their recent publication on Nature Communications](https://www.nature.com/articles/s41467-017-01741-8). To return to the problem statement, [click here](./Readme.md)!!

<br />
### Samples of 600s calcium imaging

* [Notch1KD_JMackNatComm2017_samples.hdf5 (4.7G)](https://drive.google.com/open?id=1WeNKYMnC6FqVK5IeVbYVC6DkGD2KDlfR)

This h5 file contains 4 datasets:

```
>>> f = h5py.File('Notch1KD_JMackNatComm2017.hdf5', 'r')

>>> f.keys()
[u'slide1', u'slide2', u'slide3', u'slide4']

>>> f['slide1']
<HDF5 dataset "slide1": shape (600, 1024, 1024), type "<f8">
```

Each slide contains a NumPy array of shape (600,1024,1024).


<br />
### Fmin & Fmax

* [Notch1KD_JMackNatComm2017_fmaxfmin.hdf5 (65MB)](https://drive.google.com/open?id=1IQMw7qIfedoTYMb7QDQUTBEjwHxu5jgF)

Similarly to the previous file, this h5 file contains 4 datasets:

```
>>> f = h5py.File('Notch1KD_JMackNatComm2017_fmaxfmin.hdf5', 'r')

>>> f.keys()
[u'slide1', u'slide2', u'slide3', u'slide4']

>>> f['slide1'].keys()
[u'fmax', u'fmin']

>>> f['slide1']['fmax']
<HDF5 dataset "fmin": shape (1024, 1024), type "<f8">
```

Each slide contains a NumPy array of shape (600,1024,1024).



<br />
### Example of masks for Track 2

* [Notch1KD_JMackNatComm2017_fmaxfmin.zip (100KB)](https://drive.google.com/open?id=1mlMk2SelT_62Rm0TA_FEqm_mDKhHRAHB)

In case you decide to go directly to Track 2, this file contains one possible mask obtained from Track 1.
