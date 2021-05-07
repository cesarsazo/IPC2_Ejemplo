import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class ConsumirService {

  url = "http://localhost:5000"

  constructor(private http: HttpClient) { }

  obtenerTodo() {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
        'Cache-Control': 'no-cache'
      })
    };
    return this.http.get(this.url+'/obtenerTodo', httpOptions);
  }

}
