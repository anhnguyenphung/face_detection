# Face detection in pictures and webcam using OpenCV in Python

## How to use the project
You can use this project by cloning the repository with Git command:
```shell
git clone https://github.com/anhnguyenphung/face_detection
```
Then move to the directory that you just have cloned by running the following command in the terminal:
```shell
cd face_detection
```

## Detect faces in pictures
To detect faces in a picture, run the following command in the terminal:
```shell
python face_detection.py image_file
```
where ```image_file``` is the location of the image file (in **JPG** or **PNG** format) that you want to detect faces. There are some example pictures in the folder 
```example_pictures``` of the repository, or you can choose your own pictures, to test out.

For example, ```python face_detection.py example_pictures/example_1.jpg``` would produce the following output:

![example1-photo](https://github.com/anhnguyenphung/face_detection/blob/master/pictures_for_readme/picture1.png)

```python face_detection.py example_pictures/example_2.jpg``` would produce the following output:

![example2-photo](https://github.com/anhnguyenphung/face_detection/blob/master/pictures_for_readme/picture2.png)

## Detect faces in webcam
To detect faces in webcam, run the following command in the terminal:
```shell
python webcam_face_detection.py 
```
For example, when I ran the above command on my terminal, I had the following output:

![example3-photo](https://github.com/anhnguyenphung/face_detection/blob/master/pictures_for_readme/picture3.png)

## Conclusion
From this project, I have learned how to use OpenCV library in Python for face detection, thanks to blog posts from [Real Python](https://realpython.com/).
