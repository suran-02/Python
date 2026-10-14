## FILE HANDLING PROBLEMS

#1  Log File Analysis
# Find:
# Total number of log entries
# Number of ERROR messages
# Number of WARNING messages
# Number of INFO messages

#method 1
# with open("server.log","r") as file:
#    total = error = warning = info = 0
#    for line in file:
#        total += 1
#        level = line.split()[0]
#        if level == "ERROR":
#            error += 1
#        elif level == "WARNING":
#            warning += 1
#        elif level == "INFO":
#            info += 1
#
# print(f"Total number of entries -> {total}")
# print(f"Number of ERROR messages -> {error}")
# print(f"Number of WARNING messages -> {warning}")
# print(f"Number of INFO messages -> {info}")

#method 2
# counts = {
#     "INFO":0,
#     "WARNING":0,
#     "ERROR":0
# }
# total = 0
# with open("server.log", "r") as file:
#     for line in file:
#         total += 1
#         level = line.split()[0]
#
#         if level in counts:
#             counts[level] += 1
#
# print(f"Total entries: {total}")
# print(f"INFO: {counts['INFO']}")
# print(f"WARNING: {counts['WARNING']}")
# print(f"ERROR: {counts['ERROR']}")

#2 Find Top 3 Most Frequent Words
# words = {}
# with open("new_data.txt","r") as file:
#     for line in file:
#         string = line.split()
#         for i in string:
#             if i in words:
#                 words[i] += 1
#             else:
#                 words[i] = 1
# top_3 = sorted(words,key = lambda x:words[x], reverse=True)[:3]
# print(top_3)

#3 Merge Multiple CSV Files
