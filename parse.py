from em_psse import *

import argparse
import logging

logger = logging.getLogger('em.parse_raw')

parser = argparse.ArgumentParser(description='Parse PSSE Files')

parser.add_argument('--input',
	help="Input RAW file")
parser.add_argument(
	'-d', '--debug',
	help="Print lots of debugging statements",
	action="store_const", dest="loglevel", const=logging.DEBUG,
	default=logging.WARNING,
)
parser.add_argument(
	'-v', '--verbose',
	help="Be verbose",
	action="store_const", dest="loglevel", const=logging.INFO,
)

# parser.add_argument('--output', 
# 	help="Output base path")
# parser.add_argument('--store',
# 	nargs='?', 
# 	default="store.h5",
# 	help="Path for local hdf storage")

args = parser.parse_args()
logging.basicConfig(level=args.loglevel)
raw_data = parse_raw(args.input)

for i in raw_data:
	if 'df' in raw_data[i]:
		logger.debug('{}'.format(i))
		logger.debug('\n{}\n'.format(raw_data[i]['df'].head()))


formatted=format_all(raw_data)

df_zone=formatted.get('zone',None)
df_tf=formatted.get('transformer',None)
df_gen=formatted.get('gen')
df_branch=formatted.get('branch')
df_load=formatted.get('load')
df_bus=formatted.get('bus')


print(df_tf.head())
print(df_gen.head())