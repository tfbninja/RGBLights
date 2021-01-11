# from https://pypi.org/project/wolframalpha/
import wolframalpha
from rgblightsappid import *

def resolveListOrDict(variable):
  if isinstance(variable, list):
    return variable[0]["plaintext"]
  else:
    return variable["plaintext"]

app_id = appID  # get your own at https://products.wolframalpha.com/api/
client = wolframalpha.Client(app_id)

const = 0.6890909091
neededResult = 235/255.0

lastDiffNegative = True
incrementer = 1
totalAdd = incrementer
lastDifference = 0

masterIterator = 100
for i in range(masterIterator):
    res = client.query("integral(max(0,sin(x) + " + str(const + totalAdd) + "),0,2*pi) / integral(abs(sin(x) + " + str(const + totalAdd) + "),0,2*pi)")
    """
    for pod in res.pods:
        for sub in pod.subpods:
            print(sub.plainText)
    """
    #print(next(res.results).plainText)

    #taken from https://medium.com/@salisuwy/build-an-ai-assistant-with-wolfram-alpha-and-wikipedia-in-python-d9bc8ac838fe
    if res['@success'] == 'false':
         print('Question cannot be resolved')
      # Wolfram was able to resolve question
    else:
        result = ''
        # pod[0] is the question
        pod0 = res['pod'][0]
        # pod[1] may contains the answer
        pod1 = res['pod'][1]
        # checking if pod1 has primary=true or title=result|definition
        if (('definition' in pod1['@title'].lower()) or ('result' in  pod1['@title'].lower()) or (pod1.get('@primary','false') == 'true')):
          # extracting result from pod1
          result = resolveListOrDict(pod1['subpod'])
          trimmedResult = result[:20]
          if (lastDiffNegative != neededResult - float(trimmedResult) < 0):
              lastDiffNegative = not lastDiffNegative
              totalAdd -= incrementer
              incrementer /= -10
          elif (lastDifference < (neededResult - float(trimmedResult))) :
              incrementer = -incrementer / 2
          else:
              totalAdd += incrementer
          print(str(neededResult - float(trimmedResult)) + " is the difference WA returned for " +   str(result) + " using a query constant of " + str(const + totalAdd) +  " .")
          lastDifference = neededResult - float(trimmedResult)
