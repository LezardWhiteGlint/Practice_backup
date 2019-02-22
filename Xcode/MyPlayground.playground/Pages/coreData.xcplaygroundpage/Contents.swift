//: [Previous](@previous)

import Foundation
import CoreData

@objc(Cost)
public class Cost: NSManagedObject {
}
extension Cost {
    
    @nonobjc public class func fetchRequest() -> NSFetchRequest<Cost> {
        return NSFetchRequest<Cost>(entityName: "Cost")
    }
    
    @NSManaged public var date: NSDate?
    @NSManaged public var category: String?
    @NSManaged public var amount: Double
    @NSManaged public var reminder: String?
    
}

let nsManagedObjectContext: NSManagedObjectContext? = nil
func test() {
    guard let context = nsManagedObjectContext else {return}
    context
}

