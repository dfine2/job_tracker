import { render, screen } from '@testing-library/react';
import Jobs from './Jobs';

test('renders learn react link', () => {
  render(<Jobs />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});

