# DIGIT RECOGNIZER
In this project Simple handwritten degit recognizer is created using python
## How To Install and Run the program.

* ### For Windows Users
#### To Run project 

```
powershell
> git clone https://github.com/swapnillondhe24/digit_recognizer .\Digit_Recognizer
> Explorer Digit_Recognizer
```
1. Open **[Capture.png](https://github.com/swapnillondhe24/digit_recognizer/blob/master/capture.png)** in paint.
2. In powershell Run Predictor_live.
3. keep drawing and Ctrl+Z to clear and draw again.

#### To Generate Dataset for project 
1. Open **[Capture.png](https://github.com/swapnillondhe24/digit_recognizer/blob/master/capture.png)** in paint.
2. In Powershell Run **[screencapture.py](https://github.com/swapnillondhe24/digit_recognizer/blob/master/screencapture.py)**
3. Keep drawing the digit told in powershell withing the given interval. use Ctrl+Z for clearing screen
4. By default the program is set to capture 50 images for each digit.
5. Once all the images are captured. Verify images by visiting Orig_images folder and respective digit folders.
6. Run gendataset.py and wait for generation of dataset.csv file
7. Run svmstarter.py, 
> tweak SVM the parameters and model name if required for better results. Do share your tweaked parameters by branching or creating pull request
8. Once model is generated run the project by above method.
     
     
