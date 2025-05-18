const fs = require("fs");
const input = fs.readFileSync("dev/stdin").toString().trim().split("\n");
const n = Number(input[0]);
let arr = [];
arr = input[1].split(" ");

arr.sort(function(a, b) {
        let str1 = a.toString();
        let str2 = b.toString();
        
        if (str1 === str2) {
            return 0;
        }
        
        if (str1 + str2 < str2 + str1)
            return 1;
        
        return -1;
    });

const result = arr.toString().replaceAll(",","");
const reg = /[1-9]/g;
reg.test(result) ? console.log(result) : console.log("0");