def d_senti(v):
    
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem import SnowballStemmer
    from nltk.tokenize import TweetTokenizer
    from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
    from sklearn.linear_model import LogisticRegression
    from sklearn.svm import SVC
    from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
    from sklearn.pipeline import make_pipeline, Pipeline
    from sklearn.model_selection import GridSearchCV
    from sklearn.metrics import make_scorer, accuracy_score, f1_score
    from sklearn.metrics import roc_curve, auc
    from sklearn.metrics import confusion_matrix, roc_auc_score, recall_score, precision_score
    import re 
    import pandas as pd
    from textblob import TextBlob 
    
    data=pd.read_csv("n.csv",  engine='python')
    
    def get_tweet_sentiment(tweet):
        analysis = TextBlob(clean_tweet(tweet))     
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'   

    def clean_tweet(tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())         

    sentiment=[]
    df=data["Doctor_Reviews"]
    for i in range(len(df)):
        n=df.iloc[i]
        senti=get_tweet_sentiment(n)
        sentiment.append(senti) 
    data["Doctor_sentiment"]=sentiment 
    
    d_list=data.loc[data["Diseases"]==v]
    l=list(d_list["Doctor"])
    doctor_list=list(set(l))
    doct=[]
    p=0
    neu=0
    neg=0
    
    for i in doctor_list:
        sd=d_list.loc[d_list["Doctor"]==i]
        s_count=list(sd["Doctor_sentiment"])
        pos=s_count.count("positive")
        neg=s_count.count("negative")
        nue=s_count.count("neutral")
        k={}
        hos=list(set(sd["Hospital"]))
        k["name"]=i
        k["Total"]=len(s_count)
        k["pos"]=pos
        k["nue"]=nue
        k["neg"]=neg
        k["hospital"]=hos[0]
        doct.append(k)
        pos=0
        nue=0
        neg=0
        print(k)
        
    return doct

def h_senti(v):
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem import SnowballStemmer
    from nltk.tokenize import TweetTokenizer
    from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
    from sklearn.linear_model import LogisticRegression
    from sklearn.svm import SVC
    from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
    from sklearn.pipeline import make_pipeline, Pipeline
    from sklearn.model_selection import GridSearchCV
    from sklearn.metrics import make_scorer, accuracy_score, f1_score
    from sklearn.metrics import roc_curve, auc
    from sklearn.metrics import confusion_matrix, roc_auc_score, recall_score, precision_score
    import re 
    import pandas as pd
    from textblob import TextBlob 
    data=pd.read_csv("n.csv",  engine='python')
    
    def get_tweet_sentiment(tweet):
        analysis = TextBlob(clean_tweet(tweet))     
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'                
    def clean_tweet(tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())         
    c=0
    sentiment=[]
    df=data["Hospital_Review"]
    for i in range(len(df)):
        n=df.iloc[i]
        senti=get_tweet_sentiment(n)
        sentiment.append(senti) 
    data["Hospital_sentiment"]=sentiment 
    d_list=data.loc[data["Diseases"]==v]  
    
    l=list(d_list["Hospital"])
    doctor_list=list(set(l))
    doct=[]
    p=0
    neu=0
    neg=0

    for i in doctor_list:
        sd=d_list.loc[d_list["Hospital"]==i]
        s_count=list(sd["Hospital_sentiment"])
        pos=s_count.count("positive")
        neg=s_count.count("negative")
        nue=s_count.count("neutral")
        k={}
        hos=list(set(sd["Hospital"]))
        k["Total"]=len(s_count)
        k["pos"]=pos
        k["nue"]=nue
        k["neg"]=neg
        k["hospital"]=hos[0]
        doct.append(k)
        pos=0
        nue=0
        neg=0
    return doct