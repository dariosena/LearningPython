''' 
An example of how to connect to MongoDB 
PyMongo Tutorial
'''

import datetime
import pprint

from pymongo import MongoClient


def main():
  ''' Connect to MongoDB '''
  
  # mongodb client with several databases
  client = MongoClient('mongodb://127.0.0.1:27017/')
  
  # getting a database
  db = client.test_database
  
  # accessing a collection within a database
  collection = db.test_collection
  
  post = {
    'author': 'Mike',
    'text': 'My first blog post',
    'tags': ['mongodb', 'python', 'pymongo'],
    'date': datetime.datetime.utcnow()
  }
  
  posts = db.posts
  
  post_id = posts.insert_one(post).inserted_id
  
  print()
  print('post id: ', post_id)
  print('Collections list:', db.list_collection_names())
  print()
  
  print('Find one without criteria:')
  pprint.pprint(posts.find_one())
  print()
  
  print('Find one with criteria: author')
  pprint.pprint(posts.find_one({'author': 'Mike'}))
  print()
  
  # An ObjectId is not the same as its string representation
  print('Querying By ObjectId')
  pprint.pprint(posts.find_one({'_id': post_id}))
  
  print()


if __name__ == '__main__':
  main()

