# Hotel Reviews Classifier
#### A machine learning application built to predict the reliability of hotel reviews by classifying them as truthful or deceptive.

## Overview
Inspired by a user-centered research course project where we designed a travel planning tool, I decided to build a ML tool that can help users verify the truthfulness of online travel reviews. The datasets used are included in the Deceptive Opinion Spam Corpus that can be obtained from the two associated papers cited below.

I referred to a similar project example on datacamp.com initially, but changed how the data is organized and inputted, rewrote the functions for processing  input text, and also implemented two more classification models then compared their accuracies. 
<br><br>
## How to Run the App
1. Download the entire repository and ensure that the files are in the same folder.
2. Run `conda activate ml` to activate the conda environment.
3. Run `streamlit run app.py` to view the app on localhost.
<br><br>
#### References:<br>
[1] M. Ott, Y. Choi, C. Cardie, and J.T. Hancock. 2011. Finding Deceptive Opinion Spam by Any Stretch of the Imagination. In Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies.

[2] M. Ott, C. Cardie, and J.T. Hancock. 2013. Negative Deceptive Opinion Spam. In Proceedings of the 2013 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies.
