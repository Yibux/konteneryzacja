import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import { VitePWA } from 'vite-plugin-pwa'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  publicDir: 'public',
  plugins: [
    vue(),
    VitePWA({
      registerType: 'autoUpdate',
      devOptions: {
        enabled: true
      },
      manifest: {
        theme_color: '#f69435',
        background_color: '#f69435',
        display: 'standalone',
        scope: '/',
        start_url: '/',
        short_name: '240754',
        name: 'Mateusz-Milczarek-innowacja',
        icons: [
          {
            src: '/icon-192x192.png',
            sizes: '192x192',
            type: 'image/png'
          },
          {
            src: '/icon-256x256.png',
            sizes: '256x256',
            type: 'image/png'
          },
          {
            src: '/icon-384x384.png',
            sizes: '384x384',
            type: 'image/png'
          },
          {
            src: '/icon-512x512.png',
            sizes: '512x512',
            type: 'image/png'
          }
        ]
      }
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
    extensions: ['.js', '.ts', '.d.ts', '.vue']
  }
  ,
	server: {
		proxy: {
			'/user': {
				target: 'http://0.0.0.0:4000',
				ws: true,
				changeOrigin: true
			},
      '/todo': {
        target: 'http://0.0.0.0:5000',
        ws: true,
        changeOrigin: true
		  }
	  }
  }
})
