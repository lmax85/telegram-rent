export default function ({ app, $axios, redirect }) {
  $axios.onRequest(config => {
    // config.withCredentials = true;

    /* eslint-disable no-console */
    console.log('Making request to ' + config.url)
  })

  $axios.onResponse(response => {
    if (response.status === 401) {
      redirect('/login')
    }
  })
}
