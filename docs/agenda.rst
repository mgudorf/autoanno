Agenda
======

Create a MVP as fast as possible. Goal is to investigate whether TDA can be used to create an unsupervised algorithm
for automatically producing annotations and labels for relatively simple data. Key features include:

- Find datasets which can be used to for classification and or clustering purposes.
- Clean and explore the data
- Wrangle the data to get into a form compatible for tools such as [word2vec]_ and [deepwalk]_.
- Use these tools to encode data as vectors.
- Use simple models as baselines for classification and clustering. (logit, KNN)
- Apply Topological data analysis on these vectors to produce clusters ([ToMATo]_ algorithm then a custom algorithm)
- Compare TDA results with baselines using statistical analysis.

As the main goal here is to investigate whether unsupervised and or automated machine learning can be used for the
purpose of annotation of data, the model will be graded as a classification algorithm.

Success will be defined