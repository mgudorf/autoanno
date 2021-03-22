Investigating Annotation via AutoML and TDA
===========================================

Create a MVP as fast as possible. Goal is to investigate whether TDA can be used to create an unsupervised algorithm
for automatically producing annotations and labels for relatively simple data. Key features include:

- Find datasets which can be used to for classification and or clustering purposes [X]
  I am going to use Taskmaster 2 data set.

- Clean and explore the data

- Wrangle the data to get into a form compatible for tools such as word2vec or deepwalk
  the former most likely accessed via gensim or pytorch

- Use these tools to encode data as vectors.

- Use simple models as baselines for classification and clustering. (KNN, other algs)

- Apply Topological data analysis on these vectors to produce clusters (ToMATo algorithm maybe a custom algorithm)

- Compare TDA results with baselines using statistical/error analysis. Could use external clustering based metrics or
  more familiar metrics like F-measure.

As the main goal here is to investigate whether unsupervised and or automated machine learning can be used for the
purpose of annotation of data, the model will be graded as a classification algorithm.
Success will be defined by

1. The TDA algorithm has better results (in some metric to be determined) than other unsupervised learning algorithms
2. The clustering/annotation is of sufficient accuracy to be deployed as a business solution. I.e. meets accuracy threshold.

For speed, this will primarily be done in notebook format.
