var BASE_URL = 'http://' + location.hostname + ':' + location.port


load_profile = function (){
    var self = this;
    var xhr = new XMLHttpRequest();
    var url = "/get_profile/";
    xhr.open("POST", url, false);
    var response = "123"
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {

            response = JSON.parse(xhr.responseText);
            // console.log(xhr.responseText)
            // console.log(json.email + ", " + json.password);
        }
    };
    var data = JSON.stringify({"page": "1"});
    xhr.send(data)
    
    // console.log(response)
    return response
  }



