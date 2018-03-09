function greeting(){
    var d = new Date();
    hour = d.getHours();

    var str = "Hello, Alexander";
    
    if(hour < 4){
        str = "Another late night, Alex?";
    }else if(hour < 12){
    	str = "Good Morning, Alexander.";
    }else if(hour < 19){
    	str = "Good Afternoon, Alexander.";
    }else{
    	str = "Good Evening, Alexander.";
    }

    return str;
}
