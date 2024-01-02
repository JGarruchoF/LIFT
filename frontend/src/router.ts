import { RouteRecordRaw } from "vue-router";

import { createRouter, createWebHistory } from "@ionic/vue-router";

import MainView from "@/views/MainView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    redirect: "/home",
  },
  {
    path: "/",
    component: MainView,
    children: [
      {
        path: "",
        redirect: "/home",
      },
      {
        path: "home",
        component: () => import("@/views/HomeView.vue"),
      },
      {
        path: "training",
        component: () => import("@/modules/training/views/TrainingView.vue"),
      },
      {
        path: "library",
        // component: () => import('./views/LibraryPage.vue'),
      },
      {
        path: "search",
        // component: () => import('./views/SearchPage.vue'),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
