
import Foundation

let currentTime = Date()
let date1 = Date(timeIntervalSinceReferenceDate: 118800)
let date2 = Date(timeIntervalSinceReferenceDate: 128800)
let dateString = DateFormatter.localizedString(from: currentTime, dateStyle: DateFormatter.Style.medium, timeStyle: DateFormatter.Style.none)
let time = DateComponents(calendar: nil, timeZone: nil, era: nil, year: 2010, month:9 , day: 11, hour: nil, minute: nil, second: nil, nanosecond: nil, weekday: nil, weekdayOrdinal: nil, quarter: nil, weekOfMonth: nil, weekOfYear: nil, yearForWeekOfYear: nil)
time.month
let calendar = Calendar(identifier: Calendar.Identifier.iso8601)
calendar.component(Calendar.Component.day, from: date1) == calendar.component(Calendar.Component.day, from: date2)

private func queryDateCheck(selectedDate:Date, toCheckDate:Date) -> Bool {
    let yearCheck = calendar.component(Calendar.Component.year, from: selectedDate) == calendar.component(Calendar.Component.year, from: toCheckDate)
    let monthCheck = calendar.component(Calendar.Component.month, from: selectedDate) == calendar.component(Calendar.Component.month, from: toCheckDate)
    return yearCheck && monthCheck
}

queryDateCheck(selectedDate: date1, toCheckDate: date2)

var amount = 2.2		
amount = 4

