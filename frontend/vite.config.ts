import path from "path";

import vue from "@vitejs/plugin-vue";
import { defineConfig } from "vite";
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  build: {
    rollupOptions: {
      external: ["vue-router"],
      output: {
        globals: {
          "vue-router": "VueRouter",
        },
      },
    },
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
});
