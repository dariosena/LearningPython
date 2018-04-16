'''
Created on Apr 15, 2018

@author: dario
'''
import pprint

from sqlalchemy import create_engine
from sqlalchemy import desc, func
from sqlalchemy.orm import sessionmaker

from orm.model import Cookie

engine = create_engine('sqlite:///orm.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# Inserting a single object (1 object - 1 insert)
cc_cookie = Cookie(cookie_name='chocolate chip',
                   cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
                   cookie_sku='CC01',
                   quantity=12,
                   unit_cost=0.50)

session.add(cc_cookie)
session.commit()

# Multiple inserts with flush (2 objects - 2 inserts)
dcc = Cookie(cookie_name='dark chocolate chip',
             cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
             cookie_sku='CC02',
             quantity=1,
             unit_cost=0.75)

mol = Cookie(cookie_name='molasses',
             cookie_recipe_url='http://some.aweso.me/cookie/recipe_molasses.html',
             cookie_sku='MOL01',
             quantity=1,
             unit_cost=0.80)

session.add(dcc)
session.add(mol)

session.flush()
session.commit()

# Bulk inserting multiple records (2 objects - 1 insert) ==> FASTER
c1 = Cookie(cookie_name='peanut butter',
            cookie_recipe_url='http://some.aweso.me/cookie/peanut.html',
            cookie_sku='PB01',
            quantity=24,
            unit_cost=0.25)

c2 = Cookie(cookie_name='oatmeal raisin',
            cookie_recipe_url='http://some.okay.me/cookie/raisin.html',
            cookie_sku='EWW01',
            quantity=100,
            unit_cost=1.00)

session.bulk_save_objects([c1, c2])
session.commit()

#####################
# Summing our cookies
#####################
inv_count = session.query(func.sum(Cookie.quantity)).scalar()
print(inv_count)

################################
# Counting our inventory records
################################
rec_count = session.query(func.count(Cookie.cookie_name)).first()
print(rec_count)

###########################
# Renaming our count column
###########################
rec_count = session.query(
    func.count(Cookie.cookie_name).label('inventory_count')).first()

print(rec_count.keys())
print(rec_count.inventory_count)

######################################
# Filtering by cookie name with filter
######################################
record = session.query(Cookie).filter(
    Cookie.cookie_name == 'chocolate chip').first()
print(record)

##########################################
#  Filtering by cookie name with filter_by
##########################################
record = session.query(Cookie).filter_by(cookie_name='chocolate chip').first()
print(record)

########################################
# Finding names with “chocolate” in them
########################################
query = session.query(Cookie).filter(Cookie.cookie_name.like('%chocolate%'))
for record in query:
    print(record.cookie_name)


# Get all the cookies
def get_all():
    cookies = session.query(Cookie).all()
    pprint.pprint(cookies)

    # memory efficient
    for cookie in session.query(Cookie):
        print(cookie)


# Select only cookie_name and quantity
def select_one():
    print(session.query(Cookie.cookie_name, Cookie.quantity).first())


# Order by quantity ascending
def select_ordered():
    for cookie in session.query(Cookie).order_by(Cookie.quantity):
        print('{:3} - {}'.format(cookie.quantity, cookie.cookie_name))


# Order by quantity descending
def select_ordered_desc():
    for cookie in session.query(Cookie).order_by(desc(Cookie.quantity)):
        print('{:3} - {}'.format(cookie.quantity, cookie.cookie_name))

