import graphlab as gl
gl.canvas.set_target('browser')

filepath = '../../ml-data/people-example.csv'
sf = gl.SFrame(filepath)

sf['Full Name'] = sf['First Name'] + sf['Last Name']

print(sf['Full Name'])
