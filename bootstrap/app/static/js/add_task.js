var today = new Date();

var year = today.getFullYear();
var month = today.getMonth()+ 1;
var day = today.getDate()
var hour = today.getHours();
var minutes = today.getMinutes();

if(month<10){
    month='0' + month
} 

if(day<10){
    day='0' + day
} 

if(hour<10){
    hour= '0' + hour
}

if(minutes < 10){
    minutes = '0' + minutes 
}

var min = year + '-' + month + '-' + day + 'T' + hour + ':' + minutes;
document.getElementById("beginning").setAttribute("min", min);