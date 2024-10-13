"""
This is Demo application for pipeline
"""
# import asyncio
# import subprocess
#
# command = ["ping", "www.google.com"]
#
# process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
#
#
# async def read_stream(stream):
#     while True:
#         line = stream.readline()
#         if not line:
#             break
#         print(line, end='')
#         await asyncio.sleep(1)
#
#
# async def other_thread():
#     while True:
#         print('Other thread is running')
#         await asyncio.sleep(1)
#
#
# async def demo():
#     await asyncio.gather(other_thread(), read_stream(process.stdout))
#
# asyncio.run(demo())
