# autoanno 0.1dev1 (in planning)

# Introduction

The original idea behind this project was to test a new clustering algorithm for network data.
Originally this was simply a bin for my CS 7280 (Network science, taught by Konstantine Dovrolis at Georgia Tech) 
coursework, but since I have decided to expand it into a tool for usage with network and text-based data embeddings.
This was accomplished by the following steps:

	1. Get network datasets from [Index of Complex Networks (ICON)](https://icon.colorado.edu/#!/)
	2. Use [deepwalk](https://github.com/phanein/deepwalk) for "representation learning" 
		(intelligently mapping network data to a vector space)
	3. Apply various persistent homology tools from [Gudhi](https://gudhi.inria.fr) to find hidden topologies.
	4. Use some topological metric as a means for cluster determination.
	5. Analyze the significance of this algorithm statistically by using generated networks with matching properties. 
	
Now, however, it has come to my attention that NLP is a hot topic in the data science world. One problem with NLP is
the fact that in order to use text based data in supervised learning, annotation by hand is typically required in
order to create training and testing datasets. While there are other options, such as using auto-ml to generate 
data, I find this unsatisfactory. Therefore, I've made it a personal goal of mine to figure out how to circumvent
the annotation process. When querying the field of data scientists (literally just asking for conversations via LinkedIn)
there has never been a positive response to this question. The discussion begins and ends at "it's a necessary evil". 
This project is merely an investigation towards whether or not there are any alternatives. 

# Agenda and Methodology. 

As text-based data and graphs are closely related, the project will create a user-friendly API which makes
networkx, representation learning, word2vec, etc. accessible so that graph based methods can be used for 
text based data. There are a number of various metrics that can be investigated, the two categories that stand
out are clustering and node centrality. 

1. Clean and explore network and or text based data
2.a For network data: use deepwalk for representation learning (nodes and edges mapped into a vector space)
2.b For text data: Use some embedding algorithm, I am leaning towards word2vec. 
3. Write scripts (.bat) for deepwalk, as it is accessed primarily through command line executables. 
4. Create an API that wraps pytorch/gensim algorithms,
5. Write wrappers/API for Gudhi persistent homology package
6. Determine if persistent homology provides a statistically significant improvement over other algorithms.
4. Interpret persistent homology data in the context of learned representation and original network.

The null hypothesis for these investigations will always be of the form: does persistent homology capture {property}
of {dataset} better than other algorithms? The is quantified by the distribution of scores for whatever metric or
property is being investigated. Additionally I think it is worthwhile to experiment with whether or not structure
is being detected where none exists. 


A. Perform same calculations on random networks as a null hypothesis
B. Calculate community structure with networkX and compare.
C. Performance comparisons?

Goal that is likely harder than it seems:
Finding subgraphs which correspond to most persistent Betti number events.
What happens to the network when all but the most persistent components are pruned?

 

