function turn(vehicles,peoples,buildings){
    var i;
    var tempList = [];
    initBuilding(buildings);
    for (i = 0; i < vehicles.length; i++){
        //if it is the start of the challenge, start moving the taxis to some buildings
        if (isEmpty(vehicles[i]) == true){
            vehicles[i].name = i;
            vehicles[i].destination = buildings[i];
            buildings[i].occupied = true;
        }
        else{
            vehicles[i].destination = buildings[vehicles[i].path[0]];
            buildings[vehicles[i].path[0]].occupied = true;
            vehicles[i].path = vehicles[i].path.slice(0,1);
        }
        getPassAndPath(vehicles[i],peoples,buildings);
        vehicles[i].moveTo(vehicles[i].destination);
    }
 }

function getPassAndPath(vehicles,peoples,buildings){
    var j;
    var passBuildList = [];
    var newDest;
    var randInt;
    for (j = 0; j < buildings.length; j++){
        if (checkLocation(vehicles,buildings[j]) == true){
            passBuildList = passInBuild(peoples,buildings[j]);
            if (passBuildList.length > 1){
                pickUpPass(vehicles,peoples,passBuildList,buildings);
                buildings[j].occupied = false;
            }
            else if (passBuildList.length == 0 || buildings[j].occupied == true){
                randInt = getRandomInt(0,5);
                newDest = buildings[randInt];
                if (randInt == j || newDest.occupied == true){
                    while(newDest.occupied == true || randInt == j){
                        randInt = getRandomInt(0,5);
                        newDest = buildings[randInt];
                    }
                }
                else{
                    vehicles.destination = newDest;
                    newDest.occupied = true;
                }
            }
        }
    }
}

function pickUpPass(vehicles,peoples,list,buildings){
    var i;
    var taxiPath = [];
    if (isFull(vehicles) != true){
        for (i = 0;i < (list.length); i++){
            var dist = checkDistance(vehicles,peoples[list[i]]);
            if (checkPaitence(peoples[list[i]],dist) > 0){
                vehicles.pick(peoples[list[i]]);
                taxiPath.push(peoples[list[i]].destination);
                vehicles.path = convertPath(buildings,taxiPath);
            }
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

function optimizePass(list,dist){
    var i;
    for (i = 0; i < list.length; i++){
        list[i]
    }
}

//determine if a vehicle is full or not
//returns true if the vehicles is too full
//returns false if the vehicles is not full
function isEmpty(vehicles){
    return vehicles.peoples.length == 0;
}

//determine if a vehicle is full or not
//returns true if the vehicles is too full
//returns false if the vehicles is not full
function isFull(vehicles){
    return vehicles.peoples.length == 4;
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

function checkPaitence(pass,turns){
    return pass.time - turns;
}

function getRandomInt(min,max){
    return Math.floor(Math.random()*(max-min + 1)) + min;
}

//initialize a dictionary of buildings
function initBuilding(buildings){
    var i;
    for (i = 0; i < buildings.length; i++){
        buildings[i].occupied = false;
    }
}
