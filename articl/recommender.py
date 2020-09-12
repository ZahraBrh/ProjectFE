from django.contrib.auth.models import User
from .models import ArticlPub,Note,Favorite
from accounts.models import Profile
from home.models import Follower
import numpy as np
from math import sqrt
import math

def my_cosine_similarity(A, B):
    result = 0.0
    
    numerator = np.dot(A,B)
    denominator = sqrt(A.dot(A)) * sqrt(B.dot(B))
    result = numerator / denominator
    return result


def get_follower_list(user):
    follower, created = Follower.objects.get_or_create(current_user=user)
    followers = follower.users.all().values('username')
    
        
def get_ratings_vector(user):
    ratings = Note.objects.filter(user_id=user,note__gt=0).values('articl', 'note')
    res = {}
    for r in ratings:
        res[r['articl']] = r['note']
    return res

def cosine_sim(user1_r,user2_r):
    result = 0.0
    l1=list(user1_r.keys())
    l2=list(user2_r.keys())
    #trouver les articls en commun par intersection entre les articles noté si 0 ils n'ont pas noté les memes articls sinn 
    common_item=list(set(l1).intersection(l2))
    if len(common_item) == 0:
        return 0
    
    top_result = 0.0
    bottom_left_result = 0.0
    bottom_right_result = 0.0
    #parcourir les articl
    for item in common_item:
        rxs = user1_r[item]
        rys = user2_r[item]
        # calcul numérateur note-user1 * note_user2
        top_result += (rxs) * (rys)
        #dénominateur
        bottom_left_result += pow(rxs, 2)
        bottom_right_result += pow(rys, 2)
    
    bottom_left_result = math.sqrt(bottom_left_result)
    bottom_right_result = math.sqrt(bottom_right_result)
    #numérateur/ dénominateur
    result = top_result / (bottom_left_result * bottom_right_result)
    
    return result

def user_average_rating(user_data):
    avg_rating = 0.0
    size = len(user_data)
    for rating in user_data.values():
        avg_rating += float(rating)
    avg_rating /= size * 1.0
    return avg_rating

def predict(item,knn , rating_user_context):
    users_corr=list(knn.keys())
    valid_users=check_nieghbors_validation(item, users_corr)
    if not len(valid_users):
        return 0.0
    
    top_result = 0.0
    bottom_result = 0.0
    avg_rating_user = user_average_rating(rating_user_context)
    for u in valid_users:
        rating_user = get_ratings_vector(u)
        u_similarity = knn[u]
        rating =rating_user[item.pk]
        avg_u=user_average_rating(rating_user)
        #calculer le numérateur
        top_result += u_similarity * (rating-avg_u )
        #calculer le  dénominateur
        bottom_result += u_similarity
        if bottom_result == 0 :
            return 0
    result = avg_rating_user+(top_result/bottom_result)
    return result


def check_nieghbors_validation(item, users_corr):
    result = []
    for user in users_corr:
        ratings = get_ratings_vector(user)
        if item.pk in ratings.keys():
            result.append(user)
    return result

def get_predict_list(user):
    users=User.objects.all().exclude(pk=user.pk)
    follower, created = Follower.objects.get_or_create(current_user=user)
    followers = follower.users.all().values('pk','username')
    v1 = get_ratings_vector(user.pk)
    if not v1:
        return[]

    profile_no_followed = []
    
    for u in users:
        if u.pk in followers.values():  
            continue
        profile_no_followed.append(u)
    
    
    similarity_to_user = {}
    
    for p in profile_no_followed:
        v2 = get_ratings_vector(p.pk)
        #calcul similarity
        similarity=cosine_sim(v1,v2)
        if similarity > 0 :
            similarity_to_user[p.pk]=similarity

    #tri de la liste des similarite
    list = []
    knn=sorted(similarity_to_user.items(),key=lambda t: t[1] , reverse=True)[:20]
    for i in knn:
        list.append(i[0])
    
    
    return list 

    
    


    






