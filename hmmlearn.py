from hmmlearn import hmm
import numpy as np

states = ['Rainy', 'Sunny']
observations = ['walk', 'shop', 'clean']

model = hmm.MultinomialHMM(n_components=2)
model.startprob_ = np.array([0.6, 0.4])
model.transmat_ = np.array([[0.7, 0.3],
                            [0.4, 0.6]])
model.emissionprob_ = np.array([[0.1, 0.4, 0.5],
                                [0.6, 0.3, 0.1]])

# predict a sequence of hidden states based on visible states
bob_says = np.array([[0, 1, 2]]).T
logprob, alice_hears = model.decode(bob_says, algorithm="viterbi")

print ('log probability: ', logprob)
print ("Bob says:", ", ".join(map(lambda x: observations[x], np.asarray(bob_says).reshape(1, -1)[0,:])))
print ("Alice hears:", ", ".join(map(lambda x: states[x], np.asarray(alice_hears).reshape(1, -1)[0,:])))
