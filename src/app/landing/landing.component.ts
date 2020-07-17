import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { ApiService } from '../api.service';
import Swal from 'sweetalert2';

declare var particlesJS: any;


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
  ) {
    this.newsletterForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]]
    })
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
        response => {
          Swal.fire({
            title: "Good job!",
            text: "You email was posted! Check your inbox.",
            icon: "success",
          });
          console.log(response)
        }
      ).catch(
        error => {
          Swal.fire({
            title: "Hold on!",
            text: "That email was already registered. Try another email. :) ",
            icon: "warning",
          });
          console.log(error)
        }
      )
    this.newsletterForm.reset();

    
  }


  ngOnInit() {}
  
  
}