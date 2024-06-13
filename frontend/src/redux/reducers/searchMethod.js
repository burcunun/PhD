const searchMethodReducer = (state = 'dense_vectors', action) => {
  switch (action.type) {
    case 'DENSE_VECTORS':
      return 'dense_vectors';
    case 'ELASTIC_SEARCH':
      return 'multi_match';
    default:
      return state;
  }
};

export default searchMethodReducer;
