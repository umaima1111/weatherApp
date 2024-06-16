from flask import Flask, render_template ,request
import weatherApi


app=Flask(__name__)
data=""

@app.route("/")
def mainPage() :
 
  return render_template('weathermain.html',data=data)


@app.route("/weatherupdate", methods=['POST'])
def weatherupdate() : 
  
 
  if request.form.get('city_name') != "":
    print(request.form.get('city_name'))
    lat,lon= weatherApi.getLatLon(request.form.get('city_name'),request.form.get('state_code'),request.form.get('country_code'))
    data=weatherApi.getweatherUpdates(lat,lon)
    return render_template('weathermain.html',data=data)
  else :
    data=""
    return render_template('weathermain.html',data=data)



if __name__ == '__main__':
 app.run(debug=True)