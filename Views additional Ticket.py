class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ShowtimeListByMovie(generics.ListAPIView):
    serializer_class = ShowtimeSerializer

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Showtime.objects.filter(movie_id=movie_id)

class ShowtimeDetail(generics.RetrieveAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
