class ClassStaticTest {
    var test:Int
    func testSet() -> Int {
        print("static func")
        return 666
    }
    init() {
        self.test = 1
    }
}

let test = ClassStaticTest()
test
.test = 2
test.test

var aList = [1,2,3,4,5,6]
aList.last
let mappedResult = aList.map({$0*2})
for i in mappedResult
{
    print(i)
}
func closureTest() -> Int
{
    var closure : Int { return 666 }
    return closure
}
closureTest()
