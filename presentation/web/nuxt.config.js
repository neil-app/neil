const nuxtEnvs = {
  local: {
    buildEnv: "local",
    maintenanceMode: false,
    maintenancePassUserIds: [],
    baseURL: "http://localhost:5000",
    browserBaseURL: "http://localhost:5000",
    // browserBaseURL: "http://10.0.2.2:5000", // ie
    intercomAppId: "mdt4c02a",
    jupyterBaseURL: "http://localhost:8888",
  },
}

const env = nuxtEnvs[process.env.BUILD_ENV || "local"]

module.exports = {
  /*
  ** Headers of the page
  */
  head: {
    title: 'neil',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Nuxt.js project' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
  /*
  ** Customize the progress bar color
  */
  loading: { color: '#3B8070' },
  /*
  ** Build configuration
  */
  build: {
    /*
    ** Run ESLint on save
    */
    extend (config, { isDev, isClient }) {
      if (isDev && isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  }
}

