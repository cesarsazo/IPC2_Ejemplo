import { Component, OnInit } from '@angular/core';
import { ConsumirService } from "../../Servicios/consumir.service";

@Component({
  selector: 'app-funcionalidad',
  templateUrl: './funcionalidad.component.html',
  styleUrls: ['./funcionalidad.component.css']
})
export class FuncionalidadComponent implements OnInit {

  constructor( private svc: ConsumirService ) { }

  ngOnInit(): void {
  }

  consumir(){
    alert("consumir !!!")    
    this.svc.obtenerTodo().subscribe( data =>{
      (Object.values(data)).forEach(element => {
        console.log(element)
      });
    });
  }

}
