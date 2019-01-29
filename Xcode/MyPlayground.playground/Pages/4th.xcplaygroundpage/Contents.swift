let minValue = UInt16.min  // minValue is equal to 0, and is of type UInt8
let maxValue = UInt64.max  // maxValue is equal to 255, and is of type UInt8
Int(2.934234)
let a = 2.0000
let b = Int(a)
if a == 2 {
    print("yes")
}
let c = "23"
Int(c)
let http404Error = (404, "Not Found")
let (statusCode, statusMessage) = http404Error
print("The status code is \(statusCode)")
// Prints "The status code is 404"
print("The status message is \(statusMessage)")
// Prints "The status message is Not Found"
let possibleNumber = "123"
let convertedNumber = Int(possibleNumber)
convertedNumber == nil
var test_num = 123
if let actualNumber = Int(possibleNumber) {
    print("The string \"\(possibleNumber)\" has an integer value of \(actualNumber)")
    if true {
        print("This is second if for \(actualNumber)")
    }
} else {
    print("The string \"\(possibleNumber)\" could not be converted to an integer")
}
let random_test = ["a","b","c"]
Int.random(in:0..<10)
random_test.randomElement()

let contentHeight = 40
let hasHeader = false
let rowHeight = contentHeight + (hasHeader ? 40 : 20)
// rowHeight is equal to 90
