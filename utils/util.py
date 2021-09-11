import configparser
import random
import string

def readConfig():
  config = configparser.RawConfigParser()
  config.read('config.properties')
  return config
  
def getRandomString():
  letters = string.ascii_lowercase
  randomText =  ''.join(random.choice(letters) for i in range(10)) 
  return randomText
  

