import { createApp, watch } from 'vue'
import { createPinia } from 'pinia'


import App from './App.vue'
import router from './router'

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import { aliases, mdi } from 'vuetify/iconsets/mdi-svg'

import { createI18n } from 'vue-i18n'

import Polski from '@/locales/pl.json'
import English from '@/locales/eng.json'
import store from './stores/loginStore.js'


const vuetify = createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: 'dark'
  },
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi
    }
  }
})


const i18n = createI18n({
  locale: 'Polski',
  messages: {
    Polski,
    English
  }
})

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(vuetify)
app.use(i18n)
app.use(store)

app.mount('#app')

const storedLanguage = localStorage.getItem('language')
if (storedLanguage && (storedLanguage === 'Polski' || storedLanguage === 'English')) {
  i18n.global.locale = storedLanguage
}

watch(
  () => i18n.global.locale,
  (newLocale) => {
    localStorage.setItem('language', newLocale)
  }
)
