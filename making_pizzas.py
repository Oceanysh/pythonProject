# import pizza
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# from pizza import make_pizza
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_pizza as mp
import pizza as p
from pizza import *
mp(16, 'pepperoni')
p.make_pizza(16, 'pepperoni')
make_pizza(16, 'pepperoni')