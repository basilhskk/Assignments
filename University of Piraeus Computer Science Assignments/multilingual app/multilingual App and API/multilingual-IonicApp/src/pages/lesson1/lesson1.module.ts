import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { Lesson1Page } from './lesson1';

@NgModule({
  declarations: [
    Lesson1Page,
  ],
  imports: [
    IonicPageModule.forChild(Lesson1Page),
  ],
})
export class Lesson1PageModule {}
