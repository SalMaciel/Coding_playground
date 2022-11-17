import Cocoa

var name = "Ted"
name = "Rebecca"

let user = "Daphne"
print(user)

let actor = "Tom Cruise"
let quote = "He tapped a sign saying \"Believe\" and walked away."
let movie = """
A day in
the life of an
Apple engineer
"""
print(actor.count)
print(quote.hasPreffix("He"))
print(quote.hasSuffix("Away."))

let score = 10
let higherScore = score + 10
let halvedScore = score / 2

var counter = 10
counter += 5
let number = 120
print(number.isMultiple(of: 3))
let id = Int.random(in: 1...1000)

let doubleVar = 3.0
let intVar = 3

let goodDogs = true
let gameOver = false
var isSaved = false
isSaved.toggle()

let name = "Taylor"
let age = 26
let message = "I'm \(name) and I'm \(age) years old."
print(message)

var colors = ["Red", "Green", "Blue"]
let numbers = [4, 8, 15, 16]
let readings = [0.1, 0.5, 0.8]
print(colors[0])
print(readings[2])
colors.append("Tartan")
colors.remove(at: 0)
print(colors.count)
print(colors.contains("Octarine"))

let employee = [
    "name": "Taylor",
    "Job": "Singer"
]
print(employee["job", default: "Unknown"])

var numbers = set([1, 1, 3, 5, 7, 9])
print(numbers)
numbers.insert(10)
numbers.contains(11)