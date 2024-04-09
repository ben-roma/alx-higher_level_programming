#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    // If w or h are not positive integers or are 0,
    // do not create width and height properties,
    // effectively making it an "empty" object.
  }
}

module.exports = Rectangle;
