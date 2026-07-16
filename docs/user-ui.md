### React router

- use React router mode to integrate it in an existing project
- use a dedicated `routes.ts` file to specify your routes
- don't forget the `outlet` in the root route, children routes will be rendered in the `outlet`
- children/component `Hone` should have `index: true`
- the `router` is imported from `routes.ts` into `main.tsx` and passed to `<RouterProvider router={router}/>`

### Best practices:

#### absolute import

- absolute import using @, add the following to "compilerOptions" in `tsconfig.app.json`

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": [
        "./src/*"
      ]
    }
  }
}
```

```typescript
// vite.config.ts
import {defineConfig} from 'vite'
import path from 'path'

import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
    plugins: [react()],
    resolve: {
        alias: {
            '@': path.resolve(__dirname, './src'),
        },
    },
    server: {
        allowedHosts: [
            'demoapp.yassinecheffai.me'
        ]
    }
})
```