import { Component,ViewChild } from '@angular/core';
import { IonicPage, NavController, NavParams,Slides, Alert} from 'ionic-angular';
import { AlertProvider } from '../../providers/alert/alert';

@IonicPage()
@Component({
  selector: 'page-exercise2',
  templateUrl: 'exercise2.html',
})
export class Exercise2Page {
  
  @ViewChild(Slides)slides: Slides;
  answer:string;
  imageContainer:any;
  constructor(public navCtrl: NavController, public navParams: NavParams,public alertProv:AlertProvider) {
    this.imageContainer=[{'path':'/animals/dog.jpg',name:'dog'},{'path':'/animals/lamb.png',name:'lamb'},{'path':'/animals/shark.png',name:'shark'},
    {'path':'/animals/rat.png',name:'rat'},{'path':'/animals/zebra.png',name:'zebra'},{'path':'/animals/monkey.png',name:'monkey'},
    {'path':'/animals/donkey.png',name:'donkey'},{'path':'/animals/frog.png',name:'frog'},{'path':'/animals/elephant.png',name:'elephant'}]

  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad Exercise2Page');
  }


  validate(answer){
    if(answer == this.answer){
      this.alertProv.showSuccess('Μπράβο το βρήκες, πάμε στο επόμενο',()=>{
        this.answer='';
        this.slides.slideNext();
      })
    }else{
      this.alertProv.showError('Προσπάθησε πάλι, πήγαινε στα μαθήματα για να το ξαναδείς, ή παρε μια βοήθεια!',()=>{})
    }
  }
  help(answer){
    this.alertProv.showHelp('Η λέξη αρχίζε με '+answer.substring(0,2),()=>{})

  }

}
