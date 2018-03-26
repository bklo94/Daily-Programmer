
function turn(vehicles,peoples,buildings){
    var i;
    var tempList = [];
    for (i = 0; i < vehicles.length; i++){
        //if it is the start of the challenge, start moving the taxis to some buildings
        getPassAndPath(vehicles[i],peoples,buildings);
        if (isEmpty(vehicles[i]) == true){
            vehicles[i].name = i;
            vehicles[i].destination = buildings[i];
        }
        else{
            vehicles[i].destination = buildings[vehicles[i].path[0]];
            vehicles[i].path = vehicles[i].path.slice(0,1);
        }
        vehicles[i].moveTo(vehicles[i].destination);
    }
 }

function getPassAndPath(vehicles,peoples,buildings){
    var j;
    var passBuildList = [];
    for (j = 0; j < buildings.length; j++){
        if (checkLocation(vehicles,buildings[j]) == true){
            passBuildList = passInBuild(peoples,buildings[j]);
            pickUpPass(vehicles,peoples,passBuildList,buildings);
        }
    }
}

function pickUpPass(taxi,peoples,list,buildings){
    var i;
    var taxiPath = [];
    if (isFull(taxi) != true){
        for (i = 0;i < (list.length); i++){
            taxi.pick(peoples[list[i]]);
            taxiPath.push(peoples[list[i]].destination);
            taxi.path = convertPath(buildings,taxiPath);
        }
    }
}

function convertPath(buildings,pathList){
    var tempList = [];
    var i,j;
    for (i = 0; i < buildings.length;i++){
        for (j = 0; j < pathList.length;j++){
            if (buildings[i].name == pathList[j]){
                tempList.push(i);
            }
        }
    }
    return tempList;
}

 //initialize a dictionary of buildings
 function initCurrDest(vehicles,buildings){
     var i;
     var dict = {};
     for (i = 0; i < vehicles.length; i++){
         dict[i] = initBuildingDict(buildings);
     }
     return dict;
 }

//initialize a dictionary of buildings
function initBuildingDict(buildings){
    var i;
    var dict = {};
    for (i = 0; i < buildings.length; i++){
        dict[buildings.name] = 0;
    }
    return dict;
}


//determine if a vehicle is full or not
//returns true if the taxi is too full
//returns false if the taxi is not full
function isEmpty(taxi){
    return taxi.peoples.length == 0;
}

//determine if a vehicle is full or not
//returns true if the taxi is too full
//returns false if the taxi is not full
function isFull(taxi){
    return taxi.peoples.length == 4;
}

//finds the number of passengers per buildings
function passInBuild(pass,places){
    var i,a;
    var list = [];
    for(i = 0; i < pass.length;i++){
        if (pass[i].x == places.x && pass[i].y == places.y && pass[i].origin == places.name){
            list.push(i);
        }
    }
    return list;
}

//finds the number of people's destination from each building
function checkLocation(a,b){
    return (a.x == b.x) && (a.y == b.y);
}

function checkDistance(a,b){
    return Math.abs(a.x-b.x) + Math.abs(a.y-b.y);
}

function checkBuilding(place,buildings){
    var i;
    for (i = 0; i < buildings.length; i++){
        if (buildings[i].name == place){
            return i;
        }
    }
}
