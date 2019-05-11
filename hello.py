from wit import Wit
import os

client = Wit(os.environ.get('WITAI_ACCESS_TOKEN'))
client.interactive()
