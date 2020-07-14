import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { ApiService } from '../api.service';


@Component({
  selector: 'app-landing',
  templateUrl: './landing.component.html',
  styleUrls: ['./landing.component.css']
})
export class LandingComponent implements OnInit {

  newsletterForm: FormGroup;
  submitted: boolean;
  errorMsg = '';

  constructor(
    public fb: FormBuilder,
    public apiService: ApiService,
    private http: HttpClient
  ) {
    this.newsletterForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]]
    })
    this.http = http
  }

  get f() { return this.newsletterForm.controls; }

  registerData() {
    this.submitted = true;
    if (this.newsletterForm.invalid) {
      return (this.newsletterForm.reset());
    }
    var formData = new FormData();
    formData.append("email", this.newsletterForm.get('email').value);

    this.apiService.createRecipient(this.newsletterForm.get('email').value)
      .then(
        response => console.log(response)
      ).catch(
        error => {
          alert(`The unknown error has occurred: ${error}`);
        }
      )
  }


  ngOnInit(): void {
  }

} 
