import os
import json
from flask import Flask, request
from invisible_watermark import *
from img_watermark import *
app = Flask(__name__)

@app.route("/getimglist", methods=['GET'])
def getimglist():
    args = request.args
    if (args and args.get("id")):
        rootdir = '/home/specs/public_html/ymmts_imglist'
        foldercomponent = args.get("id")
        print(foldercomponent)
        prefixes =['invisible','watermark']
        Key =foldercomponent.split('_')[3]
        foldername = foldercomponent.split('_')[0] + '_' + foldercomponent.split('_')[1] + '_' + foldercomponent.split('_')[2]
        resp = []

        if ((foldername) and (len(foldername) > 0)):
            for root, subdirectories, files in os.walk(rootdir):
                for subdirectory in subdirectories:
                    if (foldername == subdirectory):
                        directory = r'%s' % os.path.join(root, subdirectory)

                        for filename in os.listdir(directory):
                          if not filename.startswith(tuple(prefixes))  :
                            visiblewatermark(directory,Key, filename)
                        for filename in os.listdir(directory):
                            if (filename.startswith('watermark' +'_' + Key)):
                              resp.append('https://specs-images.vinaudit.com/ymmts_imglist/' + foldername + '/' + filename)
        return json.dumps(resp)



@app.route("/getimglistInvisible", methods=['GET'])
def getimglistInvisible():
      args = request.args
      if (args and args.get("id")):
          rootdir = '/home/specs/public_html/ymmts_imglist'
          foldercomponent = args.get("id")
          WatermarkType = foldercomponent.split('_')[3]
          Key =foldercomponent.split('_')[4].lower()
          foldername = foldercomponent.split('_')[0] + '_' + foldercomponent.split('_')[1] + '_' + foldercomponent.split('_')[2]
          resp = []
          prefixes =['invisible','watermark']
          if ((foldername) and (len(foldername) > 0)):
              for root, subdirectories, files in os.walk(rootdir):
                for subdirectory in subdirectories:
                    if (foldername == subdirectory):
                       directory = r'%s' % os.path.join(root, subdirectory)
                       for filename in os.listdir(directory):
                           if not filename.startswith(tuple(prefixes))  :
                             encode(directory , filename , Key)
                       for filename in os.listdir(directory):
                           if (filename.startswith('invisibleWatermark' + '_' + Key)):
                             resp.append('https://specs-images.vinaudit.com/ymmts_imglist/' + foldername + '/' + filename)
          return json.dumps(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)