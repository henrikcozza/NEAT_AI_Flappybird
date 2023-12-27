## NEAT_AI_Flappybird
This project is an AI with learns to play a clone from Flappybird using Neural Evolution with Augmenting Topology NEAT.
<br />
<br />
<br />
![running game gif](assets/running.gif)
<br />
<br />
<br />
### How this work
The model receive some data inputs to take a decision in output.

Data inputs to the model:
 - position Y of bird
 - distance between the bird and the top tube
 - distance between the bird and the down tube 

Data output to the model is the action to jump or not jump.

Using the inputs that are multiplied with a weight, the result is used in a function called hyperbolic tangent. This function subtracts a bias value and returns a value between -1 and 1. If the value is greater than 0.5, the action is to jump; if it is less than 0.5, no action is taken.


### Use

```shell

 > cd NEAT_AI_Flappybird

 > pip install -r requirements.txt

 > python3 ./src/main.py


# optional

 > pytest

# optional to watching tests

 > pwt
```

