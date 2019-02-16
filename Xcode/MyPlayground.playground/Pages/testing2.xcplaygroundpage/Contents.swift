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
