import moment from 'moment';

let myDate = new Date();
let myCoolDate = moment(myDate).format("LL");
console.log(myCoolDate);