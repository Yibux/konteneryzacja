<script setup lang="ts">
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import store from './../stores/loginStore.js'

  const email = ref('')
  const password = ref('')
  const useRoute = useRouter()

  const handleSignUp = async () => {
    try {
      const response = await fetch('user/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          email: email.value,
          password: password.value
        })
      })
      console.log(response)
      
      if (response.ok) {
        const data = await response.json()
        console.log('data: ' + data)
        localStorage.setItem('authToken', data.token)
        localStorage.setItem('userId', data.userId)
        store.commit('setLoggedIn', true)
        store.commit('setUserId', data.userId)
        
        console.log('Response body values:')
        for (const key in data) {
          if (key === 'id') {
            store.commit('setUserId', data[key])
            localStorage.setItem('userId', data[key])
            console.log('getting id: ' + localStorage.getItem('userId'))
          }
          console.log(`${key}: ${data[key]}`)
        }
        
        useRoute.push('/todoList')
        console.log('Login successfull')
      } else {
        console.error('Failed to login')
      }
    } catch (error) {
      console.error('An error occurred during logging:', error)
    }
  }

</script>

<template>
  <v-row class="ma-4" justify="center">
    <h1>{{ $t('SignUp') }}</h1>
  </v-row>

  <v-form>
    <v-row justify="center" class="ma-4">
      <v-col cols="12" md="8"> </v-col>

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
          @click="handleSignUp"
          >{{ $t('SignUp') }}</v-btn
        >
      </v-col>

      <v-btn
        justify-center
        color="error"
        variant="plain"
        width="50%"
        class="rounded-pill"
        @click="() => $router.push('/register')"
        >{{ $t('NoAccount') }}
      </v-btn>
    </v-row>
  </v-form>
</template>
