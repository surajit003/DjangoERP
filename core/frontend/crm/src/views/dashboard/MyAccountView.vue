<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">My account</h1>
      </div>

      <div class="column is-12">
        <div class="buttons">
          <button @click="logout()" class="button is-danger">Log out</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name: "MyAccountView",
  methods: {
    async logout() {
     await axios
          .post('/api/v1/token/logout')
          .then(response => {
            console.log(response);
            this.$store.commit('removeToken')
            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')
            this.$router.push('/')
          })
          .catch(errors =>{
            console.log(JSON.stringify(errors))
          })
    }
  }
}
</script>