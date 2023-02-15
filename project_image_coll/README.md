# Automated data collection system for convolutional neural networks

## Overview

A service that allows the developer of convolutional neural networks or datasets for them to quickly create a dataset from images from a selected source with the ability to specify the desired number of images

**Features:**
* Data collecting
* Searching and sorting data
* Secure uploading and storing images

**Technologies used:**
* Python
* Selenium
* Requests
* ChromeDriver
* Shutil

**Dependencies**
 

## Getting started

### Install the App
Clone the repository:

```sh
$ git clone https://github.com/IThinkthisisKazan/Python.git
$ cd Python
```

Examples of data filling:

1)find_and_separate -- is main function, they have a 5 attributes (theme, quantity, path, separation_one, separation_two),
2)theme -- "cats dogs mouse",    *its your response
3)quantity -- "100",   *amount of picture
4)path -- " "C:\\Users\\Acer\\Pictures" "   *The place where you want to download all the pictures
5)separation_one -- "30"  *\
                            The proportions you want to divide (the amount must not be more or less than 100!)
6)separation_two -- "70"  */
