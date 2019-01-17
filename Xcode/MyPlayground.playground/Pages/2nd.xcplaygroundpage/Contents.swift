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
