const replaceDecimal = (number, n, x, s, c) => {
  const re = '\\d(?=(\\d{' + (x || 3) + '})+' + (n > 0 ? '\\D' : '$') + ')';
  const num = number.toFixed(Math.max(0, ~~n));

  return (c ? num.replace('.', c) : num).replace(new RegExp(re, 'g'), '$&' + (s || ','));
};

export default {
  /* remove last 0 from decimal number */
  formatNumberDecimal: (val) => {
    const decimal = val % 1;

    if (decimal === 0) {
      return replaceDecimal(parseFloat(val), 0, 3, ' ', '.')
    }
    if ((decimal.toFixed(0) + 0.0) - decimal.toFixed(1) !== 0) {
      return replaceDecimal(parseFloat(val), 1, 3, ' ', '.')
    }
    if ((decimal.toFixed(1) + 0.00) - decimal.toFixed(2) !== 0) {
      return replaceDecimal(parseFloat(val), 2, 3, ' ', '.')
    }
    if ((decimal.toFixed(2) + 0.000) - decimal.toFixed(3) !== 0) {
      return replaceDecimal(parseFloat(val), 3, 3, ' ', '.')
    }
  },
}
