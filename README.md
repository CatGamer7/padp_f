# Cool dispy exercise
Definitely did not copy that from the first example of dispy documentation. Processes a text document by removing punctuation marks and numerals.

# Launch server
From your venv directory (right where your python executable is):

`python dispynode.py -i {your_host} -s {secret_key}`

# launch client
Client program expects several environment variables:
- DISPY_SECRET - your secret key that is shared between servers and client
- DISPY_NODES - space-separated list of server hostnames

Then, run:

`python main.py -i {input_filename} -o {output_filename}`
