import { Component, ViewChild } from '@angular/core';
import { IonicPage, NavController, NavParams, Slides } from 'ionic-angular';
import { AlertProvider } from '../../providers/alert/alert';

@IonicPage()
@Component({
  selector: 'page-exercise1',
  templateUrl: 'exercise1.html',
})
export class Exercise1Page {
  @ViewChild(Slides) slides: Slides;
  answer: string;
  imageContainer: any;
  constructor(public navCtrl: NavController, public navParams: NavParams, public alertProv: AlertProvider) {
    this.imageContainer = [{ 'path': '/numbers/one.png', name: 'one' }, { 'path': '/numbers/two.png', name: 'two' }, { 'path': '/numbers/three.png', name: 'three' },
    { 'path': '/numbers/four.png', name: 'four' }, { 'path': '/numbers/five.png', name: 'five' }, { 'path': '/numbers/six.png', name: 'six' },
    { 'path': '/numbers/seven.png', name: 'seven' }, { 'path': '/numbers/eight.png', name: 'eight' }, { 'path': '/numbers/nine.png', name: 'nine' }]
  }
  validate(answer) {
    if (answer == this.answer) {
      this.alertProv.showSuccess('Μπράβο το βρήκες, πάμε στο επόμενο', () => {
        this.answer = '';
        this.slides.slideNext();
      })
    } else {
      this.alertProv.showError('Προσπάθησε πάλι, πήγαινε στα μαθήματα για να το ξαναδείς, ή παρε μια βοήθεια!', () => { })
    }
  }

  help(answer) {
    this.alertProv.showHelp('Η λέξη αρχίζε με ' + answer.substring(0, 2), () => { })

  }

}
