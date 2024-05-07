<script>

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

      <!-- <v-col align="center" cols="12" md="8">
        <v-btn
          color="primary"
          variant="flat"
          width="70%"
          class="rounded-pill"
          @click="userStore.signIn"
          >{{ $t('SignUp') }}</v-btn
        >
      </v-col> -->

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
