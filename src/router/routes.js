import { useUserStore } from "../stores/user";
const routes = [
  {
    path: "/login",
    name: "login",
    component: () =>
      import(/* webpackChunkName: "login" */ "../pages/login.vue"),
    meta: {
      authRequired: false,
    },
  },
  {
    path: "/preloader",
    name: "preloader",
    component: () =>
      import(/* webpackChunkName: "preloader" */ "../pages/Preloader.vue"),
    meta: {
      authRequired: false,
    },
  },
  {
    path: "/",
    name: "app",
    component: () => import("layouts/GithubLayout.vue"),
    // children: [{ path: "", component: () => import("pages/IndexPage.vue") }],
    children: [
      {
        path: "",
        name: "home",
        component: () => import("pages/Index.vue"),
        meta: {
          authRequired: true,
        },
      },
      {
        path: "/clients",
        name: "clients",
        component: () =>
          import(
            /* webpackChunkName: "clients" */ "../pages/clients/index.vue"
          ),

        meta: {
          authRequired: true,
        },
      },
      {
        path: "/clients/:id",
        name: "Client details",
        component: () =>
          import(
            /* webpackChunkName: "clients" */ "../pages/clients/Details.vue"
          ),
        meta: {
          authRequired: true,
        },
        beforeEnter: (to, from, next) => {
          // console.log("to", to);
          // console.log(from);
          to.params.from = from.path;
          next();
        },
        // props: (route) => ({ number: parseInt(route.params.number) }),
        props: true,
      },
      {
        path: "/appointments",
        name: "appointments",
        component: () =>
          import(
            /* webpackChunkName: "appointments" */ "../pages/appointments/index.vue"
          ),
        meta: {
          authRequired: true,
        },
      },
      {
        path: "/visits",
        name: "visits",
        component: () =>
          import(/* webpackChunkName: "visits" */ "../pages/visits/index.vue"),
        meta: {
          authRequired: true,
        },
      },
      {
        path: "/users",
        name: "users",
        component: () =>
          import(/* webpackChunkName: "users" */ "../pages/users/index.vue"),
        meta: {
          authRequired: true,
        },
      },
      {
        path: "/playground",
        name: "playground",
        component: () =>
          import(
            /* webpackChunkName: "playground" */ "../pages/playground/index.vue"
          ),
        meta: {
          authRequired: true,
        },
      },
    ],
    meta: {
      authRequired: true,
    },
  },
  {
    path: "/github",
    component: () => import("layouts/GithubLayout.vue"),
    children: [
      // { path: '', component: () => import('pages/content.vue') }
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
