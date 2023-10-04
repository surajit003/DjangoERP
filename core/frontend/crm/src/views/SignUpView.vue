<template>
  <div class="container">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Sign up</h1>

        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Email</label>
            <div class="control">
              <input type="email" name="email" class="input" v-model="email">
            </div>
          </div>

          <div class="field">
            <label>First Name</label>
            <div class="control">
              <input type="text" name="first_name" class="input" v-model="first_name">
            </div>
          </div>

          <div class="field">
            <label>Last Name</label>
            <div class="control">
              <input type="text" name="last_name" class="input" v-model="last_name">
            </div>
          </div>

          <div class="field">
            <label>Password</label>
            <div class="control">
              <input type="password" name="password1" class="input" v-model="password1">
            </div>
          </div>

          <div class="field">
            <label>Confirm password</label>
            <div class="control">
              <input type="password" name="password2" class="input" v-model="re_password">
            </div>
          </div>
          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-success">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default {
  name: 'SignUpView',
  data() {
    return {
      email: '',
      first_name: '',
      last_name: '',
      password1: '',
      re_password: '',
      errors: [],
    }
  },
  methods: {
    submitForm() {
      console.log("submit form")
      this.errors = []

      if (this.email === '') {
        this.errors.push("Username cannot be empty")
      }

      if (this.first_name === '') {
        this.errors.push("First Name cannot be empty")
      }

      if (this.last_name === '') {
        this.errors.push("Last Name cannot be empty")
      }

      if (this.password1 === '') {
        this.errors.push("Password cannot be empty")
      }

      if (this.re_password === '') {
        this.errors.push("Confirm Password cannot be empty")
      }

      if (!this.errors.length) {
        const signUpFormData = {
          email: this.email,
          first_name: this.first_name,
          last_name: this.last_name,
          password: this.password1,
          re_password: this.re_password
        }
        axios
            .post("/api/v1/users/", signUpFormData)
            .then(response => {
              console.log("response" + response);
              toast({
                message: 'Account was created, please log in',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
              })
              this.$router.push("/login")
            })
            .catch(error => {
              if (error.response) {
                for (const property in error.response.data) {
                  this.errors.push(`${property}: ${error.response.data[property]}`);
                }
              } else if (error.message) {
                this.errors.push('Something went wrong. Please try again!');
              }
            })
      }
    }
  }
}
</script>