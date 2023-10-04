<template>
  <div class="container">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Log in</h1>

        <form @submit.prevent="loginForm">
          <div class="field">
            <label>Email</label>
            <div class="control">
              <input type="email" name="email" class="input" v-model="email">
            </div>
          </div>

          <div class="field">
            <label>Password</label>
            <div class="control">
              <input type="password" name="password" class="input" v-model="password">
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

export default {
  name: "LoginView",
  data() {
    return {
      email: "",
      password: "",
      errors: [],
    }
  },
  methods: {
    loginForm() {
      this.errors = []
      if (this.email === '') {
        this.errors.push("Email cannot be empty")
      }

      if (this.password === '') {
        this.errors.push("Password cannot be empty")
      }

      if (!this.errors.length) {
        this.$store.commit('setIsLoading', true)
        axios.defaults.headers.common['Authorization'] = ''
        localStorage.removeItem('token')

        const loginFormData = {
          email: this.email,
          password: this.password
        }

        axios
            .post('/api/v1/token/login/', loginFormData)
            .then(response => {
              const token = response.data.auth_token
              this.$store.commit('setToken', token)
              axios.defaults.headers.common['Authorization'] = 'Token ' + token
              localStorage.setItem('token', token)
              this.$router.push('/dashboard/my-account')
            })
            .catch(errors => {
              if (errors.response) {
                for (const property in errors.response.data) {
                  this.errors.push(`${errors.response.data[property]}`)
                }
              } else if (errors.message) {
                this.errors.push(errors.message);
              }
            })
      }
    }
  }
}
</script>