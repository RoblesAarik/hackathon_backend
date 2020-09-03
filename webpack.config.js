var path = require("path");
var webpack = require("webpack");
var BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  context: __dirname,
  mode: "development",

  entry: "./mysiteapp/mysite/static/js/index",

  output: {
    path: path.resolve("./mysiteapp/mysite/static/bundles/"),
    filename: "[name]-[hash].js",
  },

  plugins: [new BundleTracker({ filename: "./mysite/webpack-stats.json" })],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ["babel-loader"],
      },
    ],
  },
  resolve: {
    extensions: ["*", ".js", ".jsx"],
  },
};
