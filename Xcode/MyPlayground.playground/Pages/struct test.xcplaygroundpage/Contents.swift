struct Factory {
    var time_circle = 0.0
    var production_amount = 0.0
    var production_price = 0.0
    var resource_1_name = "resource"
    var resource_1_amount = 0.0
    var resource_1_price = 0.0
    var resource_2_name: String?
    var resource_2_amount: Double?
    var resource_2_price: Double?
    var resource_3_name: String?
    var resource_3_amount: Double?
    var resource_3_price: Double?
}

let wheat = Factory(time_circle: 60, production_amount: 20, production_price: 36, resource_1_name: "Energy Cell", resource_1_amount: 20, resource_1_price: 16, resource_2_name: nil, resource_2_amount: nil, resource_2_price: nil, resource_3_name: nil, resource_3_amount: nil, resource_3_price: nil)

let a = 1
var b:Int?
b = 2
var dictest = [String:Int]()
dictest["IamDick"] = 1
dictest["haha"] == nil
dictest["IamDick"] = (dictest["IamDick"] ?? 0) + 1
let c:Double = 0.1
let d:Int = 2
//c*d


struct Point {
    var x = 0.0, y = 0.0
}
struct Size {
    var width = 0.0, height = 0.0
}
struct Rect {
    var origin = Point()
    var size = Size()
    var center: Point {
        get {
            let centerX = origin.x + (size.width / 2)
            let centerY = origin.y + (size.height / 2)
            return Point(x: centerX, y: centerY)
        }
        set(newCenter) {
            origin.x = newCenter.x - (size.width / 2)
            origin.y = newCenter.y - (size.height / 2)
        }
    }
}
var square = Rect(origin: Point(x: 0.0, y: 0.0),
                  size: Size(width: 10.0, height: 10.0))
let initialSquareCenter = square.center
square.center = Point(x: 15.0, y: 15.0)
square.center = Point(x: 13.0, y: 13.0)
struct Cuboid {
    var width = 0.0, height = 0.0, depth = 0.0
    var volume: Double {
        return width * height * depth
    }
}
let fourByFiveByTwo = Cuboid(width: 4.0, height: 5.0, depth: 2.0)
print("the volume of fourByFiveByTwo is \(fourByFiveByTwo.volume)")


class SomeClass {
    static func someTypeMethod() {
        // type method implementation goes here
        print("Triggerred")
    }
}
SomeClass.someTypeMethod()

struct LevelTracker {
    static var highestUnlockedLevel = 1
    var currentLevel = 1
    
    static func unlock(_ level: Int) {
        if level > highestUnlockedLevel { highestUnlockedLevel = level }
    }
    
    static func isUnlocked(_ level: Int) -> Bool {
        return level <= highestUnlockedLevel
    }
    
    @discardableResult
    mutating func advance(to level: Int) -> Bool {
        if LevelTracker.isUnlocked(level) {
            currentLevel = level
            return true
        } else {
            return false
        }
    }
}
class Player {
    var tracker = LevelTracker()
    let playerName: String
    func complete(level: Int) {
        LevelTracker.unlock(level + 1)
        tracker.advance(to: level + 1)
    }
    init(name: String) {
        playerName = name
    }
}
var player = Player(name: "Argyrios")
player.complete(level: 1)
print("highest unlocked level is now \(LevelTracker.highestUnlockedLevel)")
struct typeMethod {
    static var belongsToStruct = 666
    var someValue = 0
    static func ValueBelongsToStruct() {
        print("Value belongs to struct \(belongsToStruct)")
    }
}
let typeMethodTest = typeMethod()
typeMethodTest.someValue
typeMethod.belongsToStruct
typeMethod.ValueBelongsToStruct()
struct TimesTable {
    let multiplier: Int
    subscript(index: Int) -> Int {
        return multiplier * index
    }
}
let threeTimesTable = TimesTable(multiplier: 3)
print("six times three is \(threeTimesTable[6])")

