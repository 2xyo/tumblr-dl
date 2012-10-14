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
            
        
        path = item['image_store_path'] + ''.join(tmp_path) + '-' + item['image_url'].split('/')[-1]
        

        with open(path, "wb") as f:
            f.write(item['image'])
        f.close()
        
        return "Done : " + item['image_name']