from tinq import Tinq
# from tinq.projects import Projects
#
# projects = Projects()
# print(projects.list())
t = Tinq()
analyze = t.sentiments(text='neat')
print(analyze)