from __future__ import print_function
import semantria
import uuid
import time

serializer = semantria.JsonSerializer()

session = semantria.Session("dfbebbb5-af94-43b4-96e0-81894a9bc3d3", "e28ebdff-84ef-478d-82a2-5b1f07284eb8", serializer, use_compression=True)

initialTexts = [
    "Lisa - there's 2 Skinny cow coupons available $5 skinny cow ice cream coupons on special k boxes and Printable FPC from facebook - a teeny tiny cup of ice cream. I printed off 2 (1 from my account and 1 from dh's). I couldn't find them instore and i'm not going to walmart before the 19th. Oh well sounds like i'm not missing much ...lol",
    "In Lake Louise - a guided walk for the family with Great Divide Nature Tours rent a canoe on Lake Louise or Moraine Lake  go for a hike to the Lake Agnes Tea House. In between Lake Louise and Banff - visit Marble Canyon or Johnson Canyon or both for family friendly short walks. In Banff  a picnic at Johnson Lake rent a boat at Lake Minnewanka  hike up Tunnel Mountain  walk to the Bow Falls and the Fairmont Banff Springs Hotel  visit the Banff Park Museum. The \"must-do\" in Banff is a visit to the Banff Gondola and some time spent on Banff Avenue - think candy shops and ice cream.",
    "On this day in 1786 - In New York City  commercial ice cream was manufactured for the first time."
]

for text in initialTexts:
   doc = {"id": str(uuid.uuid4()).replace("-", ""), "text": text}

   status = session.queueDocument(doc)
   if status == 202:
      print("\"", doc["id"], "\" document queued successfully.", "\r\n")

length = len(initialTexts)
results = []

while len(results) < length:
   print("Retrieving your processed results...", "\r\n")
   time.sleep(2)
   # get processed documents
   status = session.getProcessedDocuments()
   results.extend(status)

print(results)

for data in results:
   # print document sentiment score
   print("Document ", data["id"], " Sentiment score: ", data["sentiment_score"], "\r\n")
   results3 = {"Document: ", str(data["id"])}

   # print document themes
   if "themes" in data:
      print("Document themes:", "\r\n")
      for theme in data["themes"]:
         print("     ", theme["title"], " (sentiment: ", theme["sentiment_score"], ")", "\r\n")
         results2 = {str(theme["title"])}

   # print document entities
   if "entities" in data:
      print("Entities:", "\r\n")
      for entity in data["entities"]:
         print("\t", entity["title"], " : ", entity["entity_type"]," (sentiment: ", entity["sentiment_score"], ")", "\r\n")         
         results = {str(entity['title'] + " : "), str(entity["entity_type"])}
