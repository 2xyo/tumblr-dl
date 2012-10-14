from scrapy.contrib.pipeline.media import MediaPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
from PIL import Image
from cStringIO import StringIO
from twisted.internet import defer, threads
import string

class MyImagesPipeline(object):

    def process_item(self, item, info):
        """Returns the media requests to download"""

        tmp_path = []

        for e in item['image_name']:
            if e.isalnum():
                tmp_path.append(e)
                
            if e in string.whitespace :
                tmp_path.append("_")
            
        
        path = '/tmp/tumblr/'+ ''.join(tmp_path) + '-' + item['image_url'].split('/')[-1]
        

        with open(path, "wb") as f:
            f.write(item['image'])
        f.close()
        
        
        # let item be processed by other pipelines. ie. db store
        #return item
