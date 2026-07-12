### React router

- use React router mode to integrate it in an existing project
- use a dedicated `routes.ts` file to specify your routes
- don't forget the `outlet` in the root route, children routes will be rendered in the `outlet`
- children/component `Hone` should have `index: true`
- the `router` is imported from `routes.ts` into `main.tsx` and passed to `<RouterProvider router={router}/>`