[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14750862&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS110 Final Project  << Semester, Year >>

## Team Members

Chanwoo Lee

***

## Project Description

This is a brief game for protecting meteor.
The screen will be divided into n^2 sections depending on the level, and an increasingly larger circle will appear in each section at random intervals.
This circle can be reduced in size by clicking on it, and when the radius becomes 0, it is judged to have disappeared.
As time goes by, as the level increases, the number of sections will increase, and the cycle of circles appearing and the speed at which the circles grow will become faster.
Thinking about some special circles which are not to be touched in ceratain instance, or blinking, flashing.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Start Menu
2. Level Design
3. Scoring System
4. Game Over Screen
5. Obstacle Collision

### Classes
class Meteor:
    
    def __init__(self,x,y,radius,img_files):
        """
        Initiatlize the meteor's position
        Args:
            x : int - the x coordinates of center of meteor
            y : int - the y coordinates of center of meteor
            radius : int - the radius of meteor
            img_files : str - path to meteor image
        """
    
    def term(self):
        """
        determine the term of meteor coming (random)
        """
        
    def terminated(self, radius, score):
        """
        Boolean operator if radius got smaller than 0. If it is, terminate the meteor image
        Args:
            radius : int - radius of meteor image
            score : int - level*certain number, get bigger when the meteor got terminated
        """
   
class Level:
    def pushing(self, radius, push, event, level):
        """
        If the meteor got clicked, disminish it's radius by certain amount.
        Args:
            radius : int - radius of meteor image
            push : int - reduce radius by 'push' amount
            event : - sense whether there was a click from user
            level : int - determine the amount of push
        """
        
    def size_rate(self,radius, level, rate):
        """
        Determine the rate of the meteor radius's getting bigger
        Args:
            radius : int - radius of meteor image
            level : int - determine the rate of getting bigger
            rate : int - determine how fast the radius getting bigger by milisecond. 
        """
    
    def score(self, timer, level, score):
        """
        Record time passing for change levels and score
        Args:
            timer : int - record time passing by milisecond to change level
            level : determine the rate of getting bigger, elevated in every 600 second
            score : recorded for level*milisecond
        """
    

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
