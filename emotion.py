import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import indicoio
import operator
indicoio.config.api_key = 'c6923e17f19f2263eaa5f547f9f7d93d'

# emotion = {u'anger': 0.15266123410000002, u'surprise': 0.10423468050000001, u'sadness': 0.6441943645, u'fear': 0.06272097680000001, u'joy': 0.0361887999}

f = open('lyrics.txt', "r")
line = f.readline()
f.close()
emotion =  indicoio.emotion(line)

song = "good feeling"
print song

anger = emotion.get('anger')
surprise = emotion.get('surprise')
sadness = emotion.get('sadness')
fear = emotion.get('fear')
joy = emotion.get('joy')

print "anger: " + str(anger)
print "surprise: " + str(surprise)
print "sadness: " + str(sadness)
print "fear: " + str(fear)
print "joy: " + str(joy)

print "result: " + str(max(emotion.iteritems(), key=operator.itemgetter(1))[0])


objects = ('anger', 'surprise', 'sadness', 'fear', 'joy')
y_pos = np.arange(len(objects))
performance = [anger, surprise, sadness, fear, joy]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Probability')
plt.title('Emotion Analysis of ' + song)
 
plt.show()


print "done"

# # batch example
# indicoio.emotion([
#     "I did it. I got into Grad School. Not just any program, but a GREAT program. :-)",
#     "Like seriously my life is bleak, I have been unemployed for almost a year."
# ])