import dayjs from 'dayjs'

export default {
  formatDate: (value, format) => {
    return dayjs(value).format(format)
  },
}
