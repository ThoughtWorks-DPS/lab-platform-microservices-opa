from invoke import Collection

from tasks import systems
from tasks import slp

ns = Collection()

ns.add_collection(systems)
ns.add_collection(slp)
