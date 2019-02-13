import UIKit

var str = "Hello, playground"
var int = 1

//print("Hello World")
var test = 1
var test2 = 3
var test3 = 0
test3 = test + test2
print(test3)
let a = 1
var b = 2
b = 10
let c:Float = 5
//print(c)
print("There is \(a) a")
print("There is \(b) b")
print("Hello Again World")
var list_test = [1,2,3]
b = list_test[0]
list_test[0] = 4
list_test
list_test.append(5)
list_test.count
list_test.append(6)
list_test.count

var dic_test = ["game1":90,"game2":100]
dic_test["game3"]=500
let empty_array = [String]()
var ifList = [Int](0...9)
var result = [Int]()
for i in ifList{
    	result.append(i*2)
}
result = []
for i in ifList{
    result.append(i+2)
}
result = []
for i in ifList{
    if i%2 == 0{
        result.append(i)
    }
}

1 == 1
var optionalName: String? = "John Appleseed"
var greeting = "Hello!"
if let name = optionalName {
    greeting = "Hello, \(name)"
}
optionalName = nil
if let game = optionalName {
    greeting = "\(game)"
}

let test_double_question_mark = "\(optionalName ?? greeting)"
var nil_test = 0
nil_test
var while_count = 0
while true{
    result.append(1)
    while_count += 1
    if while_count > 10{
        break
    }
}
result
let vegetable = "red pepper"
switch vegetable {
case "celery":
    print("Add some raisins and make ants on a log.")
case "cucumber", "watercress":
    print("That would make a good tea sandwich.")
case let x where x.hasSuffix("pepper"):
    print("Is it a spicy \(x)?")
default:
    print("Everything tastes good in soup.")
}
repeat{
    result.append(2)
    while_count += 1
}while while_count<20
var total = 0
for i in 0...4 {
    total += i
}
print(total)
// Prints "6"
func playGame(_ person:String,_ game:String) -> String{
    print("operational")
    return "\(person) is going to play \(game)"
}
playGame("Sheldon","Kerbal Space Program")
func makeIncrementer() -> ((Int) -> Int) {
    func addOne(number: Int) -> Int {
        return 1 + number
    }
    return addOne
}
var increment = makeIncrementer()
increment(7)

var numbers = [20, 19, 7, 12]
numbers.map({ (number: Int) -> Int in
    if number%2 != 0{
        return 0
    }
    return number
})
class Game{
    var title = String()
    var price = Int()
    var hours = Float()
    
    init(title:String,price:Int,hours:Float){
        self.title = title
        self.price = price
        self.hours = hours
    }
    func play(hours:Float) {
        
    }
}
//let isInt = "sdf"
//isInt is Int
