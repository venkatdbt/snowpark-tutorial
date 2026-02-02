'''
ALL
DEBUG
INFO
WARNING
ERROR
FETAL

'''
# HOW TO ENABLE LOGGING IN SNOWPARK
# All:combination of all
# Debug:(fatal+error+warn+info+debug) To know minute information ) debugging the application ar devel,developers use this to understand application flow.step by ste inofrmation it logs
# info:(fatal+error+warn+info) Record messages about routine application operation.In real time system admin watch the info loags to ensure whats happening aon the system right now
# Warn:(fatal+error+warn) used to indicate that you migh havre a problem  unusuall situation
# Error:(Fatel+error) serious problems that you need to investigate.not fatal but still a problem
# Fatal: very serious error eg: 404 error when click on app
# OFF/Trace/

#  info,error,fatal mostly used ,warn too used in some cases

data = [("Banana",1000, "USA"), ("Carrots", 1500, "USA"), ("Beans",1600, "USA"), \
("Orange",2000, "USA"), ("Orange",2000,"USA"), ("Banana",400,"China"), \
("Carrots",1200, "China"), ("Beans",1500,"China"), ("Orange",4000,"China"), \
("Banana",2000, "Canada"), ("Carrots",2000,"Canada"), ("Beans",2000,"Mexico")] I

columns= ["Product", "Amount", "Country"]