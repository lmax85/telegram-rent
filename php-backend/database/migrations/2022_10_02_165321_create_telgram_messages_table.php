<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateTelgramMessagesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('telegram_messages', function (Blueprint $table) {
            $table->bigInteger('id');
            $table->unsignedBigInteger('telegram_group_id')->nullable()->index();
            $table->unsignedBigInteger('telegram_author_id')->nullable()->index();
            $table->unsignedInteger('city_id')->nullable()->index();

            $table->bigInteger('grouped_id');
            $table->text('text');
            $table->integer('price');
            $table->timestamps();
            $table->softDeletes();

            $table->primary(['id', 'telegram_group_id']);
            $table->foreign('telegram_group_id')->references('id')->on('telegram_groups')->onDelete('cascade');
            $table->foreign('telegram_author_id')->references('id')->on('telegram_authors')->onDelete('cascade');
            $table->foreign('city_id')->references('id')->on('cities')->onDelete('cascade');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('telegram_messages');
    }
}
