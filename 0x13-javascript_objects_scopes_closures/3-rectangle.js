#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let pr = '';
      for (let i = 0; i < this.width; i++) {
        pr = pr + 'x';
      }
      console.log(pr);
    }
  }
}
module.exports = Rectangle;
