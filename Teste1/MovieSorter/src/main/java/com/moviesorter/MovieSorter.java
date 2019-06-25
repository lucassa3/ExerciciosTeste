package com.moviesorter;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Arrays;
import java.util.Scanner;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

public class MovieSorter {
static String URL_STRING = "https://jsonmock.hackerrank.com/api/movies/search/?Title=";
	
	static JsonObject getJSONResponse(String params) throws IOException {
		URL url = new URL(URL_STRING + params);
		HttpURLConnection con = (HttpURLConnection) url.openConnection();
		con.setRequestMethod("GET");
		
		BufferedReader br = new BufferedReader(new InputStreamReader(url.openStream()));
		
		String response = "";
		String line = "";
		while((line = br.readLine()) != null) {
			response += line;
			
		}
		br.close();
		
		return new Gson().fromJson(response, JsonObject.class);
	}
	
	static int getTotalPages(String movie_substr) throws IOException {
		JsonObject json_parser = getJSONResponse(movie_substr);
		return json_parser.get("total_pages").getAsInt();
	}
	
	static int getTotalMovies(String movie_substr) throws IOException {
		JsonObject json_parser = getJSONResponse(movie_substr);
		return json_parser.get("total").getAsInt();
	}
	
	static String[] getMoviesOnPage(String movie_substr, int page) throws IOException{
		JsonObject json_parser = getJSONResponse(movie_substr + "&page=" + Integer.toString(page));
		JsonArray movie_array = json_parser.get("data").getAsJsonArray();
		String movie_names[] = new String[movie_array.size()];
		
		for(int i = 0; i< movie_names.length; i++) {
			movie_names[i] = movie_array.get(i).getAsJsonObject().get("Title").getAsString();
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
