//export.js 를 통해서 모듈을 공급받아서 사용
import obj from "./export.js";
// exItem.PLAYERS.forEach(element => {
//    console.log(element) 
// });
// console.log(exItem.MAX_SIZE);
// console.log(exItem.add(10, 5));
obj.log();
let { template } = obj;
console.log(template);