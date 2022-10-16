<?php

namespace App\Http\Controllers\Estate;

use App\Models\City;
use App\Models\Country;
use App\Models\Message;
use App\Http\Controllers\Controller;
use App\Http\Resources\Estate\MessageListResource;
use Spatie\QueryBuilder\AllowedFilter;
use Spatie\QueryBuilder\QueryBuilder;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

class MessageController extends Controller
{
    public function index(): JsonResource
    {
        $messages = QueryBuilder::for(Message::class)
            ->with(['photos', 'author', 'group'])
            ->when(request('city_id'), function ($query) {
                return $query->where('city_id', '=', request('city_id'));
            })
            ->defaultSort('-updated_at')
            ->allowedSorts('price', 'city_id', 'updated_at')
            ->allowedFilters([
                AllowedFilter::callback('price_min', function (Builder $query, $value) {
                    $query->where('price', '>=', $value);
                }),
                AllowedFilter::callback('price_max', function (Builder $query, $value) {
                    $query->where('price', '<=', $value);
                }),
            ])
            ->paginate(24);

        return (MessageListResource::collection($messages))
            ->additional([
                'meta' => [
                    'countries' => Country::all(),
                    'cities' => City::all(),
                    'price_max' => Message::query()
                        ->when(request('city_id'), function ($query) {
                            return $query->where('city_id', '=', request('city_id'));
                        })
                        ->max('price'),
                ],
            ]);
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        //
    }

    public function show(int $author_id, int $id)
    {
        $message = Message::query()
            ->where('id', '=', $id)
            ->where('telegram_author_id', '=', $author_id)
            ->with(['photos', 'author', 'group'])
            ->firstOrFail();

        return new MessageListResource($message);
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        //
    }
}
