# Genetic Improvement Optimisation of Runtime Performance Using Reinforcement Learning



ABSTRACT
Genetic Improvement (GI) is a new field in software engineering that mutates programs to identify better versions of already-existing software. However, the choice of location and mutation type in GI is currently done randomly, causing several uncompilable and inadequate generated program variants. To combat this problem, we propose a new selection strategy, based on Reinforcement learning (RL), precisely Q-learning, as a better selection strategy for selecting mutation types in GI. Our proposed Q-learning-based approach uses epsilon-greedy, a probabilistic selection strategy, to select a mutation type for a code edit in software. To find the most efficient epsilon-greedy hyper parameter we have run four different alpha values and analysed their performances (0.1,0.3,0.5,and 0.85). We have found that alpha 0.1 is the most efficient learning rate for our approach. In addition to that we discovered that our approach is far more efficient in selecting a mutation type and improving software’s runtime performance than random selection, reducing the runtime of MOEA/D by 15 seconds while random selection only improved the software’s runtime by 1 second. Nevertheless, while Q-learning-based mutation selection is more efficient than random selection, our approach takes 5 times longer to generate a patch than random selection.


## Prerequisites
* [Python 3.5+](https://www.continuum.io/downloads)
* [srcML](https://www.srcml.org/#download) (optional if you want to use the XML engine on srcML translated files. [example](https://github.com/coinse/pyggi/blob/master/example/repair_java.py))

## Documentation
You can find the PYGGI's documentation
The pdf file is available at [link](https://dl.acm.org/citation.cfm?id=3341184).

## Getting Started

#### 1. Clone the repository
```bash
$ git clone ~
$ cd PYGGI
```

#### 2. Install
```bash
$ python setup.py install
```

#### 3. Generate MOEA/D Patches
##### 1. Improving runtime of MOEA/D 

```bash
$ cd example
$ python improve_MOEAD.py
```

#### 3. Validating MOEA/D Patches
##### 1. Improving runtime of MOEA/D 

```bash
$ cd example
$ python validate_moead.py
```

