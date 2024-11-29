# Create a new python virtual environment 

 Use the venv module to create the virtual environment:
 ```
python -m venv myenv
 ```
 Replace myenv with your desired environment name.
###  Activate the Virtual Environment
On Windows:
```
myenv\Scripts\activate
```
On macOS/Linux:
```
source myenv/bin/activate
```
After activation, your terminal prompt will change, showing the name of the virtual environment.
___
# Remember Numbers
This code implements a "Remember Numbers" game where players recall an expanding sequence of numbers displayed briefly. The game progresses through rounds, generating and displaying a random number sequence. Players input the sequence; correct entries advance to the next round, while errors end the game. Commands "quit" exits the game, and "reset" restarts it. Sequence visibility decreases with higher rounds. 
___
# Remove background of image using rembg package
This code uses the **rembg** package to remove the background from an image. It opens an input image (photo_1.jpg), processes it to remove the background, and saves the result as result.png.
___
# Generate a Chessboard Pattern
This code generates a chessboard pattern with n rows and m columns using ⬜ and ⬛. The pattern alternates based on the sum of the row and column indices ((i + j) % 2).