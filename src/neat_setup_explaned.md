
[NEAT]
```
I want maximize my score
```
fitness_criterion  = max

```
This is limit score to the agent
```
fitness_threshold  = 1000

```
This is quantity of the agents by generation
```
pop_size = 100

```
Give me an error, when don't evolution, anymore instead of redefining
```
reset_on_extinction   = False

```
Genome is the conections between the nodes
```
[DefaultGenome]

<br />
# node activation options
```
Set the Tangent Hiperbolic function to nodes activation 
```
activation_default      = tanh
activation_mutate_rate  = 0.0
activation_options      = tanh

<br />
# node aggregation options
```
Set how to agregate the calcules between nodes and the conections weight
```
aggregation_default     = sum
aggregation_mutate_rate = 0.0
aggregation_options     = sum

<br />
# node bias options
```
Set range values to the 'bias'
```
<br />
```
define the mean value to 'bias'
```
bias_init_mean          = 0.0
<br />
```
define the default deviation of the value 'bias'
```
bias_init_stdev         = 1.0
<br />
```
define the maximum value to 'bias'
```
bias_max_value          = 30.0
<br />
```
define the minimum value to 'bias'
```
bias_min_value          = -30.0
<br />
```
here reduces mutation power to half, because the 'bias' is multiplied by this value in each generation
```
bias_mutate_power       = 0.5
<br />
```
define the chance to mutation between generations to 70%
```
bias_mutate_rate        = 0.7
<br />
```
define the chance to create a new value to 'bias' from scratch
```
bias_replace_rate       = 0.1
<br />

# genome compatibility options
```
Set the limit values to a same specie
```
compatibility_disjoint_coefficient = 1.0
compatibility_weight_coefficient   = 0.5
<br />

# connection add/remove rates
```
Set probablites to remove or include a node conection
```
conn_add_prob           = 0.5
conn_delete_prob        = 0.5

<br />

# connection enable options
```
Set conections actives
```
enabled_default         = True
enabled_mutate_rate     = 0.01
<br />
```
Set the direction network will be processed
```
feed_forward            = True
initial_connection      = full

# node add/remove rates
node_add_prob           = 0.2
node_delete_prob        = 0.2

<br />
# network parameters
```
Set how much inputs, outputs and middle nodes is have
```
num_hidden              = 0
num_inputs              = 3
num_outputs             = 1

<br />
# node response options
```
set configuration of the output node
```
response_init_mean      = 1.0
response_init_stdev     = 0.0
response_max_value      = 30.0
response_min_value      = -30.0
response_mutate_power   = 0.0
response_mutate_rate    = 0.0
response_replace_rate   = 0.0

# connection weight options
weight_init_mean        = 0.0
weight_init_stdev       = 1.0
weight_max_value        = 30
weight_min_value        = -30
weight_mutate_power     = 0.5
weight_mutate_rate      = 0.8
weight_replace_rate     = 0.1

[DefaultSpeciesSet]
compatibility_threshold = 3.0

[DefaultStagnation]
species_fitness_func = max
max_stagnation       = 20
species_elitism      = 2

[DefaultReproduction]
elitism            = 2
survival_threshold = 0.2