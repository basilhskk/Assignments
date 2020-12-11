import { Component,ViewChild } from '@angular/core';
import { IonicPage, NavController, NavParams,Slides} from 'ionic-angular';

@IonicPage()
@Component({
  selector: 'page-lesson1',
  templateUrl: 'lesson1.html',
})
export class Lesson1Page {
  @ViewChild(Slides)slides: Slides;
  imageContainer:any;
  constructor(public navCtrl: NavController, public navParams: NavParams) {

    this.imageContainer=[{'path':'/numbers/one.png',name:'one - ου άν'},{'path':'/numbers/two.png',name:'two - τού'},{'path':'/numbers/three.png',name:'three - θρί'},
    {'path':'/numbers/four.png',name:'four - φόρ'},{'path':'/numbers/five.png',name:'five - φάηβ'},{'path':'/numbers/six.png',name:'six - σίξ'},
    {'path':'/numbers/seven.png',name:'seven - σέβεν'},{'path':'/numbers/eight.png',name:'eight - έ ιτ'},{'path':'/numbers/nine.png',name:'nine - νά ιν'}]
  
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad Lesson1Page');
  }

  next(){
    this.slides.slideNext();
  }

  prev(){
    this.slides.slidePrev();
  }

}
