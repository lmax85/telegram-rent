const filters = {};
const requireFiles = require.context('.', false, /\.js$/);

requireFiles.keys().forEach(fileName => {
  Object.assign(filters, requireFiles(fileName).default);
});

export default filters;
