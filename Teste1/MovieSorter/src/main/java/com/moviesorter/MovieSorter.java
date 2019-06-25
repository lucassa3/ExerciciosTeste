package com.moviesorter;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Arrays;
import java.util.Scanner;

import org.json.JSONArray;
import org.json.JSONObject;

public class MovieSorter {
static String URL_STRING = "https://jsonmock.hackerrank.com/api/movies/search/?Title=";
	
	static JSONObject getJSONResponse(String params) throws IOException {
		URL url = new URL(URL_STRING + params);
		HttpURLConnection con = (HttpURLConnection) url.openConnection();
		con.setRequestMethod("GET");
		
		Scanner scanner = new Scanner(url.openStream());
		
		String response = "";
		while(scanner.hasNext()) {
			response += scanner.next();
			
		}
		scanner.close();
		
		return new JSONObject(response);
	}
	
	static int getTotalPages(String movie_substr) throws IOException {
		JSONObject json_parser = getJSONResponse(movie_substr);
		return json_parser.getInt("total_pages");
	}
	
	static int getTotalMovies(String movie_substr) throws IOException {
		JSONObject json_parser = getJSONResponse(movie_substr);
		return json_parser.getInt("total");
	}
	
	static String[] getMoviesOnPage(String movie_substr, int page) throws IOException{
		JSONObject json_parser = getJSONResponse(movie_substr + "&page=" + Integer.toString(page));
		JSONArray movie_array = json_parser.getJSONArray("data");
		String movie_names[] = new String[movie_array.length()];
		
		for(int i = 0; i< movie_names.length; i++) {
			movie_names[i] = movie_array.getJSONObject(i).getString("Title");
		}
		
		return movie_names;
	}
	
	
	static String[] getMovieTitles(String movie_substr) throws IOException {
		int total_pages = getTotalPages(movie_substr);
		int total_movies = getTotalMovies(movie_substr);
		
		String titles[] = new String[total_movies];
		
		String movies_page[];
		int counter = 0;
		for(int i = 1; i<=total_pages; i++) {
			movies_page = getMoviesOnPage(movie_substr, i);
			for(int j = 0; j<movies_page.length; j++) {
				titles[counter] = movies_page[j];
				counter++;
			}	
		}
		
		return titles;
	}
	
	public static void main(String[] args) throws IOException {
		Scanner input = new Scanner(System.in);
		
		String final_list[] = getMovieTitles(input.nextLine());
		Arrays.sort(final_list);
		
		input.close();
		
		for (String name: final_list) {
			System.out.println(name);
		}	
	}
}
