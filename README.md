
| Project                               | Created    | Updated    | Version |
|---------------------------------------|------------|------------|---------|
| Re-implementing the Bellkor Algorithm | 06/01/2018 | 27/01/2018 | 0.1.0   |

# Motivation

#### Short Answer

Implement an Algorithm that had previously won a Data Science / well known competition, in this case the Netflix Grand Prize.

#### Long Answer

Firstly, recommendation systems are becoming more and more prevalent as companies are starting to become more data-driven and seeking to improve the customer experience. Its hard deny that personalisation is key in maintaining customer loyalty and engagement of a particular service. Therefore to gain an understanding and appreciation of the methods and implementation details of this algorithm I believe that its a good point in my career to learn and implement one from scratch.

Secondly, I enjoy the challenge of implementing from scratch algorithms and systems in my own time primarily to learn how to translate complex ideas into code. Also the feature engineering that was applied and used to predict the ratings and is explained and derived very well in the [paper](https://netflixprize.com/assets/GrandPrize2009_BPC_BellKor.pdf) is very clear and concise. Finally, the challenge of retracing the steps the original researchers/developers might have taken to get to their own implementation is definitely a learning strategy I like to pursue.

# Bellkor Algorithm

This is an implementation of the “BellKor’s Pragmatic Chaos” final solution, which eventually went on to win the Netflix Grand Prize. 

The purpose of this algorithm is to predict the ratings using the Bellkor Algorithm. The algoritm uses novel [Feature Engineering](https://en.wikipedia.org/wiki/Feature_engineering) in order to model the temporal properties of the users and times over time.

# Demo and usage

I've created a IPython Notebook [here](resources/Demo.ipynb) which showcases the implementation.

# Acknowledgments

'Yehuda Koren and the Bellkor Pramatic Choas Team' - for documenting the solution in the paper, located [here.](https://netflixprize.com/assets/GrandPrize2009_BPC_BellKor.pdf)

# Links

*   [MovieLens 20M dataset](https://grouplens.org/datasets/movielens/) - differs from the original but same as the one used in the demo.
*   [Netflix Grand Prize Info](https://en.wikipedia.org/wiki/Netflix_Prize) - overview of the original competition.

# Testing

Run the following command to start the test suite:

```
    pytest tests
```

#### Coverage

```
    67%
```

# TODO

*   Document results using the MovieLens 20M Dataset
*   2 Part - Blog Post (1 of 2 complete.)
