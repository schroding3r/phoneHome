import socket
import threading
SERVER = '10.50.28.15'

# Here's our thread:
class ConnectionThread ( threading.Thread ):

   def run ( self ):
      
      client = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
      client.connect ( ( SERVER, 4444 ) )
      print client.recv ( 1024 )
      client.close()

# Let's spawn a few threads:
ConnectionThread().start()
