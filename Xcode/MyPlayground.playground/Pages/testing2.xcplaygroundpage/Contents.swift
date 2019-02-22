class Cost {
    //MARK: Properties
    var date: String
    var category: String?
    var amount: Double
    var reminder: String?
    
    init?(date: String, category: String?, amount: Double, reminder: String?) {
        guard !amount.isEqual(to: 0.0) else {
            return nil
        }
        self.date = date
        self.category = category
        self.amount = amount
        self.reminder = reminder
    }
    
}

let cost = Cost(date: "", category: nil, amount: 0.0, reminder: nil)
Double("string")

class setGetTest {
    var input:Int
    var test:Int {
        set(value) {
            input = value * 10
            print("You are setting the var")
        }
        get {
            print("You are getting the var")
            return input/10
        }
    }
    init(input:Int) {
        self.input = input
    }
}

let setGet = setGetTest(input: 10)
setGet.input
setGet.test
setGet.test = 10
