function ensure(value) {
    if(value === undefined) {
        throw new Error('Value is undefined');
    }

    return value;
    }
    try {
    console.log(ensure());
    } catch(err) {
    console.log(err);
    }



// Write a function that converts user entered date formatted as M/D/YYYY to a format required by an API (YYYYMMDD). The parameter "userDate" and the return value are strings.

// For example, it should convert user entered date "12/31/2014" to "20141231" suitable for the API.

// function formatDate(userDate) {

//     let array = userDate.split("/");
//     console.log(array)
//     while(array[0].length < 2) {
//         array[0] = "0" + array[0];
//     }
//     while(array[1].length < 2) {
//         array[1] = "0" + array[1];
//     }
//     let arrayAnswer = array[2]+ array[0]+ array[1];
//     return arrayAnswer;
// } 



// console.log(formatDate("12/31/2014"));


function createCheckDigit(membershipId) {
    var str=membershipId
    var x = 0
    for (var i = 0; i < str.length; i++) {

    console.log(str[i])
    x+=parseInt(str[i])
    
}
    x=x.toString()
    if (x.length >=2){
        var j =0
        for (var i = 0; i < x.length; i++) {
                j+=parseInt(x[i])
            }

        }
        return j;

    }


console.log(createCheckDigit("55555"));