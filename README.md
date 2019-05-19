# HMM-POC
A simple implementation of the Hidden Markov Model in Python.

### Structure
hmmlearn.py : A multimonial HMM model is implemented using [hmmlearn](https://hmmlearn.readthedocs.io/en/latest/tutorial.html#available-models) library.

viterbi.py : Includes the implementation of Viterbi algorithm from scratch.

## Scenario

Consider two friends Alice and Bob, who live far apart from each other but they talk to each other daily over the telephone about what they did that day. Bob is only interested in three activities: walking in the park, shopping, and cleaning his apartment. The choice of his activity is determined exclusively by the weather on a given day. Alice has no definite information about the weather, but she knows the general trends of Bob. Based on what Bob tells her he did each day, Alice tries to guess what the most likely weather for that day at Bobs place might be.

Alice believes that weather operates as a discrete Markov chain. There are two states, "Rainy" and "Sunny", but she cannot observe them directly since they are hidden from her. On each day there is a certain chance that Bob will perform one of the following activities, depending on the weather: "walk", "shop", or "clean". Since Bob tells Alice about his activities and Alice can directly observe them, these are the observations.

This implmentation assumes that the transition, emission and initial probabilies are a priori knowledge. The assumed probabilities are shown in the diagram given below. 

![Example hmm model](https://github.com/kniveditha/HMM-POC/blob/master/wiki-ex.PNG)
