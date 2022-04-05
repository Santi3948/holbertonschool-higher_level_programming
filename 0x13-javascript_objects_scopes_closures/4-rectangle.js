#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (c) {
    let cha = 'x';
    if (c !== undefined) {
      cha = c;
    }
    for (let i = 0; i < this.height; i++) {
      let pr = '';
      for (let i = 0; i < this.width; i++) {
        pr = pr + cha;
      }
      console.log(pr);
    }
  }

  rotate () {
    const aux = this.height;
    this.height = this.width;
    this.width = aux;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
