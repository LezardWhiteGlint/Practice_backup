//let contentHeight = 40
//let hasHeader = false
//let rowHeight = contentHeight + (hasHeader ? 40 : 20)
//var let_test1 = 1
//let let_test:Int
//let_test =

if true || false {
    print("It works")
}
let softWrappedQuotation = """
The White Rabbit put on his spectacles.  "Where shall I begin,
please your Majesty?" he asked.

"Begin at the beginning," the King said gravely, "and go on
till you come to the end; then stop."
"""
let threeDoubleQuotationMarks = """
Escaping all three quotation
marks \"\"\"
"""
let _ = 1

func minMax(array: [Int]) -> (min: Int, max: Int)? {
    if array.isEmpty { return nil }
    var currentMin = array[0]
    var currentMax = array[0]
    for value in array[1..<array.count] {
        if value < currentMin {
            currentMin = value
        } else if value > currentMax {
            currentMax = value
        }
    }
    return (currentMin, currentMax)
}
let bounds = minMax(array: [])
//print("min is \(bounds.min) and max is \(bounds.max)")
func stepForward(_ input: Int) -> Int {
    return input + 1
}
func stepBackward(_ input: Int) -> Int {
    return input - 1
}
func chooseStepFunction(backward: Bool) -> (Int) -> Int {
    return backward ? stepBackward : stepForward
}
var currentValue = 3
let moveNearerToZero = chooseStepFunction(backward: currentValue > 0)
while currentValue != 0 {
    print("\(currentValue)... ")
    currentValue = moveNearerToZero(currentValue)
}
print("zero!")
var somelist = [1,2,3,4]
somelist.remove(at:0)
somelist

