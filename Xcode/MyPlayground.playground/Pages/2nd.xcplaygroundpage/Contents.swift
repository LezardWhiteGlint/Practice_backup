class Game{
    var title = String()
    var price = Int()
    var hours = Float()
    
    init(title:String,price:Int,hours:Float){
        self.title = title
        self.price = price
        self.hours = hours
    }
    func addHours(hours:Float) {
        self.hours += hours
    }
    var happyness:Float{
        get{
            return self.hours/100
        }
        set{
            self.hours = newValue * 100
        }
    }
}
var Kerbal = Game(title:"Kerbal",price:150,hours:50)
Kerbal.title
Kerbal.price
Kerbal.hours
Kerbal.addHours(hours:20.2)
Kerbal.hours
var MH = Game(title: "Monster Hunter", price: 500, hours: 800)
MH.hours
MH.happyness
MH.happyness = 10
Int("42")
var short:Int = 1
//short = nil
var test:Int? = 1
test = nil
if let testunwrapped:Int = test {
    print("OK\(testunwrapped)")
}

var mealPreference: String? = "Vegetarian"
if let unwrappedMealPreference: String = mealPreference {
    print("Meal: \(unwrappedMealPreference)")
}

var optionaltest1 : String? = nil
optionaltest1 = "Kerbal"


var religiousAffiliation: String? = "Rastafarian"
religiousAffiliation = nil
//if religiousAffiliation != nil { ... }
enum Rank: Int {
    case ace = 1
    case two, three, four, five, six, seven, eight, nine, ten
    case jack, queen, king
    
    func simpleDescription() -> String {
        switch self {
        case .ace:
            return "ace"
        case .jack:
            return "jack"
        case .queen:
            return "queen"
        case .king:
            return "king"
        default:
            return String(self.rawValue)
        }
    }
}
let ace = Rank.ace
let aceRawValue = ace.rawValue
if let convertedRank = Rank(rawValue: 3) {
    let threeDescription = convertedRank.simpleDescription()
}
enum Suit {
    case spades, hearts, diamonds, clubs
    
    func simpleDescription() -> String {
        switch self {
        case .spades:
            return "spades"
        case .hearts:
            return "hearts"
        case .diamonds:
            return "diamonds"
        case .clubs:
            return "clubs"
        }
    }
}
let hearts = Suit.hearts
let heartsDescription = hearts.simpleDescription()
enum Games{
    case game1,game2,game3
    func name() -> String{
        switch self {
            case .game1:
                return "Kerbal"
            case .game2:
                return "Monster Hunter World"
            case .game3:
                return "Eve Online"
        }
    }
    func price() -> Int{
        switch self {
        case .game1:
            return 150
        case .game2:
            return 400
        case .game3:
            return 800
        }
    }
}

var enum_test = Games.game1
enum_test.name()
enum_test.price()

enum Game_test{
    case game1
    case game2
}

var switch_test = Int()
switch_test = 3
switch switch_test {
case 1:
    print("One")
case 2:
    print("Two")
default:
    print("Magic Number")
}


enum ServerResponse {
    case result(String, String)
    case failure(String)
}

let success = ServerResponse.result("6:00 am", "8:09 pm")
let failure = ServerResponse.failure("Out of cheese.")

switch success {
case let .result(sunrise, sunset):
    print("Sunrise is at \(sunrise) and sunset is at \(sunset).")
case let .failure(message):
    print("Failure...  \(message)")
}

let binding_test = 1111
switch binding_test{
case let x:
    print(x)
}
switch failure {
case let .result(sunrise, sunset):
    print("Sunrise is at \(sunrise) and sunset is at \(sunset).")
case let .failure(message):
    print("Failure...  \(message)")
}

let switch_test_2 = "something"
switch switch_test_2 {
case let x:
    print("I got \(x)")
default:
    print("this is default")
}
let finalSquare = 25
var board = [Int](repeating: 0, count: finalSquare + 1)
board[03] = +08
board

