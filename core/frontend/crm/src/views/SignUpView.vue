<template>
  <div class="container">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Sign up</h1>

        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Email</label>
            <div class="control">
              <input type="email" name="email" class="input" v-model="username">
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
              <input type="password" name="password2" class="input" v-model="password2">
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
      username: '',
      password1: '',
      password2: '',
      errors: [],
    }
  },
  methods: {
    submitForm() {
      console.log("submit form")
      this.errors = []

      if (this.username === '') {
        this.errors.push("Username cannot be empty")
      }

      if (this.password1 === '') {
        this.errors.push("Password cannot be empty")
      }

      if (this.password2 === '') {
        this.errors.push("Confirm Password cannot be empty")
      }

      if (!this.errors.length) {
        const signUpFormData = {
          username: this.username,
          password: this.password1
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
            .catch(error =>{
              if(error.response){
                 console.log(error.response);
              }
              else if(error.message){
                console.log("error"  + error);
              }
            })
      }
    }
  }
}
</script>