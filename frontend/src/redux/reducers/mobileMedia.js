const mobileMediaReducer = (state = false, action) => {
  switch (action.type) {
    case 'MOBILE':
      return !state;
    default:
      return state;
  }
};

export default mobileMediaReducer;
