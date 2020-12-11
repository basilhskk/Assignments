import { Component,ViewChild } from '@angular/core';
import { IonicPage, NavController, NavParams,Slides} from 'ionic-angular';


@IonicPage()
@Component({
  selector: 'page-lesson2',
  templateUrl: 'lesson2.html',
})

export class Lesson2Page {

  @ViewChild(Slides)slides: Slides;

  imageContainer:any;
  constructor(public navCtrl: NavController, public navParams: NavParams) {
    this.imageContainer=[{'path':'/animals/dog.jpg',name:'dog - ντόγκ'},{'path':'/animals/lamb.png',name:'lamb - λάμπ'},{'path':'/animals/shark.png',name:'shark - σάρκ'},
    {'path':'/animals/rat.png',name:'rat - ράτ'},{'path':'/animals/zebra.png',name:'zebra - ζέμπρα'},{'path':'/animals/monkey.png',name:'monkey - μόνκι'},
    {'path':'/animals/donkey.png',name:'donkey - ντόνκι'},{'path':'/animals/frog.png',name:'frog - φρόγκ'},{'path':'/animals/elephant.png',name:'elephant - έλεφαντ'}]
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
