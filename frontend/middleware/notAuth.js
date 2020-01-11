export default function ({ store, redirect }) {
  // If the user is not authenticated
  if (!store.getters['user/getIsAuth']) {
    return redirect('/login/')
  }
}
