import { environment } from './../environments/environment';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  headers = new HttpHeaders({
    'Content-Type': 'application/json'
  })

  baseUrl = 'https://alcohol-tracker-db-api.herokuapp.com/api/newsletter_recipients1/';

  constructor(
    private httpClient: HttpClient,
  ) { }

  createRecipient(email: string) {
    const body = JSON.stringify({ email: email });
    const promise = new Promise((resolve, reject) => {
      this.httpClient.post(this.baseUrl, body, { headers: this.headers }).toPromise().then(
        response => {
          console.log(response)
          resolve();
        },
        error => {
          console.log(error);
          reject(error);
        })
    });
    return promise
  }
}
