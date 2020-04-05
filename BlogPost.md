# Guest post: Reimplementing the Bellkor Algorithm

Note: Results and proofreading remain...

## Post by: Dan Dixey, January 2018

### Introduction

In 2006 Netflix announced a data mining / machine learning competition in search of a model that could outperform their own ‘best’ collaborative filtering algorithm that had been developed internally called Cinematch. The competition became known as the ‘Netflix Prize’ and gained a lot of media attention during the two years that it ran for, with many teams from around the world competing for the grand prize - beating Netflix’s own algorithm and the allure of a $1 million dollar prize money. It’s important to recognise that this competition was years before Machine Learning gained the hype that we see today, years before Deep Learning had any profound impact with CNN’s and even before the role of the Data Scientist had even been coined. The Netflix Prize showcased an innovative way of open source collaboration and to bring the power of Machine Learning to the forefront of the business world.

This article will aims to discuss recommendation systems in general, the winning Netflix Prize solution and also my own implementation of the winning algorithm, Bellkor’s Pragmatic Chaos.

Recommended systems (ResSys) and collaborative filtering:

The Netflix competition was seeking to award the wining system that was capable of the achieving the smallest Root Mean Squared Error (RMSE) on an unseen validation dataset (similar to how Kaggle run their competitions). These systems known as a Recommendation systems are designed to help users discover items that they may like based on their previous rating history and also users with similar ratings behaviours to themselves. When running this kind of process at such a large scale, the need for algorithmic approach to solve this problem is clearly the only option. Its important to note even at the time of the competition that they will have had millions of users and tens of thousands of media items in their catalogue.

![Context](https://spatnaik77.files.wordpress.com/2013/07/user-user1.jpg)

Recommendation systems typically can be broken down into three categories; collaborative filtering, content-based filtering and hybrid systems, conceptually each of the methods are seeking to achieve the same end goal, which is to predict the preference that each user would give to an item. As shown in the image above Customer A and Customer B have similar buying patterns - both are purchasing music CD’s, since each customer (user) share similarities, conveyed by their similar dress, we are able to predict (filtering) suitable (recommendations) for customer B. This method is known commonly known as collaborative filtering. More concisely if customer A and B have close enough preferences then B is more than likely going to like a recommended item that Customer like over a otherwise randomly selected item. This type of recommendation is very common, companies such as Spotify, Netflix and Amazon all use this method and variants to give you product recommendation every time you use their service.

### Motivation

I’ll briefly discuss my own motivation for implementing the winning algorithm:

Firstly, recommendation systems are becoming more and more prevalent as companies are starting to become more data-driven and seeking to improve the customer experience. Its hard deny that personalisation is key in maintaining customer loyalty and engagement of a particular service. Therefore to gain an understanding and appreciation of the methods and implementation details of this algorithm I believe that its a good point in my career to learn and implement one from scratch.

Secondly, I enjoy the challenge of implementing from scratch algorithms and systems in my own time primarily to learn how to translate complex ideas into code. Also the feature engineering that was applied and used to predict the ratings and is explained and derived very well in the [paper](https://netflixprize.com/assets/GrandPrize2009_BPC_BellKor.pdf) is very clear and concise. Finally, the challenge of retracing the steps the original researchers/developers might have taken to get to their own implementation is definitely a learning strategy I like to pursue.
Overview and novelty of the Winning solution:

As mentioned earlier the paper explains in detail the core ideas linear model, incrementally adding additional complexity at each phase in the paper with applied examples in order to provide intuition as to why each new part was necessary. Core ideas that stood out for me were; modelling the temporal changing of behaviours, the grouping of blocks of time, modelling variability of ratings for each movie and the ability to model user ‘drift’ as their rating style changes over time. While they all not completely novel the combination to use and model them all simultaneously in my opinion is. The diagram below is the Bellkor Pragmatic Chaos algorithm:

		bui = µ +bu+αu ·devu(tui)+bu,tui +(bi+bi,Bin(tui) )·cu(tui)+bi, fui

With the inclusion of the base line predictors this became:

		rˆui = bui +q T i pu(tui)+|N(u)| − 1 2 ∑ j∈N(u) yj ! .

The winning team then applied this algorithm via the use of many different types of machine learning models essentially becoming an Ensemble of models. Despite all the successes of this competition and algorithm, the winning solution never ended up getting used by Netflix. Xavier Amatriain and Justin Basilico, part of the Personalization Science and Engineering at Netflix, after the event stated the complexity of the model was too high to warrant the benefit of releasing it into production and that the nature of Netflix’s business had evolved over the duration of the competition.

### Python implementation

Implementing the algorithm was an interesting process, having not done differentiation for a while (not in a professional setting), since leaving university, the derivation of the gradients was certainly stumbling block initially. To over come this I had to refresh my knowledge of the Chain and Product rules in order to do the derivation. Once this had been completed I was then ready to start implementing the algorithm.

For this I implemented the algorithm into distinct pieces of functionality, each as their own method within a Python Class; train, model, predict, initialise and gradient decent, working over the weekend I was quickly able to implement each part of the algorithm. Once complete I used the MovieLens 20M dataset to check that the data could be used by the model and all the parts were working as expected. The Python implementation can be found here: https://github.com/FunctorML/BellkorAlgorithm/blob/master/Bellkor/Algorithm.py

Interpretation of the models results:

TODO

### Next steps

In the next post I’ll discuss the implementations results, performance and the challenges that I ran into whilst writing the code.
