const nuxtEnvs = {
  local: {
    buildEnv: "local",
    maintenanceMode: false,
    maintenancePassUserIds: [],
    baseURL: "http://localhost:5000",
    browserBaseURL: "http://localhost:5000",
  },
}

const env = nuxtEnvs[process.env.BUILD_ENV || "local"]

module.exports = {
  /*
   ** Headers of the page
   */
  head: {
    title: "neil",
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: "Nuxt.js project" }
    ],
    link: [
      {
        rel: "icon",
        type: "image/x-icon",
        href: "/favicon.ico"
      }
    ],
    script: [
      {
        src: "//amp.azure.net/libs/amp/latest/azuremediaplayer.min.js"
      }
    ]
  },
  css: [{ src: "~assets/main.sass", lang: "sass" }],
  modules: ["nuxt-fontawesome", "@nuxtjs/axios", "nuxt-buefy"],
  /*
   ** Customize the progress bar color
   */
  loading: { color: "#3B8070" },
  /*
   ** Build configuration
   */
  build: {
    vendor:
      process.env.NODE_ENV !== "production"
        ? ["babel-polyfill", "axios", "event-source-polyfill"]
        : ["babel-polyfill", "axios"],
    /*
     ** Run ESLint on save
     */
    extend(config, { isDev, isClient }) {
      if (isDev && isClient) {
        config.module.rules.push({
          enforce: "pre",
          test: /\.(js|vue)$/,
          loader: "eslint-loader",
          exclude: /(node_modules)/
        });
      }
      if (isClient) {
        config.devtool = "source-map";
      }
    }
  },
  axios: {
    // debug: true,
    requestInterceptor: (config, { store }) => {
      if (store.state.token) {
        config.headers.common["Authorization"] = `Bearer ${store.state.token}`;
      }
      return config;
    },
    baseURL: env.baseURL,
    browserBaseURL: env.browserBaseURL
  },
  fontawesome: {
    imports: [
      {
        set: "@fortawesome/free-solid-svg-icons",
        icons: ["fas"]
      }
    ]
  }
};
