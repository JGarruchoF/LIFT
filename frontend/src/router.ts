import { createRouter, createWebHistory } from '@ionic/vue-router';
import Main from './common/views/Main.vue'
import { RouteRecordRaw } from 'vue-router';

const routes: Array<RouteRecordRaw> = [
    {
        path: '/',
        redirect: '/home',
      },
      {
        path: '/',
        component: Main,
        children: [
          {
            path: '',
            redirect: '/home',
          },
          {
            path: 'home',
            component: () => import('./common/views/Home.vue'),
          },
          {
            path: 'radio',
            // component: () => import('./views/RadioPage.vue'),
          },
          {
            path: 'library',
            // component: () => import('./views/LibraryPage.vue'),
          },
          {
            path: 'search',
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