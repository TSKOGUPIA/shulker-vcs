import os

def init(args):
    os.makedirs(".shulker/objects/blobs")
    if args.verbose == True:
        print("Created directory .shulker/objects/blobs")
    os.makedirs(".shulker/index")
    if args.verbose == True:
        print("Created directory .shulker/index")
    print("Created repository")