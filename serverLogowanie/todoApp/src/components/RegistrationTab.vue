<script setup lang="ts">
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import store from './../stores/loginStore.js'

  const email = ref('')
  const password = ref('')
  const useRoute = useRouter()


  const registerUser = async () => {
    try {
      const response = await fetch('user/add', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'mode': 'no-cors'
        },
        body: JSON.stringify({
          email: email.value,
          password: password.value
        })
      })

      if (response.ok) {
        const data = await response.json()
        localStorage.setItem('authToken', data.token)
        localStorage.setItem('userId', data.id)
        store.commit('setLoggedIn', true)
        useRoute.push('/todoList')
        console.log('User registered successfully')
      } else {
        console.log(response.body)
      }
    } catch (error) {
      console.error('An error occurred during registration:', error)
    }
  }
</script>

<template>
  <v-row class="ma-4" justify="center">
    <h1>{{ $t('CreateAccount') }}</h1>
  </v-row>

  <v-form>
    <v-container>
      <v-row justify="center" class="ma-4">
        <v-col cols="12" md="8">
          <v-text-field
            v-model="email"
            :label="$t('Email')"
            placeholder="johndoe@gmail.com"
            type="email"
            variant="outlined"
          ></v-text-field>
        </v-col>

        <v-col cols="12" md="8">
          <v-text-field
            v-model="password"
            :label="$t('Password')"
            type="password"
            :hint="$t('PasswordHint')"
            variant="outlined"
          ></v-text-field>
        </v-col>

        <v-col align="center" cols="12" md="8">
          <v-btn
            color="primary"
            variant="flat"
            width="70%"
            class="rounded-pill"
            @click="registerUser"
          >{{ $t('Register') }}</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>
