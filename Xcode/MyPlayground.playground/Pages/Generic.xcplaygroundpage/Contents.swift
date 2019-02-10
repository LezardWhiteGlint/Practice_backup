func swapTwoInts(_ a: inout Int, _ b: inout Int) {
    let temporaryA = a
    a = b
    b = temporaryA
}
var someInt = 3
var anotherInt = 107
swapTwoInts(&someInt, &anotherInt)
print("someInt is now \(someInt), and anotherInt is now \(anotherInt)")


func swapTwoValues<FFF>(_ a: inout FFF, _ b: inout FFF) {
    let temporaryA = a
    a = b
    b = temporaryA
}
swapTwoValues(&someInt,&anotherInt)
print("someInt is now \(someInt), and anotherInt is now \(anotherInt)")
true || false
