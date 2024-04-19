
| Project                               | Created    | Updated    | Version |
|---------------------------------------|------------|------------|---------|
| Re-implementing the Bellkor Algorithm | 06/01/2018 | 05/04/2020 | 0.1.0   |

FYI - This is no-longer actively maintained!

# Motivation

#### Short Answer

Implement an Algorithm that had previously won a Data Science / well known competition, in this case the Netflix Grand Prize.

#### Long Answer

Firstly, as companies increasingly adopt data-driven approaches and prioritize enhancing customer experiences, recommendation systems are gaining prominence. It's evident that personalization is crucial for fostering customer loyalty and engagement. Therefore, delving into the intricacies and implementation of these algorithms seems opportune for advancing my career.

Secondly, I relish the task of building algorithms and systems from scratch in my spare time, primarily to master the art of translating intricate concepts into code. Moreover, the paper's elucidation of feature engineering used for rating prediction is exceptionally clear and succinct. Lastly, I find great value in the challenge of retracing the footsteps of original researchers and developers to understand their implementation strategies, which aligns with my preferred learning approach.

# Bellkor Algorithm

This is an implementation of the “BellKor’s Pragmatic Chaos” final solution, which eventually went on to win the Netflix Grand Prize.

The purpose of this algorithm is to predict the ratings using the Bellkor Algorithm. The algorithm uses novel [Feature Engineering](https://en.wikipedia.org/wiki/Feature_engineering) in order to model the temporal properties of the users and times over time.

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
