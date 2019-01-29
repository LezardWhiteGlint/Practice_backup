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

Rank.init(rawValue: 1)

enum Suit:Int {
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

Suit(rawValue:0)

struct Card {
    var rank: Rank
    var suit: Suit
    func simpleDescription() -> String {
        return "The \(rank.simpleDescription()) of \(suit.simpleDescription())"
    }
    func all_cards() -> [Card] {
        var set = [Card]()
        let rank_iter = [Rank.ace, Rank.two, Rank.three, Rank.four, Rank.five, Rank.six, Rank.seven, Rank.eight, Rank.nine, Rank.ten, Rank.jack, Rank.queen, Rank.king]
        let suit_iter = [Suit.spades, Suit.hearts, Suit.diamonds, Suit.clubs]
        for r in rank_iter {
            for s in suit_iter {
                set.append(Card(rank:r,suit:s))
            }
        }
        return set
    }
}

let threeOfSpades = Card(rank:.ace,suit: .spades)
let threeOfSpadesDescription = threeOfSpades.simpleDescription()
let cardtest = threeOfSpades.all_cards()
//func set_of_cards() -> Array<Any>{
//    var set = [Any]()
//    let rank = [1,2,3,4,5,6,7,8,9,10,11,12,13]
//    let suit = [0,1,2,3]
//    for r in rank {
//        for s in suit {
//            set.append(Card(rank:))
//        }
//
//    }
//    return set
//}
//
//let test = set_of_cards()
//test
protocol ExampleProtocol {
    var simpleDescription: String { get }
    mutating func adjust()
}

class SimpleClass: ExampleProtocol {
    var simpleDescription: String = "A very simple class."
    var anotherProperty: Int = 69105
    func adjust() {
        simpleDescription += "  Now 100% adjusted."
    }
}
var a = SimpleClass()
a.adjust()
let aDescription = a.simpleDescription

struct SimpleStructure: ExampleProtocol {
    var simpleDescription: String = "A simple structure"
    mutating func adjust() {
        simpleDescription += " (adjusted)"
    }
}
var b = SimpleStructure()
b.adjust()
let bDescription = b.simpleDescription

extension Double {
    func adjust() {
        if self < 0 {
             -self
        }
        if self >= 0 {
             self
        }
    }
}
(-1.2).adjust()
let protocolValue: ExampleProtocol = a
print(protocolValue.simpleDescription)
// Prints "A very simple class.  Now 100% adjusted."
//print(protocolValue.anotherProperty)  // Uncomment to see the error
enum PrinterError: Error {
    case outOfPaper
    case noToner
    case onFire
}
func send(job: Int, toPrinter printerName: String) throws -> String {
    if printerName == "Never Has Toner" {
        throw PrinterError.noToner
    }
    if printerName == "On Fire" {
        throw PrinterError.onFire
    }
    if printerName == "No Paper" {
        throw PrinterError.outOfPaper
        }
    return "Job sent"
}
do {
    let printerResponse = try send(job: 1040, toPrinter: "Never Has Toner")
    print(printerResponse)
} catch {
    print(error)
}
// Prints "Job sent"
do {
    let printerResponse = try send(job: 1440, toPrinter: "On Fire")
    print(printerResponse)
} catch PrinterError.onFire {
    print("I'll just put this over here, with the rest of the fire.")
} catch let printerError as PrinterError {
    print("Printer error: \(printerError).")
} catch {
    print(error)
}
let printerSuccess = try? send(job: 1884, toPrinter: "Mergenthaler")
let printerFailure = try? send(job: 1885, toPrinter: "Never Has Toner")

var fridgeIsOpen = false
let fridgeContent = ["milk", "eggs", "leftovers"]

func fridgeContains(_ food: String) -> Bool {
    fridgeIsOpen = true
    defer {
        fridgeIsOpen = false
    }
    
    let result = fridgeContent.contains(food)
    return result
}
fridgeContains("milk")
print(fridgeIsOpen)
// Prints "false"
fridgeContent.contains("leftovers")

func makeArray<Item>(repeating item: Item, numberOfTimes: Int) -> [Item] {
    var result = [Item]()
    for _ in 0..<numberOfTimes {
        result.append(item)
    }
    return result
}
makeArray(repeating: "knock", numberOfTimes: 4)
