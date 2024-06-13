const menuCollapseReducer = (state = false, action) => {
  switch (action.type) {
    case 'COLLAPSE':
      return !state;
    default:
      return state;
  }
};

export default menuCollapseReducer;
