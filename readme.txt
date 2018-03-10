This repository contains the below files:
1. Latent Matrix Factorization for Movie recommendation - the PDF write-up
2. 3 iPython files. One corresponding to the main programme (performs matrix factorization and calculates MRR and RMSE 
with best found rank and lambda), one that performed grid-search over rank and lambda (regularization constant), 
one that proved the convergence of SGD
3. Results.xlsx - contains all the MRR and RMSE values calculated over 36 permutations of rank and lambda
4. splitData.py - this file was used to split the data into training and test set (3 folds)
5. The output of splitData.py are the 6 .csv files (2 files (test and train) per fold)
6. ml-20m : http://files.grouplens.org/datasets/movielens/ml-20m.zip


About the dataset:
the key file of interest is ratings.csv which contains the ratings some users gave to some movies on a 5-star scale 
with half-increments (e.g. 0.5 stars to 5.0 stars). On each line, the file has a rating with the following 
format (userId; movieId; rating; timestamp). If you want additional information about the movies, you can find it in the 
file movies.csv which has a row per movie containing the (movieId; title; genres) where genres is a pipe-separated list 
describing what categories the movie is in (e.g. Action, Adventure, etc.).
